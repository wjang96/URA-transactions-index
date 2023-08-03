# URA-transactions-private-properties
This repo give insights about transactions statistics of non-landed private properties rental costs in Singapore (EC & Condos)
**Output file:**
1. Price Index by Singapore Districts & No. of Bedroom
2. Price Index by Project & No. of Bedroom

**Steps:**
1. Source File is extracted from URA API call - https://www.ura.gov.sg/maps/api/#private-residential-properties-rental-contract (Please register for account and obtain API key)
2. For this API, data is refreshed on a quarterly basis by URA
3. Since it is a simple API, API call is made via Postman and JSON file is obtained
4. Python is used for converting JSON to CSV file and further performing data analysis such as caclulating percentile at districts, noofbedroom level

