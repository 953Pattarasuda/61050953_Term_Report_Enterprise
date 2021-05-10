#!/usr/bin/env python
# coding: utf-8

# In[59]:


import requests


# In[71]:


url='https://opend.data.go.th/opend-search/vir_6742_1598057614/query?dsname=vir_6742_1598057614&path=vir_6742_1598057614&path=vir_6742_1598057614&loadAll=1&type=json&limit=100&offset=0'

headers = {'api-key': 'kMbPrzSsWBS5Z98qEFZMnaVwJNTYytTi'}
response = requests.request('GET', url, headers=headers)


# In[72]:


print (response.text)


# In[ ]:




