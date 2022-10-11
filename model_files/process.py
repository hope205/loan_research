# Import libraries
import pandas as pd
import numpy as np
from category_encoders import *
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer as imputer

SEED = 123



def work(data):
    #feature engineering of the dates    	
    
    

    data['approveddate'] = pd.to_datetime(data['approveddate'],errors='coerce')
    data['birthdate'] = pd.to_datetime(data['birthdate'],errors='coerce')
    data['creationdate'] = pd.to_datetime(data['creationdate'],errors='coerce')




    # Extract date features
    def extract_date_info(df,cols, g= 0):
        for feat in cols:
            df[feat +'_year'] = df[feat].dt.year        
            df[feat +'_day'] = df[feat].dt.day
            df[feat +'_month'] = df[feat].dt.month
            df[feat +'_quarter'] = df[feat].dt.quarter  
            df[feat +'_weekday'] = df[feat].dt.weekday
            if g == 0:
                df[feat +'_hour'] = df[feat].dt.hour
                df[feat +'_minute'] = df[feat].dt.minute
                df[feat +'_second'] = df[feat].dt.second
            
            
            # df[feat +'_hour'] = 2
            # df[feat +'_minute'] = 20
            # df[feat +'_second'] = 10
            
            
    extract_date_info(data,['approveddate'],g = 0)
    extract_date_info(data,['birthdate'],g = 1)
    extract_date_info(data,['creationdate'],g = 0)


    data = data.drop(['approveddate','birthdate', 'creationdate'],1)
            # data = data.drop(['birthdate_hour','birthdate_minute', 'birthdate_second'],1)
            
    print('this is data: ',data)
            
            
    return data
           


def predict(config,model):
    
    df = pd.DataFrame([config])
    
    print('this is df: ',df)
        
    preproc_df =work(df)
    
    print(preproc_df)

    y_pred = model.predict(preproc_df)
        
    return y_pred
    
    




