# 18. Use House_Price prediction dataset. Provide summary statistics (mean, median, minimum, maximum, standard deviation) 
# of variables (categorical vs quantitative) such as- For example, if categorical variable is age groups and quantitative variable 
# is income, then provide summary statistics of income grouped by the age groups.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv("House Data.csv")
print(df)

cols=df.select_dtypes(include="object").columns.to_list()
print(cols)

df["NetSquareMeters"]=pd.to_numeric(df["NetSquareMeters"].str.replace(r"[^0-9]","",regex=True),errors="coerce")
df["NetSquareMeters"]=df["NetSquareMeters"]/10
df["NetSquareMeters"]=df["NetSquareMeters"].astype(int)
print(df["NetSquareMeters"])

df["NumberOfRooms"]=pd.to_numeric(df["NumberOfRooms"].str.replace(r"[^0-9]","",regex=True),errors="coerce")
print(df["NumberOfRooms"])


df1=df.groupby("Category")["NumberOfRooms"].agg(["mean","max","min","std","count"])
print(df1)

df2=df.groupby("district")["NetSquareMeters"].agg(["mean","max","min","std","count"])
print(df2)

df3=df.groupby("NumberOfRooms")["NetSquareMeters"].agg(["mean","median","max","min","count"])
print(df3)
