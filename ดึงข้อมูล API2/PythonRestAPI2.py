#!/usr/bin/env python
# coding: utf-8

# In[59]:


import requests


# In[67]:


url='https://opend.data.go.th/get-ckan/datastore_search?resource_id=9efa1066-e4ed-4515-b57a-b25daf83dc5c&limit=1000'

headers = {'api-key': 'kMbPrzSsWBS5Z98qEFZMnaVwJNTYytTi'}
response = requests.request('GET', url, headers=headers)


# In[69]:


print (response.text)


# In[ ]:




