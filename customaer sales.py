import pandas as pd 

df=pd.read_csv("C:\\LEVEL-2 SEM-2\\data science\\EDA data\\customer_sales_500.csv")
print(df.head())

print(df.info())

print(df.isnull().sum())
print(df.duplicated().sum())

print(df.dtypes)
df['Date']=pd.to_datetime(df['Date'])

df.to_csv("C:\\LEVEL-3 SEM-1\\LEVEL-3 SEM-1\\Data Analysis Project\\New folder (2)\\Clean_customer_sales_data.csv", inplace=True)