import requests
from bs4 import BeautifulSoup

# URL of the web page
url = 'https://www.rcsb.org/experimental/1J5M'

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
        # Iterate through rows and extract pH values from the correct column
        for row in rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) >= 6:  # Ensure there are enough columns
                pH_value = columns[5].text.strip()
                print("Extracted pH value:", pH_value)
    else:
        print("Table not found.")
else:
    print("Failed to retrieve the web page.")
