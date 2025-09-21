
import pandas as pd
import yfinance as yf

# Step 1: Defining the list of stock tickers to analyze
tickers_list = ['TCS.NS', 'INFY.NS', 'WIPRO.NS', 'RELIANCE.NS']

# Creating an empty list to store the results
all_data = []

print(f"Fetching data for: {tickers_list}")

# Step 2: Loop through each ticker in the list
for ticker in tickers_list:
    try:
        # Creating a Ticker object from the yfinance library
        stock = yf.Ticker(ticker)

        # Getting the P/E ratio from the .info dictionary
        pe_ratio = stock.info['trailingPE']
        
        # Storing the ticker and its P/E ratio in a dictionary
        stock_data = {
            'Ticker': ticker,
            'P/E Ratio': pe_ratio
        }
        
        # Adding this company's data to our main list
        all_data.append(stock_data)

    except Exception as e:
        # This is a safety net: if a ticker fails, it prints a message and continues
        print(f"Could not get data for {ticker}. Skipping.")


# Step 3: Creating a table (DataFrame) from our list of data and print it
df = pd.DataFrame(all_data)

print("\n--- Results ---")
print(df)
