import requests
from bs4 import BeautifulSoup
import json
import sqlite3 as db
import datetime

def extract(response):
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        #locate the price information
        keywords = ['price', 'amount', 'cost']
        
        for keyword in keywords:
            price_element = soup.find(lambda tag: keyword in tag.text.lower())
            if price_element:
                product_price = price_element.text.strip()
                obj=json.loads(product_price)

                time=datetime.datetime.now()
                pname=obj["name"]
                pprice=obj["offers"]["price"]

                cursor.execute('INSERT INTO prices(Time,Name,Price) VALUES(?,?,?)',(time,pname,pprice))
                print(f'Price of {pname} is {pprice}')
                break           
        else:
           print("Price information not found on the page.")
    else:
        print(f"Request failed with status code {response2.status_code}")


#CREATING DATABASE
connection=db.connect('prices.db')
cursor=connection.cursor()

#CREATING TABLE
cursor.execute('''
    CREATE TABLE IF NOT EXISTS prices (
        Time TEXT,
        Name TEXT,
        Price TEXT
    )
''')


product1 = '' #place url to product 1 within quotes
product2= ''   #place url to product 2 within quotes

# Create a session
s = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}

# Set headers for the session
s.headers.update(headers)

# Send a GET request within the session
response1 = s.get(product1, timeout=10)
response2 = s.get(product2, timeout=10)

extract(response1)
extract(response2)

connection.commit()
connection.close()
