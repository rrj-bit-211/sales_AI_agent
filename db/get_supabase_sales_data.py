import pandas as pd
import requests
import json
import os 
from dotenv import load_dotenv

# Load envrionment variables from .env files

load_dotenv()

df=pd.read_csv(r'D:/salesAI_project/salesReviews.csv')
print(df.columns)
df.columns=[col.strip().replace(" ","_").lower() for col in df.columns]
print(df.columns)


#access the variables

url=os.getenv("SUPABASE_URL")
api_key=os.getenv("SUPABASE_KEY")
authorization=os.getenv("SUPABASE_KEY")



headers={
    "apikey":api_key,
    "Authorization":authorization,
    "Content-Type":"application/json"
}

batch_size=100

for i in range(0,len(df),batch_size):
    batch=df.iloc[i:i+batch_size]
    records=batch.to_dict(orient='records')

    try:
        response=requests.post(url,json=records,headers=headers)
        print(f"Batch {i//batch_size + 1}:{response.status_code}")
        if response.status_code!=201:
            print("Error response:",response.text)
    except TypeError as e:
        print("Exception during batch insert:",e) 

         