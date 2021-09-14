#!/usr/bin/env python
# coding: utf-8

# In[1]:


FavoriteColors = ["black", "teal", "white"] #Q1
print(type(FavoriteColors))
print(FavoriteColors)


# In[2]:


nums=list(range(30,63,3)) #Q2
print(nums) 


# In[3]:


nums=("30","33", "36", "39", "42", "45", "48", "51", "54", "57", "60") #Q2
print(type(nums))
print(nums)


# In[4]:


x=[] #Q3
print(x)


# In[5]:


x.append('0') #Q3
x.append('1')
x.append('2')
x.append('3')
x.append('4')
x.append('5')
print(x)


# In[7]:


x.remove('2') #Q3
print(x)


# In[8]:


x.insert(2,2.0) #Q3
print(x)


# In[9]:


len(x) #Q3


# In[14]:


x=[0,1,2.0,3,4,5] #Q3
max(x)


# In[15]:


min(x) #Q3


# In[16]:


list1=[] #Q4
for item in range(1,11):
    list1.append(item)
list1


# In[17]:


sum(list1) #Q4

