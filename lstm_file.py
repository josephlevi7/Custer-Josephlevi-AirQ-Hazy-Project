import numpy as np
import pandas as pd
from datetime import timedelta
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import r2_score
import s3fs

def lstm_model():
    # AWS S3 bucket directories
    DIR_input = 's3 bucket input'
    DIR_pred = 's3 bucket output'
    # Initialize S3 File System
    s3 = s3fs.S3FileSystem()

    # Load scaled data from S3
    with s3.open(DIR_input, 'rb') as f:
        df = pd.read_csv(f)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index(['City', 'Date'], inplace=True)

    # Predictions for each city
    cities = df.index.get_level_values(0).unique()

    all_predictions = pd.DataFrame()  # Create an empty DataFrame to store all predictions

    for city in cities:
        city_data = df.loc[city]
        features = ['PM2.5', 'PM10', 'CO', 'O3']
        city_data_features = city_data[features]

        time_steps = 5

        # Creating the dataset for LSTM
        Xs, ys = [], []
        for i in range(len(city_data_features) - time_steps):
            v = city_data_features.iloc[i:(i + time_steps)].values
            Xs.append(v)
            ys.append(city_data_features.iloc[i + time_steps].values)
        X, y = np.array(Xs), np.array(ys)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        # Define LSTM model
        model = Sequential()
        model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
        model.add(Dense(4))
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

        # Predict on the test dataset and calculate R^2 score
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        print(f"R^2 Score for {city}: {r2}")

        # Predictions from the latest data to a future date
        last_steps_data = city_data_features.iloc[-time_steps:].values.reshape((1, time_steps, 4))
        start_date = city_data.index[-1] + timedelta(hours=6)  # Incrementing by 6 hours
        end_date = pd.Timestamp('2025-01-01 00:00:00')

        city_predictions = []
        current_step = last_steps_data

        while start_date < end_date:
            next_step_pred = model.predict(current_step).flatten()
            next_step_input = np.append(current_step[:, 1:, :], next_step_pred.reshape(1, 1, -1), axis=1)
            formatted_pred = [start_date] + list(next_step_pred)
            city_predictions.append(formatted_pred)
            current_step = next_step_input.reshape((1, time_steps, 4))
            start_date += timedelta(hours=6)  # Incrementing by 6 hours

        # Convert predictions for the city to DataFrame
        city_predictions_df = pd.DataFrame(city_predictions, columns=['Date', 'PM2.5', 'PM10', 'CO', 'O3'])
        city_predictions_df.insert(0, 'City', city)

        # Concatenate the city predictions to the all_predictions DataFrame
        all_predictions = pd.concat([all_predictions, city_predictions_df], ignore_index=True)

    # Save all predictions to a single CSV file in S3
    with s3.open(f"{DIR_pred}/all_city_predictions.csv", 'w') as f:
        all_predictions.to_csv(f, index=False)