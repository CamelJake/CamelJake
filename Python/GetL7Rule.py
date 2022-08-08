import requests

url = "https://api.meraki.com/api/v0/networks/{networkId}/l7FirewallRules"

payload = None

apiKey = ""

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": apiKey
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

