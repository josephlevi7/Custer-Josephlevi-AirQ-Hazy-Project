Luis Rosales, Joseph-Levi Custer - ECE 5984 - Dec 2023
**********************************************************************************************************************************
Title: “Haziness In The Air”, Air Quality Predictions
**********************************************************************************************************************************
Project’s Function: The purpose of our model is to forecast air quality in various cities globally for the years 2023 to 2025, utilizing historical pollution data to identify trends and anticipate future air quality conditions. By analyzing patterns in key pollutants like PM2.5, PM10, carbon monoxide, and ozone, the model aims to provide accurate predictions that can inform public health initiatives, environmental policies, and urban planning strategies. 

Dataset: The dataset in question aggregates air pollution data from three global cities including Los Angeles, Paris, and Jakarta, spanning from January 1, 2020, to September 1, 2023. It focuses on key pollutants like PM2.5, PM10, carbon monoxide, and ozone, offering a comprehensive view of air quality trends in these urban areas. Data is sourced via the OpenWeatherMap's Air Pollution History API and is structured to include city, country, date, time, and pollutant levels, ultimately compiled into a DataFrame and stored as a CSV file in an AWS S3 bucket.

Pipeline / Architecture: The project utilizes Apache Airflow for workflow management, orchestrating tasks like data ingestion (with Python scripts), transformation, feature extraction, and machine learning modeling (LSTM for time series prediction). The data is stored and managed in AWS S3 buckets, ensuring scalable and efficient handling.

Data Quality Assessment: The data quality is assessed by checking for completeness, accuracy, and consistency. Specific focus is given to handling missing or anomalous values, particularly in the O3 column, and ensuring the dataset is up-to-date and reflective of true air quality conditions.

Data Transformation Models use: The project employs data transformations to handle missing values and scale features using MinMaxScaler from scikit-learn. The LSTM (Long Short-Term Memory) model is used for predicting future air quality, leveraging its ability to learn time-dependent data for accurate forecasting.
**********************************************************************************************************************************

Los Angeles, California, United States 

Poor Air quality in Los Angeles, CA was predicted to increase through 2024. Los Angeles continues to receive poor grades in terms of air quality. Carbon Dioxide (CO) continues to increase due to its high amount of vehicles including cars and airplanes – Los Angeles Aiport (LAX). Another critical factor for its poor air quality is that about 40% of imports arrive at the Los Angeles port. 

![LA-USA](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/d01c417d-816c-475a-8714-5100a968c4aa)

![chrome_hQXqvFGIps](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/8673addb-c82a-44c8-9519-b17b25bbf02b)

**********************************************************************************************************************************

Jakarta, Indonesia

Jakarta is experiencing one of the worst air quality in the world. Its air quality measurements of CO, O3, PM10, and PM2.5 are forecasted to increase – the increase is reaching serious unhealthy levels of air quality. Jakarta is host to many coal-fired power plants (CFPP) which has a detrimental effect on air quality. Even so, in 2022 CFPP’s in Indonesia caused caused 10,500 deaths in Indonesia. [Source]

![JK-IN](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/e5459bc0-b7b3-4fac-aa20-aae97f486f5c)

![chrome_Qyjhwy2mYM](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/98f8539c-36dc-4e65-acf9-8c9abb0e3348)

**********************************************************************************************************************************

Paris, France

France set up a road map to reduce its carbon emissions by 40% by 2030 beginning in 1990. France introduced its roadmap: The National Low-Carbon Strategy (Stratégie Nationale Bas-Carbone SNBC) – the roadmap provides guidelines to reduce carbon emissions in different industries. This roadmap is working for France based on the prediction shown below. Emissions are decreasing drastically and are maintained at a healthy level. 

An interesting fact about the upcoming Olympics 2024 is that the Seine River has been cleaned to host swimming competitions. It has been 80 years since it was safe to swim in the Seine! – now, clean air and water in Paris! 

![PA-FR](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/e103e3f8-ee3e-4843-a0fd-a0a4127b4ebb)

![chrome_yogEuoUn85](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/02d0a8b5-0be8-437f-b997-d612ec28aa2c)

**********************************************************************************************************************************
Thorough Investigation: Our "Hazy Skies" project, while successful in making predictions, faces accuracy challenges with R^2 scores between 0.30 and 0.50 across different cities, indicating a need for improvement. A key step forward is to significantly extend the dataset, potentially incorporating 30-50 years of historical data for each city to enhance the model's accuracy. Additionally, the project encountered computational limitations with AWS, as running the entire pipeline in Apache Airflow took 30-40 minutes. Therefore, the immediate focus should be on acquiring more comprehensive data and optimizing computational resources to train the model more effectively.
**********************************************************************************************************************************
Screenshots:

Below are screenshots of the different iterations that were performed in Apache Airflow during this project. 

![chrome_9zh3exNwhQ](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/ee5b6fa0-40c6-4193-9fb9-95c48b7af411)
![chrome_IWtj6huLss](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/d98f5309-0942-4314-a283-5b3c584d5ce4)
![chrome_l1l90P9Mad](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/02e25ee4-3051-4cc0-8663-aa8f454c94db)
![chrome_VJiZ8Wtm49](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/a9d550cb-564b-4424-bd85-5e549f9dc91c)
![data-prototype](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/4f9f0200-4445-4164-8b71-7c27c3bafea8)
![EXCEL_l4ORMhq042](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/63b06c58-07ef-4bb2-b7a9-cfe2e139560a)
![Test-002](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/04985506-deee-4fbf-8800-43c086838089)
![Test-004](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/251b64bb-40cd-40cc-8302-1cbaf0b254a9)
![chrome_a4fOsmSFqT](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/dbdab1e9-1a36-4a95-8e9e-9e34bb143c57)
![tableau_Q2rA2rSJWX](https://github.com/LRosal3s/Rosales-Luis-AirQ-Hazy-Project/assets/143309517/05ab60f4-7903-447a-8cab-5f7c3597ff33)


