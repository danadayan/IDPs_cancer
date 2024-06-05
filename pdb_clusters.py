#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:30:37 2024

@author: danadayan
"""
# %% Load packages
import os as os
import pandas as pd


# %% Set directory
os.chdir("/Users/danadayan/Documents/Maruvka Lab/MS.c Bioinformatics/Disordered_proteins/PDB/")

# %% Load 100% identity file
identity = pd.read_csv("clusters-by-entity-100.txt", header = None)

# Name the new column as cluster
identity.columns = ['cluster']

# %% Remove _num from clusters
def remove_num(text):
    return ' '.join([part.split('_')[0] for part in text.split()])

# %% Apply the function to the df
identity['cluster'] = identity['cluster'].apply(remove_num)
    

# %% Convert data frame to dictionary
clusters_dict = {f'cluster_{i+1}': row['cluster'].split() for i, row in identity.iterrows()}
