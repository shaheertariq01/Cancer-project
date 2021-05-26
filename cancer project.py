#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[11]:


cancerm= pd.read_csv("cancer_m.csv", index_col='Id')
cancerm
cancerb= pd.read_csv("cancer_b.csv", index_col='Id')
cancerb


# In[12]:


sns.distplot(a=cancerm['Area (mean)'], kde=False)
sns.distplot(a=cancerb['Area (mean)'], kde=False)


# In[13]:


sns.kdeplot(data=cancerm['Radius (mean)'], shade=True)
sns.kdeplot(data=cancerb['Radius (mean)'], shade=True)


# In[ ]:




