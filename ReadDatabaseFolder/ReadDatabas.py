#For File
import json

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

# Token is Your API 
notion_token = os.getenv("notion_token")

# Notion URL
notion_page_id = os.getenv("notion_page_id")
notion_database_id = os.getenv("notion_stockprices")

def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)


def safe_get(data, dot_chained_keys):

    keys = dot_chained_keys.split('.')
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data

def main():
    client = Client(auth=notion_token)
    
    db_info = client.databases.retrieve(database_id=notion_database_id)

    write_dict_to_file_as_json(db_info, 'ReadDatabaseFolder/db_info.json')

    db_rows = client.databases.query(database_id=notion_database_id)

    simple_rows = []

    for row in db_rows['results']:
        company_name = safe_get(row, 'properties.Company Name.title.0.plain_text')
        date = safe_get(row, 'properties.Date.date.start')
        price = safe_get(row, 'properties.Price.number')

        simple_rows.append({
            'Company Name': company_name,
            'Date': date,
            'Price': price
        })

    write_dict_to_file_as_json(simple_rows, 'ReadDatabaseFolder/simple_rows.json')


if __name__ == '__main__':
    main()