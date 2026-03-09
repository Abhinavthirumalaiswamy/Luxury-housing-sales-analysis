# connect to sql
from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv("C:/Users/H T Abhinav/Downloads/Luxury_Housing_Bangalore (3).csv")
engine = create_engine("mysql+pymysql://root:12345@localhost:3306/luxury_housing_sales_analysis")
df.to_sql(name='luxury_housing_bangalore', con=engine, if_exists='append', index=False)