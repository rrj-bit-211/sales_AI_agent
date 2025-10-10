import pandas as pd
import requests
import json

#df= pd.read_excel(r'D:/salesAI_project/sales-pipeline.xlsx')

# Save as CSV
#df.to_csv(r'D:/salesAI_project/sales_pipeline.csv', index=False)
df=pd.read_csv(r'D:/salesAI_project/salesReviews.csv')
print(df.columns)
df.columns=[col.strip().replace(" ","_").lower() for col in df.columns]
print(df.columns)
#import pdb;pdb.set_trace()
# df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
# df['close_date'] = pd.to_datetime(df['close_date'], errors='coerce')



# Drop or fix rows with invalid dates
# df = df.dropna(subset=['created_date', 'close_date'])

# df['created_date']= df['created_date'].dt.strftime('%Y-%m-%d')
# df['close_date']= df['close_date'].dt.strftime('%Y-%m-%d')


# replace NAN with none
#df=df.where(pd.notnull(df),None)

# url : https://cgqrulebmklnjoqsvunv.supabase.co
# API key : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNncXJ1bGVibWtsbmpvcXN2dW52Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4MzMyMTUsImV4cCI6MjA3NTQwOTIxNX0.LO-q4GAdrHA8EUfQZXCDRbdhdJS-uqXPJ2hCDxbHpn8

url="https://cgqrulebmklnjoqsvunv.supabase.co/rest/v1/sales_pipeline" 

headers={
    "apikey":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNncXJ1bGVibWtsbmpvcXN2dW52Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4MzMyMTUsImV4cCI6MjA3NTQwOTIxNX0.LO-q4GAdrHA8EUfQZXCDRbdhdJS-uqXPJ2hCDxbHpn8",
    "Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNncXJ1bGVibWtsbmpvcXN2dW52Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4MzMyMTUsImV4cCI6MjA3NTQwOTIxNX0.LO-q4GAdrHA8EUfQZXCDRbdhdJS-uqXPJ2hCDxbHpn8",
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
         