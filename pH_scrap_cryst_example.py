#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
"""
Created on Mon May 27 14:11:29 2024

@author: danadayan
"""

import requests
from bs4 import BeautifulSoup

# URL of the web page
url = 'https://www.rcsb.org/experimental/1A2C'

# Send a GET request to fetch the HTML content of the page
response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Locate the table
    table = soup.find('table', class_='table table-hover table-responsive')
    if table:
        # Find all rows in the table
        rows = table.find_all('tr')
        # Extract the pH value from the third row and third column
        pH_value = rows[2].find_all('td')[2].text.strip()
        print("Extracted pH value:", pH_value)
    else:
        print("Table not found.")
else:
    print("Failed to retrieve the web page.")
