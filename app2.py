#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st


# In[4]:


import pandas as pd


# In[9]:


import streamlit as st
import numpy as np
import pandas as pd
image = Image.open('airbnb.jpg')

st.image(image, caption='Airbnb Recommendation',use_column_width=True)
add_selectbox = st.sidebar.radio(
    "Select the SEARCH METHOD",
    ("Content Based Recommendation")
)

st.markdown('<style>body{background-color: #f2fffe;}</style>',unsafe_allow_html=True)
if add_selectbox == 'Content Based Recommendation' :
 st.title("Images using Content Based Recommendation")
 st.write("-------------------------------------------------------------------------------------------------")
 def get_data():
    return pd.read_csv(r"C:\Users\Dona\Downloads\airbnbBOS\recommend_output.csv")
 n=1
 df = get_data()
 images = df['0'].unique()

 st.subheader("Choose an image from the below list : ")
 pic = st.selectbox('Choices : ', images)
 st.subheader("**_IMAGE_** selected by the **_USER!_**")
 st.image(pic,width=None)

 st.subheader('How Many Images do you want to see?')
 z = st.radio(
    'Select the Number',
    (1,2,3,4,5,6,7,8,9,10))
 st.subheader("SIMILAR IMAGES OF THE **_SELECTED IMAGE :_**")
 for index, row in df.iterrows():
     if row['0']==pic:
        while n < z+1:
            st.image(row[n], use_column_width=None, caption=row[n])
            n+=1
                       





