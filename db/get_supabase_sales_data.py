import pandas as pd
import requests
import json


df=pd.read_csv(r'D:/salesAI_project/salesReviews.csv')
print(df.columns)
df.columns=[col.strip().replace(" ","_").lower() for col in df.columns]
print(df.columns)

url="https://cgqrulebmklnjoqsvunv.supabase.co/rest/v1/sales_pipeline" 

headers={
    "apikey":"api_key",
    "Authorization":"api_key",
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
         
