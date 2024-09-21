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
notion_token = os.getenv("notion_invoice_token")

# Notion URL
notion_database_id = os.getenv("notion_invoice_db")

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

    write_dict_to_file_as_json(db_info, 'Invoice_db/invoice_rows_info.json')

    db_rows = client.databases.query(database_id=notion_database_id)

    simple_rows = []

    for row in db_rows['results']:
        trading_partner = safe_get(row, 'properties.Trading Partner.title.0.plain_text')
        invoice_number = safe_get(row,"properties.Invoice Number.rich_text.0.plain_text")
        invoice_date = safe_get(row, 'properties.Invoice Date.date.start')
        due_date = safe_get(row, 'properties.Due Date.date.start')
        amount = safe_get(row, 'properties.Amount.number')
        tax_amount = safe_get(row, 'properties.Tax Amount.number')
        invoice_status =safe_get(row,'properties.Invoice Status.select.name')

        simple_rows.append({
            'Trading Partner': trading_partner,
            'Invoice Number': invoice_number,
            'Invoice Date': invoice_date,
            'Due Date': due_date,
            'Amount': amount,
            'Tax Amount': tax_amount,
            'Invoice Status':invoice_status
        })

    write_dict_to_file_as_json(simple_rows, 'Invoice_db/invoice_rows.json')


if __name__ == '__main__':
    main()