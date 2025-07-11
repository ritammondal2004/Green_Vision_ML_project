import sys
from src.forest.exception import ForestException

import pymongo
from dotenv import load_dotenv
from urllib.parse import quote_plus 
import os 
from src.forest.constant.database import DATABASE_NAME
import certifi

load_dotenv()
              
ca = certifi.where()
        
class MongoDBClient:

    client = None 

    def __init__(self, db_name = DATABASE_NAME) -> None:
        try:                       
            if MongoDBClient.client is None:
                               
                # Get credentials from environment variables
                username = os.getenv("MONGO_DB_USERNAME")
                password = quote_plus(os.getenv("MONGO_DB_PASSWORD"))
                               
                uri = f"mongodb+srv://{username}:{password}@cluster0.j6bmnim.mongodb.net/?retryWrites=true&w=majority"
                if uri is None:
                    raise Exception("MongoDB URI is not set in environment variables.")
                MongoDBClient.client = pymongo.MongoClient(uri, tlsCAFile=ca)  

            self.client = MongoDBClient.client
            self.database = self.client[db_name] 
            self.db_name = db_name
        except Exception as e:
            raise ForestException(e, sys)