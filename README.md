# URA-transactions-private-properties
This repo give insights about transactions statistics of non-landed private properties rental costs in Singapore (EC & Condos)

**Output file:**
1. Price Index by Singapore Districts & No. of Bedroom
2. Price Index by Project & No. of Bedroom

Eg.

| Bedroom         | 1                | 1                | 1                |2               | 2                | 2                | 
| --------------- | ---------------- | ---------------- | ---------------- |--------------- | ---------------- | ---------------- |
| rental_district | rental_rent_25th | rental_rent_50th | rental_rent_75th | rental_rent_25th | rental_rent_50th | rental_rent_75th |
| `D01 Boat Quay / Raffles Place / Marina` | 4300 | 4900 | 5500 | 5950 | 6850 | 8000 |
| `D02 Chinatown / Tanjong Pagar`          | 3800 | 4400 | 4800 | 4800 | 5500 | 6275 |
| `D03 Alexandra / Commonwealth`           | 3600 | 3900 | 4200 | 4800 | 5300 | 5800 |

**Steps:**
1. Source File is extracted from URA API call - https://www.ura.gov.sg/maps/api/#private-residential-properties-rental-contract (Please register for account and obtain API key)
2. For this API, data is refreshed on a quarterly basis by URA
3. Since it is a simple API, API call is made via Postman and JSON file is obtained
4. Python is used for converting JSON to CSV file and further performing data analysis such as caclulating percentile at districts, noofbedroom level

