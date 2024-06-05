#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:35:52 2024

@author: danadayan
"""

# %% Import packages and variables
import requests
from bs4 import BeautifulSoup
import os as os
import pandas as pd

# %% Set directory
os.chdir("/Users/danadayan/Documents/Maruvka Lab/MS.c Bioinformatics/Disordered_proteins/PDB/")

# %% Import list of PDBs with chemical shifts file

nmr_pdbs = pd.read_csv("pdb_nmr_cs_all.txt", header = None)
nmr_pdbs.columns = ['pdb_id']

# Convert to a list
pdb_ids = list(nmr_pdbs['pdb_id'])

# Make it fit the PDB id
pdb_ids = [pdb.upper() for pdb in pdb_ids] 

# %% 
def get_pH_value(pdb_id):
    # URL of the web page
    url = f'https://www.rcsb.org/experimental/{pdb_id}'
    
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
                    return pH_value
        else:
            return "Table not found."
    else:
        return "Failed to retrieve the web page."


# %% Get pH values for wanted pdb
pH_values = {}

for pdb_id in pdb_ids:
    pH_value = get_pH_value(pdb_id)
    pH_values[pdb_id] = pH_value

# %% Save output dictionary
import json
with open('pH_values_nmr.json', 'w') as f:
    json.dump(pH_values, f)



