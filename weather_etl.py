import tweepy
import requests
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_etl():

    api_key = "8a01b76965d97936653b32a17275337d"

    baseURL = "https://api.openweathermap.org/data/2.5/weather?q=toronto&appid=" + api_key

    response = requests.get(baseURL)
    data = response.json()


    df= pd.DataFrame([data])

    df.to_csv("s3://weather-airflow/toronto_weather.csv",index=False)
