import pandas as pd
from prophet import Prophet

df = pd.read_csv("../data/deals.csv")

won = df[df["stage"]=="Closed Won"]

monthly = won.groupby("created_date")["value"].sum().reset_index()

monthly.columns = ["ds","y"]

model = Prophet()

model.fit(monthly)

future = model.make_future_dataframe(periods=180)

forecast = model.predict(future)

print(forecast.head())
