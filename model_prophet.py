import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from prophet import Prophet
import warnings

warnings.filterwarnings("ignore")

def model_prop(file_name):
    df = pd.read_csv(file_name)

    df['date_time'] = pd.to_datetime(df['date_time'])

    df.set_index('date_time', inplace=True)

    numeric_columns = df.select_dtypes(include='number').columns
    df_numeric = df[numeric_columns]

    df_daily = df_numeric.resample('D').mean()
    df_daily.reset_index(inplace=True)

    forecast_data = df_daily.rename(columns={"date_time": "ds", "tempC": "y"})

    model = Prophet()
    model.fit(forecast_data)
    forecasts = model.make_future_dataframe(periods=730)
    predictions = model.predict(forecasts)

    fig = model.plot(predictions)

    plt.xlabel('Date')
    plt.ylabel('Temperature')

    img_path = "static/temp.png"
    plt.savefig(img_path, format='png')
    plt.close()

    return img_path
