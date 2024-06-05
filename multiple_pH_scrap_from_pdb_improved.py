#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:32:38 2024

@author: danadayan
"""

# %% Import packages and variables
import requests
from bs4 import BeautifulSoup
import os as os
import pandas as pd
from import_pdb_ids import pdb_ids

# %% Set directory
os.chdir("/Users/danadayan/Documents/Maruvka Lab/MS.c Bioinformatics/Disordered_proteins/PDB/")

# %% Function that will scrap the pH from HTML
def fetch_pH(pdb_id):
    url = f"https://www.rcsb.org/experimental/{pdb_id}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='table table-hover table-responsive')
        if table:
            rows = table.find_all('tr')
            if len(rows) > 2:
                cells = rows[2].find_all('td')
                if len(cells) > 2:
                    pH_value = cells[2].text.strip()
                    return pH_value
                else:
                    return "pH value not found in the expected cell"
            else:
                return "Not enough rows in the table"
        else:
            return "Table not found"
    else:
        return "Failed to retrieve the web page"


# %% Get pH values for wanted pdb
pH_values = {}

for pdb_id in pdb_ids:
    pH_value = fetch_pH(pdb_id)
    pH_values[pdb_id] = pH_value
    

# %% Transform the dictionary the dictionary a data frame
ph_df = pd.DataFrame.from_dict([pH_values]).T
    
# Change column name to pH
ph_df.columns = ['pH']

  

