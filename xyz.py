import pandas as pd
col_lst=["emp_id","name","company","location","salary","dept_id"]
vals=pd.read_csv("emp_hive.csv",usecols=col_lst)
print(vals["name"].head(5))
print(vals["salary"].max())
