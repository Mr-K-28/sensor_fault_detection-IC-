from pymongo.mongo_client import MongoClient
import pandas as pd
import json
# uniform source identifer 
uri = "mongodb+srv://kapilmohan1005:Kapil2003@cluster0.u4gzcz5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)
#create database name and collection name 
DATABASE_NAME="ABHI_28"
COLLECTION_NAME="waferfoult"
# read data as dataframe 
df=pd.read_csv("C:\projects A-Z\sensor fault detection\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
#convert to jason
json_record=list(json.loads(df.T.to_json()).values())



#NOW DUMP DATA INTO DATABASE
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)