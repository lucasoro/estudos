import pandas_datareader.data as web, datetime, pandas as pd

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2017,1,1)

facebook = web.DataReader('FB', 'yahoo', start, end)