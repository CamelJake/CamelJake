import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = ''
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)



network_ids = [ ]


for network in network_ids:
    response = dashboard.networks.getNetworkAlertsSettings(
    network)
    print(response)
