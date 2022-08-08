#Add a L7 rule to one or many Meraki firewalls.
#Created by Jacob Bennett 5/19/2022

import requests

API_KEY = ''

network_id = ['']

#Apply the rule to each network listed in the network_id list.
#The "rules" list will need to be edited. The current value of rules just shows all the different L7 rule types you can do.

for networks in network_id:
    url = "https://api.meraki.com/api/v0/networks/{}/l7FirewallRules".format(network_id[network])

    payload = '''{
        "rules": [
            {
                "policy": "deny",
                "type": "application",
                "value": {
                    "id": "meraki:layer7/application/67",
                    "name": "Xbox LIVE"
                }
            },
            {
                "policy": "deny",
                "type": "applicationCategory",
                "value": {
                    "id": "meraki:layer7/category/2",
                    "name": "Blogging"
                }
            },
            {
                "policy": "deny",
                "type": "host",
                "value": "google.com"
            },
            {
                "policy": "deny",
                "type": "port",
                "value": "23"
            },
            {
                "policy": "deny",
                "type": "ipRange",
                "value": "10.11.12.00/24"
            },
            {
                "policy": "deny",
                "type": "ipRange",
                "value": "10.11.12.00/24:5555"
            },
            {
                "policy": "deny",
                "type": "blacklistedCountries",
                "value": [ "AX", "CA" ]
            },
            {
                "policy": "deny",
                "type": "whitelistedCountries",
                "value": [ "US" ]
            }
        ]
    }'''

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": API_KEY
    }

    response = requests.request('PUT', url, headers=headers, data = payload)
    print(response.text.encode('utf8'))


