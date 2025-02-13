import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from save_DF_analysis import save_dataframe_analysis

#Complete Historical Cryptocurrency Financial Data
df = pd.read_csv('consolidated_coin_data.csv')

#save information about db in text file with function
save_dataframe_analysis(df, 'data_analysis.txt')

# convert to datetime
df['Date'] = pd.to_datetime(df['Date'], errors = 'coerce')

# convert numeric values (Open, High, Low, Close, Volume, Market Cap)
numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']
for i in numeric_columns:
    df[i] = pd.to_numeric(df[i].astype(str).str.replace(',',''), errors='coerce')


# 1. Average closure price for each cryptocurrency
avg_close_price = df.groupby('Currency')['Close'].mean().reset_index().rename(columns={'Close': 'Average Close Price'})

# 2. Total bidding for each cryptocurrency
total_volume = df.groupby('Currency')['Volume'].sum().reset_index().rename(columns={'Volume': 'Total Volume'})

# 3. The greatest growth in one day (opening to closure)
df['Daily Change'] = df['Close'] - df['Open']
max_growth = df.loc[df['Daily Change'].idxmax(), ['Currency', 'Date', 'Open', 'Close', 'Daily Change']]

# 4. Greatest volatility (difference between High and Low)
df['Volatility'] = df['High'] - df['Low']
max_volatility = df.loc[df['Volatility'].idxmax(), ['Currency', 'Date', 'High', 'Low', 'Volatility']]

# Display results
print(" Average closure price for each cryptocurrency:")
print(avg_close_price)

print("\nTotal bidding for each cryptocurrency:")
print(total_volume)

# Output the greatest growth per day
print("\nThe greatest growth in one day:")
print(max_growth)

# Output of the greatest volatility
print("\nThe greatest volatility:")
print(max_volatility)
print('**************')
#  Definition of top 3 cryptocurrencies by average market capitalization
top_3_currencies = df.groupby('Currency')['Market Cap'].mean().nlargest(3).index

# Data filtration for top 3 cryptocurrencies
top_3_df = df[df['Currency'].isin(top_3_currencies)]

print(df.info())
df = df.dropna(subset=numeric_columns)

df.to_csv('modified_consolidated_coin_data.csv', index=False)

# Building a trend of market capitalization trend
plt.figure(figsize=(12, 6))
for currency in top_3_currencies:
    currency_data = top_3_df[top_3_df['Currency'] == currency]
    plt.plot(currency_data['Date'], currency_data['Market Cap'], label=currency)

plt.xlabel('Date')
plt.ylabel('Market capitalization (USD)')
plt.title('Market capitalization trend for top 3 cryptocurrencies')
plt.legend()
plt.xticks(rotation=45)
plt.show()
