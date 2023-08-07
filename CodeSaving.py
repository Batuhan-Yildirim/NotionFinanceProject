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
#                 Block                            #
#################################################### 

def write_text(token,page_id,script):
        client = Client(auth=token)
        client.blocks.children.append(
            block_id=page_id,
            children=[
                {
                    "object": "block",
                    "type": 'code',
                    'code': {"caption": [],
                            "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": script
                        }
                        }],
                        "language": "python"
                    }
                }
            ]
        )

####################################################
#                 File                             #
#################################################### 
    
def file(self):
        
        input_file_path = self
        output_file_path = "test_codes\script.txt"

        # Read the contents of the input .py file
        with open(input_file_path, "r") as inputfile:
            py_code = inputfile.read()

        # Write the contents to the output text file
        with open(output_file_path, "w") as outputfile:
            outputfile.write(py_code)

        print(f"Contents of '{input_file_path}' have been written to '{output_file_path}'.")

        
        file_path = output_file_path

        # Open the file for reading
        with open(file_path, "r") as file_data:
            # Read the entire content of the file
            content = file_data.read()

        print(f"Your Python Script length is -- {len(content)} --")

        return content 

class codesaving:

    def __init__(self,name,token,pageid):
        self.name = name
        self.token = token
        self.pageid = pageid
    ####################################################
    #                 Notion                           #
    #################################################### 
    
    def main(self):

        content = file(self.name)

        if len(content) <= 2000:
            first = content[:2000]
            second = content[2000:]

            list_1 = [first,second]
            for i in list_1:
               one = write_text(self.token,self.pageid,i)
        
        elif len(content) > 2000 and len(content) <= 4000:
            first_1 = content[:2000]
            second_1 = content[2000:4000]
            third = content[4000:]

            list_2 = [first_1,second_1,third]

            for n in list_2:
               two = write_text(self.token,self.pageid,n)

        elif len(content) > 4000 and len(content) <= 6000:
            first_2 = content[:2000]
            second_2 = content[2000:4000]
            third_1 = content[4000:6000]
            fourth = content[6000:]
            
            list_3 = [first_2,second_2,third_1, fourth]

            for k in list_3:
               three = write_text(self.token,self.pageid,k)

        elif len(content) > 6000 and len(content) <= 8000:
                
            first_3 = content[:2000]
            second_3 = content[2000:4000]
            third_2 = content[4000:6000]
            fourth_1 = content[6000:8000]
            fifth = content[8000:]

            list_4 = [first_3,second_3,third_2,fourth_1,fifth]
            
            for m in list_4:
                four = write_text(self.token,self.pageid,m)

        else:
            info = "Please this function is not available more than 8000 line"
            print(info)

        print("Completed !!")
        
        return one or two or three or four

        
        
     

  # Token is Your API 
notion_token = os.getenv("notion_token_2")

# Notion Page URL
notion_page_id = os.getenv("notion_page_id_2")


script = codesaving("StockPrice.py",notion_token,notion_page_id).main()
print(script)



