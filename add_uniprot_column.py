#!/usr/bin/env python
# coding: utf-8

# ## Dispherd input w/ specific regions 

# In[6]:


# Import packages
import pandas as pd
import gget


# In[21]:


# Load data frame
IDR_30 = pd.read_csv("borderline_IDRs_length_30_regions.csv")


# In[22]:


IDR_30


# In[29]:


IDR_30['UniProt_ID'] = IDR_30['ID'].apply(lambda ensembl_id: gget.info(ensembl_id)['uniprot_id'][0])


# In[30]:


IDR_30


# In[31]:


# Save it ASAP
IDR_30.to_csv("borderline_IDRs_length_30_regions_uniprot.csv")


# In[39]:





# In[ ]:




