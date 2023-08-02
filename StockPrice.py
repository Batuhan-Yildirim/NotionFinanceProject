# Core Libraries
import pandas as pd
import numpy as np

# Data Library
import yfinance as yf

# For Notion
from notion_client import Client

#For API Key
import os
from dotenv import load_dotenv

#API keys hidden for security !!!
load_dotenv()

# Warning Signs
import warnings
warnings.filterwarnings('ignore')



####################################################
#                 Data                             #
####################################################  


# MCD = McDonald's Corporation 

Data = yf.Ticker("MCD")

Data_history = Data.history(period="max")

Data_history.index = Data_history.index.strftime("%Y-%m-%d")
Data_history.index = Data_history.index.astype(str)

Close_prcie = Data_history.iloc[-1][["Close"]].values
Date = Data_history.index[-1]

info_keys = Data.info.keys()          # Company information

Data_info = []

for i in info_keys:
    v = Data.info.get(i)
    Data_info.append(v)
Data_info = pd.DataFrame(Data_info, index = info_keys, columns=["Information"])
Data_info.index.name = "Title"

name = Data_info[Data_info.index == "longName"]["Information"][-1]

####################################################
#                 Notion                           #
####################################################  

# Token is Your API 
notion_token = os.getenv("notion_token")

# Notion URL
notion_page_id = os.getenv("notion_page_id")
notion_database_id = os.getenv("notion_stockprices")



def write_row(client, database_id, company_name, price, date):

    client.pages.create(
        **{
            "parent": {
                "database_id": database_id
            },
            'properties': {
                'Company Name': {'title': [{'text': {'content': company_name}}]},
                'Price':{'number': price},                              # For text {'rich_text': [{'text': {'content': price}}]},
                'Date': {'date': {'start': date}}
            }
        }
    )


def main():
    
    client = Client(auth=notion_token)
    user_id = name
    event =  Close_prcie[0]
    date = Date
    write_row(client, notion_database_id, user_id, event,date)

# For Multi upload data
'''
    for i in np.arange(0,len(Date)):
        user_id = name
        event =  Close_prcie[i][0]
        date = Date[i]
        write_row(client, notion_database_id, user_id, event,date)
'''

if __name__ == '__main__':
    main()

