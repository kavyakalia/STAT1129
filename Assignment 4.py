#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question 1

import numpy as np
import matplotlib.pyplot 
x=np.array

for row in integers:
    for column in row:
        print(column, end= ' ')
    print()


# In[7]:


integers*2


# In[8]:


integers.ndim


# In[9]:


integers.shape


# In[10]:


#Question 2 

import numpy as np
integers=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

for row in integers:
    for column in row:
        print(column, end= ' ')
    print()


# In[12]:


for i in integers.flat: 
    print(i, end=' ')


# In[13]:


#Question 3 

import numpy as np
xintegers=np.arange(1,7)
xintegers


# In[21]:


import numpy as np
yintegers=np.arange(5,11)
yintegers


# In[26]:


import matplotlib.pyplot as plt
import numpy as np

plt.plot(xintegers,yintegers)
plt.show 


# In[25]:


#Question 4 

import matplotlib.pyplot as plt
import numpy as np 

xpoints=np.array([3,6,9,12])
ypoints=np.array([2,8,1,10])

plt.plot(xpoints,ypoints,marker='o')
plt.show()


# In[33]:


#Question 5

import matplotlib.pyplot as plt
import numpy as np 

xpoints=np.array([0,1,2,3,4,5])
ypoints=np.array([2,4,6,14,10,12])

plt.plot(xpoints,ypoints,'D:r',ms=10,mfc='g',mec='g')
plt.show()

