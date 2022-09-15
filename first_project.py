#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
data=pd.read_csv(r"C:\Users\JMS\Downloads\Marriage_Divorce_DB.csv")


# In[5]:


data.head(2)


# In[6]:


data.shape


# In[7]:


data.index


# In[9]:


data.dtypes


# In[10]:


data["Education"].unique()


# In[12]:


data.nunique()


# In[14]:


data.count()


# In[15]:


data["Education"].value_counts()


# In[16]:


data.info()


# In[17]:


data.nunique()


# In[18]:


data["Good Income"].nunique()


# In[21]:


data["Good Income"].unique()


# In[22]:


data.head(2)


# In[25]:


data["Religion Compatibility"].value_counts() 


# In[34]:


data[data["Religion Compatibility"] > 99]


# In[40]:


data.groupby("Religion Compatibility").get_group("clear")


# In[47]:


data.isnull().sum()


# In[ ]:





# In[46]:


data.notnull().sum()


# In[49]:


data.rename(columns={"Education":"pravin"})


# In[51]:


data["Cultural Similarities"].mean()


# In[52]:


data["Cultural Similarities"].std()


# In[57]:


data[data["Cultural Similarities"]>90]


# In[63]:


data.groupby("Education").min()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




