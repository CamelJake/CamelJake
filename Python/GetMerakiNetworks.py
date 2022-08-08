#Gathers all meraki network metadata and exports it to a csv.
#Includes network ID, network name, etc. 
#Created by Jacob Bennett 5/19/2022

import requests
import pandas as pd
import json

#The organization ID(s) can be found by sending a GET request to https://api.meraki.com/api/v0/organizations/
organizationId = ""
payload = None
apiKey = ""

url = "https://api.meraki.com/api/v0/organizations/{}/networks".format(organizationId)

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "{}".format(apiKey)
}

response = requests.request('GET', url, headers=headers, data = payload)

#Convert the response text to JSON and export to csv using Pandas.
networkData=json.loads(response.text)
df=pd.DataFrame(networkData, columns=['id', 'organizationId', 'name', 'timeZone','tags', 'productTypes', 'type', 'disableMyMerakiCom', 'disableRemoteStatusPage'])
filepath = r'C:\Users\jacob.bennett\MerakiNetworkInfo.csv'
df.to_csv (filepath, index = False, header=True)
                
