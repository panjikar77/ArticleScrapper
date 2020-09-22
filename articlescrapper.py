#!/usr/bin/env python
# coding: utf-8

# In[35]:


import newspaper
import numpy as np


# In[29]:


numberOfArticles = 10


# In[30]:


guardianNews = newspaper.build('https://www.theguardian.com/au')


# In[31]:


for article in guardianNews.articles:
    print(article.url)
    


# In[44]:


from newspaper import Article


# In[41]:


url = 'https://www.theguardian.com/science/2020/sep/22/scientists-disagree-over-targeted-versus-nationwide-measures-to-tackle-covid'


# In[42]:


url


# In[45]:


article = Article(url)


# In[46]:


article.download()


# In[47]:


article.html


# In[48]:


article.parse()


# In[57]:


authors = article.authors


# In[58]:


date = article.publish_date


# In[59]:


text = article.text


# In[54]:


article.nlp()


# In[60]:


keywords  = article.keywords


# In[61]:


summary = article.summary


# In[62]:


keywords


# In[63]:


articleData = [authors, date, text, keywords, summary]


# In[64]:


articleData


# In[65]:


import csv


# In[ ]:




