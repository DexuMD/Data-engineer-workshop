import sys
import pandas as py


print("Hello from pipeline.py")

month = int(sys.argv[1])

df = py.DataFrame({"day":[1,2], "burgers sold":[5,10]})
df['month'] = month

df.to_parquet(f"output_{month}.parquet")