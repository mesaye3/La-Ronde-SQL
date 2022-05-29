#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_csv("RIDE.csv")


# In[12]:


df.head()


# In[13]:


df.isnull().sum()


# In[18]:


df2= df.dropna()


# In[19]:


df2.isnull().sum()


# In[20]:


df2= df.drop(columns= "Unnamed: 6")


# In[21]:


df2.head()


# In[22]:


df2.dtypes


# In[23]:


df2.to_csv("ride_updated.csv", index= False)


# In[ ]:




