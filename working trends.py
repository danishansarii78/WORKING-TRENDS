#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[9]:


data=pd.read_csv(r"C:\Users\DELL\Downloads\python day 24 Your Career Aspirations of GenZ.csv")
data.head()


# In[10]:


data.columns


# In[11]:


country=data["Your Current Country."].value_counts()
label=country.index
counts=country.values
colors=['red','lightgreen']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text="Current Country")
fig.update_traces(hoverinfo='label+value',textinfo='percent',
                  textfont_size=30,
                  marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[17]:


question1=data['Which of the below factors influence the most about your career aspirations ?'].value_counts()
label=question1.index
counts=question1.values
colors=['gold','lightgreen']
fig= go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text='Factors influencing career aspirations')
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[18]:


question2=data['Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.'].value_counts()
label=question2.index
counts=question2.values
colors=['orange','black']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text='Will you persue education Outside India')
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[19]:


question3=data['How likely is that you will work for one employer for 3 years or more ?'].value_counts()
label=question3.index
counts=question3.values
colors=['aqua','red']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text='How likelyis the you will work for one employer for 3 years or more ?  ')
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[23]:


question7=data['What is the most preferred working environment for you.'].value_counts()
label=question7.index
counts=question7.values
colors=['blue','green']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text='Preferred working environment ')
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[ ]:




