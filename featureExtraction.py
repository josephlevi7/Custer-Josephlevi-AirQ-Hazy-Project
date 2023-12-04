import s3fs
from s3fs.core import S3FileSystem
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def feature_extract():
    s3 = S3FileSystem()

    # S3 bucket directories
    DIR_wh = 's3 bucket input'
    DIR_output = 's3 bucket output'
    data_file = 'Data-Samples/airQuality_Trans.csv'

    # Load data from S3
    df = pd.read_csv(s3.open(f'{DIR_wh}/{data_file}'))

    # Convert 'Date' to datetime and set as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index(['City', 'Date'], inplace=True)

    # Filter for specific times: 0:00, 6:00, 12:00, 18:00, and 24:00
    times = ['00:00:00', '06:00:00', '12:00:00', '18:00:00']
    df = df[df.index.get_level_values('Date').strftime('%H:%M:%S').isin(times)]

    # Selecting the Features
    features = ['PM2.5', 'PM10', 'CO', 'O3']

    # Scaling the dataframe
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])

    # Save the scaled data to a single file
    combined_df = df.reset_index()

    # Push extracted features to data warehouse
    with s3.open(f'{DIR_output}/scaled_features.csv', 'w') as f:
        combined_df.to_csv(f, index=False)

