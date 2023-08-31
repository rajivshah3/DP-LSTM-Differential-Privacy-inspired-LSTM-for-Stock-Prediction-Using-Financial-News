#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, json
import pandas as pd


# ##  Function as a generator to load all files in all sub-folders under the parent directory 

# In[2]:


def list_files(dirpath):
    for dirname, dirnames, filenames in os.walk(dirpath):
        for filename in filenames:
            yield os.path.join(dirname, filename)


# ## Load all .json files use json.loads(), basically each .json file only contains 1 line

# In[3]:


json_list = []
dirpath = 'us-financial-news-articles/'
for filePath in list_files(dirpath):
    if filePath.endswith('.json'):
        with open(filePath) as f:
            for line in f:
                data = json.loads(line)
                json_list.append([data['published'],
                                  data['thread']['site'],
                                  data['title'],
                                  data['text'],
                                  data['url']])


# ## Make sure the length of json list matches the total files

# In[4]:


len(json_list)


# ## Convert Json to DataFrame in order to perform data analysis

# In[5]:


col_names =  ['published_date','source_name','title','body','url']
df= pd.DataFrame(json_list,columns=col_names)


# In[8]:


df.shape


# In[9]:


df.head()


# ## Sort the data by date

# In[10]:


df = df.sort_values(by=['published_date'], ascending=True)


# In[11]:


df.head()


# In[12]:


df=df.reset_index(inplace=False)
del df['index']


# In[17]:


df.head()


# ## Export to .csv file

# In[47]:


#df.to_csv('us_financial_news_articles_2018.csv')
