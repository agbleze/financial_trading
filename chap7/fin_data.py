#%% Yahoo financial data
from yahoofinancials import YahooFinancials as yf
import pandas as pd
aapl = yf('AAPL')

hist = aapl.get_historical_price_data('2020-01-01', '2020-12-31', 'daily')

print(hist)

#%%
hist_df = pd.DataFrame(hist['AAPL']['prices']).drop('date', axis=1).set_index('formatted_date')
print(hist_df)

#%%
# real-time data retrieval
print(aapl.get_stock_price_data())


#%% get financial statement

stmt = aapl.get_financial_stmts('quarterly', ['income', 'cash', 'balance'])
print(stmt)


#%% summary data retrieval

print(aapl.get_summary_data())

# %% Multiple-tickers retrieval

currencies = yf(['EURCHF=X', 'USDEUR=X', 'GBPUSD=x'])

#%%
print(currencies.get_historical_price_data('2020-01-01', '2020-12-31', 'weekly'))

# %%  #####   Exploring the pandas_datareader  ################

from pandas_datareader import data

start_date = '2010-01-01'
end_date = '2020-12-31'

#%%

aapl = data.DataReader('AAPL',# data_source= 'yahoo', 
                       start_date, end_date
                       )








# %%
