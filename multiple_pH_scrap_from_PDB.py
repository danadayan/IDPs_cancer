#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:49:13 2024

@author: danadayan
"""
# %% Import packages and variables
import requests
from bs4 import BeautifulSoup
import os as os
from import_pdb_ids import pdb_ids
import pandas as pd

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
                pH_value = rows[2].find_all('td')[2].text.strip()
                return pH_value
            else:
                return "pH value not found"
        else:
            return "Table not found"
    else:
        return "Failed to retrieve the web page"

# %% Get pH values for wanted pdb
# pdb_ids = ['9F3Y', '9F4D', '9F4E']
pH_values = {}

for pdb_id in pdb_ids:
    pH_value = fetch_pH(pdb_id)
    pH_values[pdb_id] = pH_value

# Print the results
for pdb_id, pH_value in pH_values.items():
    print(f"PDB ID: {pdb_id}, pH Value: {pH_value}")
    
# %% Transform the dictionary the dictionary a data frame
    ph_df = pd.DataFrame.from_dict([pH_values]).T
    
# Change column name to pH
ph_df.columns = ['pH']
# %%
# Save temporary df
ph_df.to_csv("temporary_ph.csv")
