import pandas as pd

def load_data(path):
    return pd.read_csv("/home/the-g/Desktop/maternal-mortality-ethiopia/data/raw/Maternal_mortality_national_eth.csv",sep='\t')

def filter_indicator(df, indicator_name):
    return df[df["Indicator"] == indicator_name]

def basic_clean(df):
    df = df[["SurveyYear", "Value"]].dropna()
    return df.sort_values("SurveyYear")