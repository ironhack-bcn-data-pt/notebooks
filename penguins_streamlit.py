import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go



    # st.title()- to set the title
    # st.text() to write the description for the particular graph
    # st.markdown() to display text as markdown
    # st.latex() to display the mathematical expressions in the dashboard.
    # st.write() helps to display everything such as plotly graph, dataframe, functions, model, etc.
    # st.sidebar() is used for displaying data on the sidebar.
    # st.dataframe() to display the data frame
    # st.map() to display the map in just a single line code etc


st.title('Penguins')
st.markdown('Explore the penguins dataset')
st.sidebar.title('Visualization Selector')
st.sidebar.markdown('Select the Charts/Plots accordingly:')

@st.cache
def load_data():
    """ Utility function for loading the autompg dataset as a dataframe."""
    df = sns.load_dataset('penguins')

    return df

# load dataset
data = load_data()
numeric_columns = data.select_dtypes(['number']).columns

# checkbox widget
checkbox = st.sidebar.checkbox("Reveal data.")

if checkbox:
    # st.write(data)
    st.dataframe(data=data)

# create scatterplots
st.sidebar.subheader("Scatter plot setup")

# add select widget
select_x = st.sidebar.selectbox(label='X axis', options=numeric_columns)
select_y = st.sidebar.selectbox(label="Y axis", options=numeric_columns)

# add select widget
color = st.sidebar.radio(
     "Color by",
     data.select_dtypes(['object']).columns)

sns.relplot(data=data, x=select_x, y=select_y, hue=color)
st.pyplot(plt.gcf())

sns.catplot(data=data, x=color, y=select_x, kind='box')
st.pyplot(plt.gcf())
