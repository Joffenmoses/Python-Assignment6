#!/usr/bin/env python
# coding: utf-8

# In[2]:


list1=[1,2,3,4,5,6,7,8]
list2=['a','b','c','d','e']
dict1={}
len1=min(len(list1),len(list2))

print({list1[each]:list2[each] for each in range(len1)})

