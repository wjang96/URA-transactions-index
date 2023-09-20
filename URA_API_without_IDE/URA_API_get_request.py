# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:26:02 2023

@author: WeiJin.Ang
"""
import json
import requests
import pandas as pd
import csv
import json

# Enter the YearQuarter you wish to extract the data from the API call
refperiod = '23q3'

# Register an account with URA to obtain your access key 
# Send GET Request to retrieve daily Token
api_accesskey = 'Put your own API call'
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

#convert json data to .csv file, removing the index number
flattendata.to_csv('transaction_resi_converted_raw_csv_' + refperiod + '.csv', index=False)