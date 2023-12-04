import pandas as pd
from s3fs import S3FileSystem
from sqlalchemy import create_engine
from sqlalchemy import inspect
import numpy as np

def load_data():
    s3 = S3FileSystem()
    DIR_wh = 's3 bucket'

    # CSV Files
    jakarta_df = pd.read_csv(s3.open('{}/{}'.format(DIR_wh, 'Jakarta_transformed_data.csv')))
    la_df = pd.read_csv(s3.open('{}/{}'.format(DIR_wh, 'Los Angeles_transformed_data.csv')))
    paris_df = pd.read_csv(s3.open('{}/{}'.format(DIR_wh, 'Paris_transformed_data.csv')))

    engine = create_engine("mysql+pymysql://{user}:{pw}@{endpnt}"
                           .format(user="",
                                   pw="",
                                   endpnt="database"))

    inspector = inspect(engine)
    if 'josephlevi' not in inspector.get_schema_names():
        engine.execute("CREATE DATABASE {db}"
                       .format(db="pid"))  # Enter your desired schema name
    else:
        print("Attempted to create existing schema")

    engine = create_engine("mysql+pymysql://{user}:{pw}@{endpnt}/{db}"
                           .format(user="",
                                   pw="",
                                   endpnt="database",
                                   db="pid"))

    # Insert DataFrames into MySQL DB
    jakarta_df.to_sql('jakarta_clean', con=engine, if_exists='replace', index=False)
    la_df.to_sql('los_angeles_clean', con=engine, if_exists='replace', index=False)
    paris_df.to_sql('paris_clean', con=engine, if_exists='replace', index=False)
