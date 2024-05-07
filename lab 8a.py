import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#prices of Tesla (TSLA) from January 1st 2019 to December 31st 2021.
API = 'I9C8DIPK13ODF4R2'
start = datetime.date(year=2019, month=1,  day=1)
end = datetime.date(year=2021, month=12,  day=31)
series = 'TSLA'
endpoints = 'av-monthly'
df = web.DataReader(series, endpoints, start, end, api_key=API)

#Hint: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-alphavantage
#Hint: https://www.alphavantage.co/support/#api-key
#  Then use Pandas DataReader's interface for Alpha Vantage, not the
#  API that they describe on their site (DataReader does all that for
#  you!)

# 2. Create a new column that holds the rolling 3 month average.
df['close_3mo'] = df['close'].rolling(3).mean()

# 3. Create a new dataframe from the base data from part 1 that resamples
# the data to quarterly, using the mean value.
df.index = pd.to_datetime(df.index)
df_quarter = df.resample('QS').mean()
# 4. Create a figure showing the time series for the monthly level and
# the monthly rolling average together.
fig, ax = plt.subplots(figsize=(16,9))
x = pd.to_datetime(df.index)
ax.plot(x, df['close'], 'r-', label='Mean Closing')
ax.plot(x, df['close_3mo'], 'b--', label='Mean Closing 3-mo MA')

ax.legend()
ax.set_title('Tesla Monthly Average Closing Stock Price')
ax.set_xlabel('')
ax.set_ylabel('Price ($)')
plt.show()

