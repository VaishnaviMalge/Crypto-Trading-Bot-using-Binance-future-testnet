
import streamlit as st
from binance.client import Client
from binance.enums import *
import logging



# Configure Logging file
logging.basicConfig(filename= "Trading Bot.log",                                      
                       level= logging.INFO,                                           
                       format= "%(asctime)s | %(levelname)s | %(message)s")       

st.title("Trading Bot App")
st.write("Welcome in the trading bot app")
# get api and connect to binance
binance_api = st.text_input("Binance API Key")
binance_api_secret = st.text_input("Binancey Secret API Key")

# proceed only if api and secret api is given
if binance_api and binance_api_secret:
    try:
        client = Client(binance_api, binance_api_secret, testnet = True)        
        st.success("Successfully connected to server.")
    except Exception as e:
        st.error(f"Failed to connect to server. Error:{e}")
        st.stop()


# Recive order datails
symbol_list = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "ADAUSDT", "DOGEUSDT", "SOLUSDT", "DOTUSDT", "MATICUSDT"]

symbol = st.selectbox("Trading Symbol",symbol_list)     
action_bs = st.selectbox("Action",["BUY","SELL"])
type_ml = st.selectbox("Type of Order", ["MARKET" , "LIMIT"])

if type_ml == "LIMIT":                        
    # Fetch current price 
    try:
        symbolticker = client.futures_symbol_ticker(symbol=symbol)          # gives dict with key values "symbol" and "price" where price= current market price for that symbol
        price= symbolticker["price"]  
        st.info(f"Current market price for {symbol} is {price}") 
                
    except Exception as x:
        st.info(f"Failed to fetch current price.\nError:{x}")
        logging.info("Couldn't fetch current market price and exited the code.")
        exit()     

limit_price = st.number_input("Limit Price:", 0)                                         
tif = st.selectbox("Time in Force",["GTC", "FOK", "IOC"])
quantity = st.number_input("Order Size:")

# log_info 
log_info = (f" Input => Symbol = {symbol}, Action = {action_bs}, Type = {type_ml}, Limit Price = {limit_price}, TIF = {tif}, Qty = {quantity}")


 
# Time inforce Dictionary

tif_dict = {"IOC": TIME_IN_FORCE_IOC,                                          
            "FOK":TIME_IN_FORCE_FOK,
            "GTC":TIME_IN_FORCE_GTC}


# Submit-> Place order
if st.button("Submit"):
    try:
        order_details = {
            "symbol": symbol,
            "side": SIDE_BUY if action_bs == "BUY" else SIDE_SELL,
            "type": ORDER_TYPE_MARKET if type_ml == "MARKET" else ORDER_TYPE_LIMIT,
            "quantity": float(quantity)
        }

        if type_ml == "LIMIT":                                       
            order_details["price"] = float(limit_price)
            order_details["timeInForce"] = tif_dict.get(tif, TIME_IN_FORCE_GTC)            # fetch tif from tif_dict if it"s invalid use default value TIME_IN_FORCE_GTC
        
        order = client.futures_create_order(**order_details)                               # Place an order on binance futures. ; ** : unpacking dict
        st.success("\nYour Order has been Placed Successfully!")
        st.write(order)                                                    
        logging.info(f"{log_info} | Order placed successfully.")

    except Exception as e:                                                                 # error handlinng
        st.error("\nFailed to place order.")
        st.write(f"Error: {e} .\nPlease try again after some time.")
        logging.error(f"{log_info} | Order placement failed. | Reason: {e}")