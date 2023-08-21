# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:26:02 2023

@author: WeiJin.Ang
"""
import json
import requests
import pandas as pd
# Register an account with URA to obtain your access key 
# Send GET Request to retrieve daily Token
api_accesskey = 'Put your own access key'
api_url_base= 'https://www.ura.gov.sg/uraDataService/insertNewToken.action'

headers = {'Content-Type': 'application/json',
           'AccessKey': api_accesskey,
           'User-Agent': 'Mozilla/5.0'}

def get_token():

    response = requests.get(api_url_base, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    
token_info = get_token()

if token_info is not None:
    print("Here's your token: "+'\n'+token_info['Result'])    
else:
    print('[!] Request Failed')



# Determine previous month of current period based on Today's date to enter 'refPeriod' Parameter
today = pd.to_datetime('today')
previous_month = today - pd.DateOffset(months=1)
period = previous_month.to_period('D').strftime('%Yq%q')
refperiod = period[-4:]
print(refperiod)


#send GET Request to retrieve a list of median rentals of private non-landed residential properties based on refPeriod
api_url_base2= 'https://www.ura.gov.sg/uraDataService/invokeUraDS?service=PMI_Resi_Rental&'

headers2 = {'Content-Type': 'application/json',
           'AccessKey': api_accesskey,
           'Token': token_info['Result'],
           'User-Agent': 'Mozilla/5.0'}

params = {'refPeriod' : refperiod}

def get_data():

    response = requests.get(api_url_base2, params=params, headers=headers2)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    
data_info = get_data()

if data_info is not None:
    print("Success! json dataset to convert to csv is embedded in data_info['Result']")   
else:
    print('[!] Request Failed')


#flatten nested data in json file
from pandas.io.json import json_normalize
data = data_info['Result']
flattendata = json_normalize(data,'rental',['project','street','y','x'],errors='ignore')

# URA Publishes previous month's data; Determine previous month mmYY from period YYqq
previousMMYY = previous_month.to_period('D').strftime('%m%Y')
leaseDate = previousMMYY[0:2]+previousMMYY[-2:]
print(leaseDate)

#get data for the latest month only from a quarterly-period dataset
LatestMonthData = flattendata.loc[flattendata['leaseDate'] == leaseDate]
print(LatestMonthData)

#convert json data to .csv file, removing the index number
LatestMonthData.to_csv('flatten_data_' + leaseDate +'.csv', index=False)