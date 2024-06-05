#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


# In[4]:


regions_df = pd.read_csv('borderline_IDRs_length_30_regions_uniprot.csv')


# In[6]:


regions_df


# In[8]:


sequences = {}


# In[14]:


with open('IDR_30.fasta') as fasta_file:
    for record in SeqIO.parse(fasta_file, 'fasta'):
        # Extract the UniProt ID from the description line
        uniprot_id = record.description.split('(')[-1].strip(')')
        sequences[uniprot_id] = str(record.seq)


# In[15]:


extracted_sequences = []


# In[18]:


for index, row in regions_df.iterrows():
    uniprot_id = row['UniProt_ID']
    start = row['sequence_start'] - 1  # Convert to 0-based index
    end = row['sequence_end']          # End position is inclusive in Python slicing
    
    if uniprot_id in sequences:
        full_sequence = sequences[uniprot_id]
        extracted_sequence = full_sequence[start:end]
        
        # Create a SeqRecord for the extracted sequence
        record = SeqRecord(
            Seq(extracted_sequence),
            id=uniprot_id,
            description=f'{uniprot_id} region {start+1}-{end}'
        )
        extracted_sequences.append(record)
    else:
        print(f"UniProt ID {uniprot_id} not found in FASTA file")

# Write the extracted sequences to a new FASTA file
with open('extracted_sequences.fasta', 'w') as output_file:
    SeqIO.write(extracted_sequences, output_file, 'fasta')

print('Extracted sequences written to extracted_sequences.fasta')


# In[20]:


# Read the CSV file
regions_df = pd.read_csv('borderline_IDRs_length_30_regions_uniprot.csv')

# Create a dictionary to store sequences by UniProt ID and descriptions
sequences = {}

# Parse the FASTA file and store the sequences and descriptions in the dictionary
with open('IDR_30.fasta') as fasta_file:
    for record in SeqIO.parse(fasta_file, 'fasta'):
        # Extract the UniProt ID from the description line
        uniprot_id = record.description.split('(')[-1].strip(')')
        sequences[uniprot_id] = (str(record.seq), record.description)

# List to store the extracted sequence records
extracted_sequences = []

# Extract the sequences based on the start and end positions
for index, row in regions_df.iterrows():
    uniprot_id = row['UniProt_ID']
    start = row['sequence_start'] - 1  # Convert to 0-based index
    end = row['sequence_end']          # End position is inclusive in Python slicing
    
    if uniprot_id in sequences:
        full_sequence, description = sequences[uniprot_id]
        extracted_sequence = full_sequence[start:end]
        
        # Create a SeqRecord for the extracted sequence
        record = SeqRecord(
            Seq(extracted_sequence),
            id=uniprot_id,
            description=description
        )
        extracted_sequences.append(record)
    else:
        print(f"UniProt ID {uniprot_id} not found in FASTA file")

# Write the extracted sequences to a new FASTA file
with open('extracted_sequences.fasta', 'w') as output_file:
    for record in extracted_sequences:
        output_file.write(f">{record.description}\n")
        output_file.write(f"{str(record.seq)}\n")

print('Extracted sequences written to extracted_sequences.fasta')


# In[ ]:




