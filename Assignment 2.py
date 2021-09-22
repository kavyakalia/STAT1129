#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1: 
n=0
while n<10:
    print(n)
    if n==4:
        break  
    n+=1


# In[2]:


#Question 2: 
n=0
while n<5:
    print(n)
    n+=1
else:
    print(n,"is not less than 5")


# In[3]:


#Question 3:
favorite_fruits=['banana','orange','apple','melon']
for fruit in favorite_fruits:
    if fruit=='apple':
        break
    print('I like',fruit)
print('apple is really a fruit?')


# In[4]:


#Question 4: 
count=1
sum=1
while(count<30):
    count+=1
    sum=sum+count
print(sum)


# In[5]:


#Question 5:
dict={'Sunny':'play',
         'Rainy':'watch TV',
         'Cloudy':'walk'}

for key, value in dict.items():
    print (key,'',value)


# In[6]:


dict1={'Snowy':'ski'}
dict.update(dict1)
print(dict)


# In[34]:


#Question 6:
dict={"Sunny":"play",
         "Rainy":"watch TV",
         "Cloudy":"walk"}
for key, value in dict.items():
    if key == "Sunny":
       print("When sunny let us play")
    elif key == "Rainy":
       print("When rainy let us watch tv")
    elif key == "Cloudy":
       print("When cloudy let us walk")


# In[53]:


#Question 7:
grade=59.5


# In[55]:


if grade>=90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=70:
    print("C")
elif grade >=60:
    print("D")
else:
    print("F")    

