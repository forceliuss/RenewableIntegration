# RenewableIntegration

This is an experimental project!! The main objective of this project is to create a dashboard to analyze the data from several sources and develop a common place for these insights.

![image](https://github.com/forceliuss/renewable_integration/assets/72661072/69a730f8-d56c-43ae-84e6-6d45ec5d27dc)

## Datasets

- Renewable Energy (1960 - 2023) - main source (https://www.oecd-ilibrary.org/energy/renewable-energy/indicator/english_aac7c3f1-en)
  <a href='https://www.kaggle.com/datasets/imtkaggleteam/renewable-energy-1960-2023' target='_blank'>Kaggle dataset</a>

- World GDP by Country (1960 - 2022)
  <a href='https://www.kaggle.com/datasets/sazidthe1/world-gdp-data' target='_blank'>Kaggle dataset</a>

## Code focus objectives

- Import and clear the data from the datasets
- Combine all the different sources into a main dataframe
- Analyze the dataframe and create metrics
- Create a local dashboard (StreamLit)
- Sort the global datasets by countries

## Libraries

- Pandas
- StreamLit
- Seaborn
- MathplotLib

## How to run

1. Clone this project
   ```git clone https://github.com/forceliuss/RenewableIntegration.git```
3. Run your python kernel
4. Install all the libraries above
   ```pip install -r requirements.txt```
6. Run `app.py` through the streamlit command
   ```streamlit run app.py```
