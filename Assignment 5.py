#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Question 1 
import matplotlib.pyplot as plt
import numpy as np 
y1=np.array([1,2,3,4,5])
y2=np.array([5,6,7,8,9])
y3=np.array([9,10,11,12,13])


plt.plot(y1, linewidth='1')
plt.plot(y2, linewidth='1')
plt.plot(y3, linewidth='1')

plt.xlabel("X label")
plt.ylabel("Y label")

plt.show()


# In[15]:


#Question 2
import matplotlib.pyplot 
import numpy as np 

x=np.random.normal(0,0.2,800)

plt.hist(x)
plt.show()


# In[32]:


#Question 3 
mydic={"Apples":45, "Bananas": 25, "Cherries": 15, "Dates": 20}
fruitlist=[]
fruitlist.append('Apples')
fruitlist.append('Bananas') 
fruitlist.append('Cherries') 
fruitlist.append('Dates') 
print(fruitlist)

countlist=[]
countlist.append(45)
countlist.append(25)
countlist.append(15)
countlist.append(20)
print(countlist)

import matplotlib.pyplot as plt
import numpy as np

y=np.array([45,25,15,20])
mylabels=["Apples", "Bananas","Cherries", "Dates"] 

plt. pie(y, labels=mylabels)
plt.legend()
plt.show() 

x=np.array(["Apples", "Bananas","Cherries", "Dates"])
y=np.array([45,25,15,20])

plt.bar(x,y)
plt.show()


# In[85]:


#Question 4
import matplotlib.pyplot as plt
import numpy as np 


x=np.array([10,20,30,40,50,60,70,80,90,100])
y=np.array([88,92,80,89,90,80,60,88,80,84])
plt.scatter (x,y,color='red')

x=np.array([10,20,30,40,50,60,70,80,90,100])
y=np.array([75,59,69,48,65,56,32,45,20,30])
plt.scatter (x,y,color='green')

plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.title("Scatter Plot")
mylabels=["Math Marks", "Science Marks"]
plt.legend()


plt.show()


# In[80]:


#Question 5
import matplotlib.pyplot as plt
import numpy as np

x=np.array([15,25,22,20,18,65,33,34])
y=np.array([5,10,20,22,15,45,37,31])
plt.subplot(1,4,1)
plt.scatter(x,y)
plt.title("Scatter")

y1=np.array([3,9,1,10])
y2=np.array([6,4,2,7])
plt.subplot(1,4,2)
plt.plot(y1,y2)
plt.title("Multiple Line")

x=np.array(["A", "B", "C", "D"])
y=np.array([6,2,3,4])
plt.subplot(1,4,3)
plt.bar(x,y)
plt.title("Bar")

x=np.random.normal(2,1,3)
plt.subplot(1,4,4)
plt.hist(x)
plt.title("Histogram")

plt.show()

