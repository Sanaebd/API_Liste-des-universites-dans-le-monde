#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pyodbc 
import sys
import requests
import json
import pandas


# In[91]:


r1=requests.get("http://universities.hipolabs.com/search?name=University")


# In[92]:


print(r1)


# In[93]:


dat=r1.json()


# In[94]:


dat


# In[95]:


len(dat)


# In[96]:


dat[0].keys()


# In[97]:


import pandas as pd
dataf= pd.DataFrame(data=dat,columns=['alpha_two_code', 'web_pages', 'country', 'state-province', 'name', 'domains'])


# In[98]:


dataf['domains']


# In[99]:


def inser():   
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-LAFG171K;'
                      'Database=UNIV;'
                      'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
    #ref=(alpha_two_code,web_pages,country,name,domains)
    for index,row in dataf.iterrows():
        a=dataf['alpha_two_code'][index]
        w=dataf['web_pages'][index]
        c=dataf['country'][index]
        s=dataf['state-province'][index]
        n=dataf['name'][index]
        d=dataf['domains'][index]
        cursor.execute("INSERT INTO dbo.tab4 VALUES (?,?,?,?,?,?)",str(a),str(w),str(c),str(s),str(n),str(d))
    
    cursor.commit()
    cursor.close()


# In[100]:


inser()


# In[ ]:




