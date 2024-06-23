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

#Calling the merged_df
renw = EnergyProduction('./Data/Raw/EnergyProduction.csv')
gdp = CountriesGDP('./Data/Raw/CountriesGDP.csv')

#Merging Renewable and GDP
merged_df = pd.merge(renw,gdp, how='inner')\
    .sort_values('year')

################# SIDEBAR

#Sidebar config
st.sidebar.title('Select Country')

#Selecting the continent
merged_df = merged_df.sort_values('cntry_region')

cntry_reg = st.sidebar.selectbox("Continent:",merged_df['cntry_region'].unique())

df_c = merged_df.query(
    'cntry_region == @cntry_reg'
) 
df_c = df_c.sort_values('cntry_name')

#Selecting the country
cntry = st.sidebar.selectbox("Country:",df_c['cntry_name'].unique())

df_selection = df_c.query(
    'cntry_name == @cntry'
)
df_selection = df_selection.sort_values('year')

#Time Range
time_range = st.sidebar.slider(
    'Time range:',
    1990, 2015, (1990, 2015)
)

df_selection = df_selection[(df_selection['year'] >= time_range[0])&(df_selection['year'] <= time_range[1])]
renw = renw[(renw['year'] >= time_range[0])&(renw['year'] <= time_range[1])]


st.title(":bar_chart: Renewable Integration Dashboard")
st.markdown("###")

st.caption('Renewables include the primary energy equivalent of hydro (excluding pumped storage), geothermal, solar, wind, tide and wave sources. Energy derived from solid biofuels, biogasoline, biodiesels, other liquid biofuels, biogases and the renewable fraction of municipal waste are also included.\n This indicator is measured in thousand toe (tonne of oil equivalent) as well as in percentage of total primary energy supply.')

################# Section 1 - Metrics

sec_1 = st.container()
sec_1.subheader(cntry, divider='grey')
col1, col2 = sec_1.columns(2, gap='large')

#KPIs
total_renw = df_selection['value'].sum()
average_renw = df_selection['value'].mean()
std_renw = df_selection['value'].std()
delta_renw = round(std_renw / average_renw,2)

#Converting scale of units
if total_renw >= 1000:
    total_renw = total_renw/1000


if average_renw >= 1000:
    average_renw = average_renw/1000

#Printing KPI

col1.metric(
    label="Average Production:",
    value=f'{round(average_renw,1)}',
    delta=delta_renw,
)

col2.metric(
    label="Total Production:",
    value=f'{round(total_renw,1)}',
)


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

