from src.forest.configuration.mongo_db_connection import MongoDBClient
from src.forest.constant.database import DATABASE_NAME
from src.forest.exception import ForestException
from src.forest.logger import logging
import pandas as pd
import sys
import typing as Optional
import numpy as np 

class ForestData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """     
    def  __init__(self):
        try:
            self.mongo_client = MongoDBClient(db_name=DATABASE_NAME)
            logging.info("MongoDB client initialized successfully.") 
        except Exception as e:
              raise ForestException(e, sys) 
        
    def export_collection_as_dataframe(self, collection_name:str,db_name:Optional[str]=None) -> pd.DataFrame:
        """
        Export entire collection as dataframe:
        return pd.DataFrame of collection
        """
        try:
            if db_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client.client[db_name][collection_name]
            df = pd.DataFrame(list(collection.find())) 

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            logging.info(f"Collection '{collection_name}' exported as DataFrame successfully.")
            return df
        except Exception as e:
            raise ForestException(e, sys)  
    
    
