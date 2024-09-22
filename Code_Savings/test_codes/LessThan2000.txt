'''
Referance:
    https://danisler.com/dev/notion-in-5-minutes
'''

# For Notion
from notion_client import Client
from pprint import pprint

#For Api Key
from dotenv import load_dotenv
import os


# Warning Signs
import warnings
warnings.filterwarnings('ignore')

#API keys hidden for security !!!
load_dotenv()

notion_token = os.getenv("notion_token")
notion_page_id = os.getenv("notion_page_id")

def main():
    client = Client(auth =notion_token)
    page_response = client.pages.retrieve(notion_page_id)

    pprint(page_response, indent=2)

if __name__ == '__main__':
    main()


