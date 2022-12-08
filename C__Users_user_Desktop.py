#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
df=pd.read_table(r'C:\Users\user\Downloads\customer.tsv', sep='\t')
print(df)


# In[3]:


df.iloc[1:,-1:]


# In[4]:


l=(df["Region"].to_string(header=False, index=False))
print(l)


# In[9]:


print(sorted(l.split()))




# In[10]:


for e in sorted(l.split()):
   print(e)


# In[ ]:




