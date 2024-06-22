import time
import streamlit as st

import pandas as pd
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

#Importing the cleaning file
from cleaning import *

################# STREAMLIT PAGE SETUP

st.set_page_config(
    page_title="Renewable Dashboard",
    page_icon=":infinity:",
    layout="wide",
    initial_sidebar_state="expanded"
)

#Sidebar config
st.sidebar.title('Select Country')


#################  RESET STREAMLIT
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

