#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Question 0 
marks={'Andy':88, 'Amy':66, 'James':90,'Jules':55,'Arthur':77}

#Question 1
for k,v in marks.items():
    print('k=',k,',v=',v)


# In[11]:


#Question 2
marks=[88,66,90,55,77] 
print(sum(marks)/len(marks))
print(max(marks))
print(min(marks))


# In[10]:


#Question 3 
marks={'Andy':88, 'Amy':66, 'James':90,'Jules':55,'Arthur':77}
for keys in marks.keys():
    if 'J' in keys:
        break
    print(keys)
    


# In[9]:


#Question 4
marks={'Andy':88, 'Amy':66, 'James':90,'Jules':55,'Arthur':77}
for keys in marks.keys():
    if 'J' in keys:
        continue
    print(keys)


# In[8]:


#Question 5
student_name='Teddy'

marks={'Andy':88, 'Amy':66, 'James':90,'Jules':55,'Arthur':77}
for student in marks: 
    if student==student_name:
        print(marks[student])
else: 
    print("Cannot find the student's name")
    


# In[23]:


#Question 6 
def less_than(num):
    num=0
    while num<8:
        print(num)
        num=num+1
    else:
        print("greater than 8", pow)
        
less_than(8)


# In[4]:


#Question 7 
def sum_function(num):
    n=1
    sum=0
    while n<=num:
        sum=sum+n
        n=n+1
    print(sum)
sum_function(8)


# In[5]:


#Question 8
def sumfunction(n):
    num=0
    for i in range(1, n+1):
        num=num+i       
    return num

n=8
sumfunction(n)


# In[6]:


#Question 9
def minimal(v1,v2,v3,v4):
    min_v=v1
    if v2<min_v:
        min_v=v2
    if v3<min_v:
        min_v=v3
    if v4<min_v:
        min_v=v4
    return min_v


# In[7]:


minimal(23,13,3,98)

