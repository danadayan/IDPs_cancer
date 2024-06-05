#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - Read PDB ids from files
Created on Tue May 28 13:55:32 2024

@author: danadayan
"""
# %%
import os as os
import glob
os.chdir("/Users/danadayan/Documents/Maruvka Lab/MS.c Bioinformatics/Disordered_proteins/PDB/")


# %% Function that reads the pdb ids from the query
def read_pdb_ids(file_path):
    with open(file_path, 'r') as file:
        # Read the file content and split by commas
        pdb_ids = file.read().split(',')
        # Strip any leading/trailing whitespace characters from each PDB ID
        pdb_ids = [pdb_id.strip() for pdb_id in pdb_ids]
    return pdb_ids

# %% Load pdb ids
file_pattern = 'rcsb_pdb_ids_35c3281fc07e3fc9f7a3392ee9ece027_*.txt'
files = glob.glob(file_pattern)
all_pdb_ids_1_chain = []

# %% 
for file in files:
    all_pdb_ids_1_chain.extend(read_pdb_ids(file))

# Now we have all PDB with a single chain
