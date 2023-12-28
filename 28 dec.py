#!/usr/bin/env python
# coding: utf-8

# # dictionary methods
# 
# #clear(remove elements from dict)
# mydict={'id':34,'name':'abc','city':'pune','phone':9844328734}

# In[2]:


mydict


# In[5]:


mydict.clear()


# In[6]:


mydict


# In[7]:


#copy (returns copy of dict)
car={'brand':'ford','model':'mustang','year':1964}


# In[8]:


car


# In[9]:


car.copy()


# In[10]:


#fromkey(returns specific keys)
x={'key1','key2','key3'}


# In[11]:


x


# In[12]:


y=0
dict.fromkeys(x,y)


# In[13]:


#get(returns specified value)
car.get('model')


# In[14]:


car.get('year')


# In[15]:


#keys(returns list containing dict keys)
car.keys()


# In[18]:


#values(returns values)
car.values()


# In[21]:


#update(update dict with specific key value pairs)
car.update({'color':'black'})
car


# In[22]:


#pop(remove item from dict)
car.pop('year')
car


# In[ ]:




