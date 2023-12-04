import requests
import pandas as pd
import s3fs

def blurrr():
    BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution/history"
    API_KEY = ''
    ''' 
    this is a list of all current cities we are pulling data from named "CITIES"
    So, for now we just pull them as is -- we can modify and change them however want want
    actually, in the final file, I did remove Cairo, Egypt and Bangkok Thailand because 
    the life expectancy is not on there for both those countries
    We can also remove the state column, its of no use at this point
    '''
    CITIES = {
        "Los Angeles": {"lat": 34.05, "lon": -118.25, "country": "United States", "state": "CA"},
        "Paris": {"lat": 48.8566, "lon": 2.3522, "country": "France", "state": ""},
        "Jakarta": {"lat": -6.2088, "lon": 106.8456, "country": "Indonesia", "state": ""},
    }

    #This sets the parameters for the time frame of the data
    all_records = []
    for city, details in CITIES.items():
        start_date = pd.Timestamp(year=2020, month=1, day=1)
        end_date = pd.Timestamp(year=2021, month=12, day=31)

        params = {
            'lat': details['lat'],
            'lon': details['lon'],
            'start': int(start_date.timestamp()),
            'end': int(end_date.timestamp()),
            'appid': API_KEY
        }

        #calls for the API
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        records = []

        for entry in data['list']:
            records.append({
                'City': city,
                'Country': details['country'],
                'State': details['state'],
                'Date': pd.Timestamp.utcfromtimestamp(entry['dt']).strftime('%m-%d-%Y %H:%M'),
                'PM2.5': entry['components']['pm2_5'],
                'PM10': entry['components']['pm10'],
                'CO': entry['components']['co'],
                'O3': entry['components']['o3']
            })
        all_records.extend(records)

    #pushes data to the dataframe
    df = pd.DataFrame(all_records)

    #pushes data to the AWS bucket -- if you want you can replace your own
    s3 = s3fs.S3FileSystem()
    DIR = 's3 bucket ouput'
    file_name = 'Data-Samples/airQuality.csv'
    s3_path = f'{DIR}/{file_name}'

    #creates a csv out of the data
    with s3.open(s3_path, 'w') as f:
        df.to_csv(f, index=False)

