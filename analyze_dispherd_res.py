#!/usr/bin/env python
# coding: utf-8

# ## Analyze Dispherd results

# In[15]:


# Import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[7]:


# Load Dispherd results
res = pd.read_csv("/Users/danadayan/Documents/Maruvka Lab/MS.c Bioinformatics/Disordered_proteins/Dispherd/DispHScan_results/DispHScan_results.csv", index_col=0)


# In[9]:


res


# In[10]:


res['delta'] = res['Maximum DispH'] - res['Minimum DispH']


# In[12]:


res


# In[19]:


# Plot the distribution of 'delta' using Seaborn
sns.histplot(res['delta'], kde=True, bins=20)
plt.xlabel('Delta')
plt.ylabel('Frequency')
plt.title('Distribution of Delta')
plt.show()


# In[20]:


res.describe()


# In[ ]:




