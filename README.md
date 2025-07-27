# Crypto Trading Bot App

## Overview: 
This is a simple trading bot app. That allows users to place orders(buy/sell), support the market or limit orders with price limit and quantity selection option. Also have the option to choose time in force. lt also keeps records of orders in logs and handles the error. 

## Skill/Tools:

- Python -  For writing basic coding and error handling.

- Python-binance - Python library to interact with Binance via api calls

- Binance Futures testnet - Virtual environment that provides fake currency to test bot. 

- API Key and Secret API Key:

To work with binance future testnet we require the API key and secret API key that can be created using their official website. 

- Steps to get api and secret api: login on official binance future testnet > api key > copy api key and secret api key



## Simple work process

- Input: Receives input from user 
- Add binance api key and api secret key
- Connects to binance server using client
- Place order: Execute the order using binance API
- Error handling: Handle the error occurred using basic python exception handling
- Logging: Save records of action, error, debugging, order placed in log file. Useful for future reference
- Creating simple app using streamlit
- Testing: Test if all code works right

## How to Run File

Open the code file in any python environment.(prefer vs code)
In the new terminal install binance using code 
pip install python-binance (for  jupyter notebook or google colab use !pip install python-binance)
Run the code(button available at top right corner side of vs code)
Give Input values in CLI (will be shown in terminal of vs code). Enter input value press Enter button from keyword.
Order will be placed and log file will be generated
The log file created will be saved in the same folder where your python code is running.
To run the Trading_Bot_app.py: install streamlit (skip if already installed) > in terminal give path to folder where file is saved > press Enter > in terminal streamlit run Trading_Bot_app.py > press Enter





## Future Improvements

### Service continuity to make it reliable for experienced users

Explanation: For now if code fails to fetch current market value for a given symbol it exists the code and the user can not buy/sell. In future we can make improvements to give an option to users to check the current price manually and buy/sell this will be useful for the experienced user and ensures the continuity of service. Meanwhile we can solve the problem of fetching current market prices. 
Benefit: Users can still buy/sell even if the price fetch code is not working properly. It will not affect the entire code.

### Troubleshoot Timestamp Error

Explanation: Sometimes due to some reason system and binance server time does not match so the system can not connect properly with the server this gives a timestamp error. Even though it is temporary it affects the user experience. We can add a code so that in any case the system time should match with binance server time.
Benefit: Code can run properly on any system irrespective of time setting on that system. Delays due to network issues and simple things will not affect app/code execution.






##### Note: Due to a timestamp issue, the log file currently shows error entries. The log file will be updated on github soon.
