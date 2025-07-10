# Importing libraries 
from binance.client import Client
from binance.enums import *
import logging



# Configure Logging file
logging.basicConfig(filename= "Trading Bot.log",                                     
                       level= logging.INFO,                                           
                       format= "%(asctime)s | %(levelname)s | %(message)s")       


# Connect to Binance Testnet

binance_api = input("Binance API Key:")
binance_api_secret = input("Binancey Secret API Key:")

client = Client(binance_api, binance_api_secret, testnet = True)        # connecting to future binance client


# Recieve CLI(command line interface) Inputs

symbol = input("Trading Symbol:").strip().upper()                       
action_bs = input("Action (Buy / Sell):").strip().upper()
type_ml = input("Type of Order (Market / Limit):").strip().upper()

if type_ml == "LIMIT":                        
    # Fetch current price 
    try:
        symbolticker = client.futures_symbol_ticker(symbol=symbol)          # gives dict with key values "symbol" and "price" 
        print(f"Current market price for {symbol} is {price}") 
                
    except Exception as x:
        print(f"Failed to fetch current price.\nError:{x}")
        logging.info("Couldn't fetch current market price and exited the code.")
        exit()     

limit_price = input("Limit Price:").strip()                                          
tif = input("Time in Force(GTC, FOK, IOC):").strip().upper()
quantity = input("Order Size:").strip()


# log_info 
log_info = (f" Input => Symbol = {symbol}, Action = {action_bs}, Type = {type_ml}, Limit Price = {limit_price}, TIF = {tif}, Qty = {quantity}")


               
# Time inforce Dictionary

tif_dict = {"IOC": TIME_IN_FORCE_IOC,                                          
            "FOK":TIME_IN_FORCE_FOK,
            "GTC":TIME_IN_FORCE_GTC}


# Place the order

try:
    order_details = {
        "symbol": symbol,
        "side": SIDE_BUY if action_bs == "BUY" else SIDE_SELL,
        "type": ORDER_TYPE_MARKET if type_ml == "MARKET" else ORDER_TYPE_LIMIT,
        "quantity": float(quantity)
    }

    if type_ml == "LIMIT":                                       
        order_details["price"] = float(limit_price)
        order_details["timeInForce"] = tif_dict.get(tif, TIME_IN_FORCE_GTC)            # fetch tif from tif_dict or use default value = TIME_IN_FORCE_GTC
        
    order = client.futures_create_order(**order_details)                               # Place an order on binance futures. ; ** : unpacking dict
    print("\nYour Order has been Placed Successfully!")
    print(order)                                                    
    logging.info(f"{log_info} | Order placed successfully.")

except Exception as e:                                                                 # error handlinng
    print("\nFailed to place order.")
    print(f"Error: {e} .\nPlease try again after some time.")
    logging.error(f"{log_info} | Order placement failed. | Reason: {e}")

