#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:41:35 2024

@author: danadayan
"""

import pandas as pd
import gget

# Load the DataFrame
IDR_30 = pd.read_csv("borderline_IDRs_length_30.csv")

# Collect unique gene IDs and their corresponding indices in IDR_30
unique_gene_ids = IDR_30['ID'].unique()

# Write to output file
with open('output.fasta', 'w') as f:
    for ID in unique_gene_ids:
        try:
            # Fetch information for each gene ID
            info = gget.info(ID)
            protein_name = info['protein_names'].values[0]
            uniprot_id = info['uniprot_id'].values[0]
            seq = gget.seq(ID, translate=True)[1]

            # Write to output file in FASTA format
            gene = ">" + protein_name + " (" + uniprot_id + ")" + "\n" + seq
            f.write(gene + '\n')
        except Exception as e:
            print(f"Failed to process gene ID {ID}: {e}")
