#!/usr/bin/env python
# coding: utf-8

# In[58]:


#QUESTION 1

def Frequencies(numbers_dict):
     
    frequency = {}
    for items in numbers_dict:
        frequency[items] = numbers_dict.count(items)
     
    for k, v in frequency.items():
        print (k,":", v) 
        
if __name__ == "__main__":
    numbers_dict =[2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
    Frequencies(numbers_dict)


# In[73]:


import matplotlib.pyplot as plt
import numpy as np

x=np.array(['0','1','2','3','4','5','6','7','8','9','10'])
y=np.array([2,3,4,5,5,2,6,4,3,5,3])
plt.barh(x,y, color="green")
plt.show()


# In[74]:


import json

numbersdictionary={
    2 : 4,
    4 : 5,
    6 : 6,
    8 : 3,
    5 : 2,
    1 : 3,
    9 : 5,
    0 : 2,
    7 : 4,
    3 : 5,
    10 : 3,   
}

with open ("numbers.json", "w") as outfile:
    json.dump(numbersdictionary,outfile)


# In[1]:


#QUESTION 2 

import pandas as pd

df=pd.read_csv('amazon_orders.csv')
df.head()


# In[2]:


df.shape


# In[3]:


df=df.fillna(0)
df.head()


# In[4]:


df["Item Total"]=df["Item Total"].str.replace("$", "").astype(float)
df.head()


# In[5]:


df["Item Total"].sum() #total spent 


# In[6]:


df["Item Total"].mean() #average spent on an item 


# In[7]:


df["Item Total"].median() #median is a lot lower than mean


# In[8]:


df["Item Total"].max() #maximum spent on an order


# In[9]:


df["Item Total"].min() #minimum spent on an order


# In[10]:


df["Item Subtotal Tax"]=df["Item Subtotal Tax"].str.replace('$','').astype(float)
df.head()


# In[11]:


df["Item Subtotal Tax"].sum() #total spent on tax


# In[12]:


df["Item Subtotal Tax"].sum()/df["Item Total"].sum() #4.9% sales tax rate


# In[13]:


df['Order Date'] =pd.to_datetime(df['Order Date'])
df.head()


# In[16]:


import matplotlib.pyplot as plt #bar chart of all orders
import numpy as np

df.plot.bar(x='Order Date', y='Item Total', rot=90, figsize=(20,10))


# In[18]:


daily_orders=df.groupby('Order Date').sum()['Item Total']
daily_orders.head()


# In[21]:


import matplotlib.pyplot as plt #bar char of all orders (grouped by day)
daily_orders.plot.bar(figsize=(15,10)) 

