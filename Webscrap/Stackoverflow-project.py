#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[10]:


url ='https://stackoverflow.com/questions/tagged/python?tab=Frequent'
link = requests.get(url).text


# In[12]:


soup = BeautifulSoup(link,'html')
print(soup.prettify())


# In[13]:


soup.title.string


# In[20]:


data = soup.find_all('div',id='questions') # Extracting questions,summary and tags

questions=[]
summary =[]
tag_cloud=[]
for i in data:
    qtn=i.findAll('h3')
    for qn in qtn:
        questions.append(qn.text) # Questions
        
    summ = i.find_all('div',class_='excerpt')
    for sum_data in summ:
        summary.append(sum_data.text) # Summary
        
    tag_data = i.find_all('div',class_='tags')
    for tag in tag_data:
        tags = tag.text
        tag_cloud.append(tags.split()) # Tags
        
# For getting No.of Answers
data = soup.find_all('div',class_='status')
no_answers =[]
for ans in data:
    answers=ans.findAll('strong')
    for ant in answers:
        no_answers.append(ant.text)

# for getting No.of Views
data = soup.find_all('div','views')
views =[]
for view in data:
    views.append(view.get('title'))


# Creating DataFrame

stack = pd.DataFrame()
stack['Questions'] = questions
stack['Summary'] = summary
stack['Tags'] = tag_cloud
stack['Views'] = views
stack['No.of Answers'] = no_answers

# Exporting Data to Excel file
stack.to_excel('stack_question.xlsx')

stack.head()


# In[ ]:




