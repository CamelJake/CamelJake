#Updates Syslog Servers Across a Meraki Organization
#Created 8/15/2022 by NetOps

import pandas as pd
import requests

#Define Meraki API key. DO NOT STORE YOUR KEY IN THE SCRIPT
api_key = ''

#Import csv containing WAN org Network IDs.
data = pd.read_csv(r'C:\Users\jacob.bennett\OneDrive - The Shyft Group, Inc\Documents\Meraki API Scripting\ShyftGroupWANNetworkIDs_Meraki_West.csv')

#Load the Network IDs into a pandas dataframe
df = pd.DataFrame(data, columns=['id'])

#Convert the NetworkIDs from the dataframe into a list so we can iterate over it with a for loop.
network_ids = df['id'].values.tolist()

#Define List of Syslog servers. This will be filled in later once we get that info.
syslog_server = ''

#For each Network ID in the WAN org:
for network in network_ids:
        #Define API URL for network
        url = "https://api.meraki.com/api/v1/networks/{}/syslogServers".format(network)
        #Define the syslog server for each network
        payload = '''{
            "servers": [
                {
                    "host": "",
                    "port": 514,
                    "roles": [
                        "Flows",
                        "URLs",
                        "Security events",
                        "Appliance event log"
                    ]
                }
            ]
        }'''
        #Define HTTP headers
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": "{}".format(api_key)
        }
        #Send Put Request to Meraki API to make the change. Save the reponse to a variable.
        response = requests.request('PUT', url, headers=headers, data = payload)
        #Show response for the network. Should be "200 - OK"
        print(response.text.encode('utf8'))
