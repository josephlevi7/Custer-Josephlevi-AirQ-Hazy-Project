import s3fs
from s3fs.core import S3FileSystem
import pandas as pd
from sklearn.preprocessing import MinMaxScaler



def feature_reverse():
    s3 = S3FileSystem()

    # S3 paths
    original_data_path =  's3 bucket original file before transformation'
    scaled_data_path = 's3 bucket transformed data'  # Replace with your S3 path
    output_dir =   's3 bucket output' # Replace with your output S3 directory

    # Load original unscaled data from S3
    with s3.open(original_data_path, 'rb') as f:
        original_data = pd.read_csv(f)

    # Selecting the Features
    features = ['PM2.5', 'PM10', 'CO', 'O3']

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Fit the scaler to the original unscaled data
    scaler.fit(original_data[features])

    # Load the scaled data from S3
    with s3.open(scaled_data_path, 'rb') as f:
        scaled_data = pd.read_csv(f)

    # List of cities in the scaled data
    cities = scaled_data['City'].unique()

    for city in cities:
        # Filter data for the current city
        city_data = scaled_data[scaled_data['City'] == city].copy()

        # Transform the city data back to the original scale
        city_data[features] = scaler.inverse_transform(city_data[features])

        # Save the transformed data for the current city to a CSV file in S3
        city_output_file = f'{output_dir}/{city}_transformed_data.csv'
        with s3.open(city_output_file, 'w') as f:
            city_data.to_csv(f, index=False)