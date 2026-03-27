import pandas as pd

def extract_airbnb_data() -> pd.DataFrame:
    df = pd.read_csv("/Users/zeynep/Desktop/python-sql-practice/data/raw/AB_NYC_2019.csv")
    return df