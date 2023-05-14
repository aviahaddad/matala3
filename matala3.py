#!/usr/bin/env python
# coding: utf-8

# In[25]:


import requests
import pandas as pd


# In[26]:


with open('C:/Users/אביה חדאד/Desktop/תואר ראשון/שנה ג/כרייה וניתוח נתונים מתקדם פייתון/מטלות/מטלה 3/dests.txt', 'r') as f:
    destinations = f.read().splitlines()


# In[27]:


origin = 'Tel Aviv'


# In[28]:


df = pd.DataFrame(columns=['Target', 'Distance_km', 'Duration', 'Longitude', 'Latitude'])


# In[29]:


for destination in destinations:
    try:

        url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key=AIzaSyCe7Fuy0zJAPPFdULMcFETRqF7Wkwl7uYI'
        response = requests.get(url)
        data = response.json()
        distance_km = data['rows'][0]['elements'][0]['distance']['value'] / 1000
        duration = data['rows'][0]['elements'][0]['duration']['text']
        
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={destination}&key=AIzaSyCe7Fuy0zJAPPFdULMcFETRqF7Wkwl7uYI'
        response = requests.get(url)
        data = response.json()
        longitude = data['results'][0]['geometry']['location']['lng']
        latitude = data['results'][0]['geometry']['location']['lat']
        
        df = df.append({'Target': destination, 'Distance_km': distance_km, 'Duration': duration, 'Longitude': longitude, 'Latitude': latitude}, ignore_index=True)
    except:
        print(f'Error retrieving information for {destination}')


# In[30]:


print(df)


# In[31]:


### The 3 cities furthest from Tel Aviv - 
df.sort_values('Distance_km', ascending=False).head(3)['Target']

