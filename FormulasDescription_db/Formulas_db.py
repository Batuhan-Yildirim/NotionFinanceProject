# Core Libraries
import pandas as pd
import numpy as np

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
#                  Data                            #
#################################################### 

'''
Also, you can download financial formulas with this code.

headers = {
    'Content-Type': 'application/json'
}
formulas_request = requests.get(f'https://api.tiingo.com/tiingo/fundamentals/definitions?token={os.getenv("Tiingo_key")}', headers=headers)
formulas_data = formulas_request.json()
'''

# This is a saving .csv file
formulas_data = pd.read_csv("Formulas_db.csv")
formulas_data = formulas_data.drop(["Unnamed: 0"], axis=1)

Formulas = pd.DataFrame(formulas_data)
Formulas["units"][Formulas["units"].isnull() == True] = "No Units"


####################################################
#                 Notion                           #
####################################################  

# Token is Your API 
notion_token = os.getenv("notion_token")


notion_page_id = os.getenv("notion_page_id")
notion_database_id = os.getenv("notion_database_id_formulas")


def write_row(client, database_id, short_version, name, description,statement_type,units):

    client.pages.create(
        **{
            "parent": {
                "database_id": database_id
            },
            'properties': {
                'Short Version': {'title': [{'text': {'content': short_version}}]}, # These names have to match inside of your database
                'Name': {'rich_text': [{'text': {'content': name}}]},
                'Description': {'rich_text': [{'text': {'content': description}}]},
                'Statement Type': {'rich_text': [{'text': {'content': statement_type}}]},
                'Units': {'rich_text': [{'text': {'content': units}}]}
            }
        }
    )


def main():
    client = Client(auth=notion_token)

    for i in np.arange(0,len(Formulas)):
        short_version = Formulas.iloc[i]["dataCode"]
        name =  Formulas.iloc[i]["name"]
        description = Formulas.iloc[i]["description"]
        statement_type = Formulas.iloc[i]["statementType"]
        units = Formulas.iloc[i]["units"]
        write_row(client, notion_database_id, short_version, name,description,statement_type,units)

if __name__ == '__main__':
    main()