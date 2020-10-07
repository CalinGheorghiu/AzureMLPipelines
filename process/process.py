import pandas as pd
from azureml.core import Run
import os
run = Run.get_context()
dataframe=run.input_datasets["input1"].to_pandas_dataframe()
def process_dataframe(df):
    df1=df.copy()
    df1["Hours_recorded"]=df1["Lektionslängd"]/60.0
    df1["Hours_Absent"]=df1["AntalMin_Frånvaro"]/60.0
    return df1
output=process_dataframe(dataframe)
output.to_csv("output1.csv")
os.makedirs("output1.csv",exist_ok=True)