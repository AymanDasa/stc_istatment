import pandas as pd
import glob
from datetime import datetime
file_list =glob.glob('*.csv') 
error = 0
for filename in file_list:
    try:
        cal_name = ["Phone_Number","group_name","Description","FROM_DATE","TO_DATE","NUMBER_OF_UNIT","UNIT","VOLUME","discount","amount"]
        stc_csv = pd.read_csv(filename, encoding='cp1252' ,names= cal_name)
        stc_csv = stc_csv[stc_csv["Description"] == "Current_Bill_Amount"]
        stc_csv.drop(['group_name' , 'FROM_DATE' ,'Description','TO_DATE' ,'NUMBER_OF_UNIT','UNIT', 'VOLUME','discount'], axis=1 , inplace=True)
        stc_csv['Phone_Number']= stc_csv['Phone_Number'].astype(int)
        stc_csv = stc_csv.sort_values(by='Phone_Number',ascending=True)
        filename = filename.replace('.csv',datetime.today().strftime('_%Y_%m_%d'))
        stc_csv.to_csv( filename+'.csv',index=False)
    except:
        error = error +1
print(error , " Files cant convert")
