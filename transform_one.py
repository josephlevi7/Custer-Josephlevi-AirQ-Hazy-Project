import pandas as pd
import s3fs


def cloudburst():
    '''
    as we mentioned -- the Ozone (O3) column is kinda messed up, goes to 0 soo, we just supply the avg>
    we may end up not even using the O3 column, the other columns such as PM 2.5 and PM 10 seem to be >
    '''
    file_in = 's3 bucket input'
    file_out = 's3 bucket output'

    s3 = s3fs.S3FileSystem(anon=False)

    with s3.open(file_in, 'r') as f:
        df = pd.read_csv(f, low_memory=False)

    city_o3_mean = df[df['O3'] != 0].groupby('City')['O3'].mean()

    for index, row in df.iterrows():
        if row['O3'] == 0:
            df.at[index, 'O3'] = city_o3_mean[row['City']]

    with s3.open(file_out, 'w') as f:
        df.to_csv(f, index=False)

