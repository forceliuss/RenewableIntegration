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

#Calling the merged_df
renw = EnergyProduction('./Data/Raw/EnergyProduction.csv')
gdp = CountriesGDP('./Data/Raw/CountriesGDP.csv')

#Merging Renewable and GDP
merged_df = pd.merge(renw,gdp, how='inner')\
    .sort_values('year')


st.title(":bar_chart: Renewable Integration Dashboard")
st.markdown("###")

st.caption('Renewables include the primary energy equivalent of hydro (excluding pumped storage), geothermal, solar, wind, tide and wave sources. Energy derived from solid biofuels, biogasoline, biodiesels, other liquid biofuels, biogases and the renewable fraction of municipal waste are also included.\n This indicator is measured in thousand toe (tonne of oil equivalent) as well as in percentage of total primary energy supply.')

################# Section 1 - Metrics

sec_1 = st.container()
sec_1.subheader(cntry, divider='grey')
col1, col2 = sec_1.columns(2, gap='large')


################# Section 2 - Charts

sec_2 = st.container()
col3, col4 = sec_2.columns(2, gap='large')

#################  RESET STREAMLIT
hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

