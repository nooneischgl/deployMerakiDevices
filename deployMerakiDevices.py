# deployMerakiDevice.py is used to configured (or update) in mass a devices, Name, Tags, Address.

import pandas as pd
import meraki 
import argparse



# Assign users Args 
# Handel the Args 
parser = argparse.ArgumentParser(description="deployMerakiDevice.py takes a Excel or CSV file and Configures the devices Name, Address, Tags")
parser.add_argument("-ConfigFile", action="store", dest="configFile")
parser.add_argument("-NetworkName", action="store", dest="networkName")
parser.add_argument("-APIKey", action="store", dest="apiKey")
parser.add_argument("-OrgName", action="store", dest="orgName")

args = parser.parse_args()
 
inputFileName = args.configFile
claimNetworkName = args.networkName
apikey = args.apiKey
orgName = args.orgName

pdConfigFile = pd.read_excel(inputFileName)

orgID = None

dashboard = meraki.DashboardAPI(apikey) 
orgs = dashboard.organizations.getOrganizations()

# Get Org ID
if orgName:
    for org in orgs:
        if org["name"]== orgName:
            orgID = org["id"]
else:
    orgid = orgs[0]["id"]


networks = dashboard.organizations.getOrganizationNetworks(orgID)

# Claim Devices into Network (If configured)
if claimNetworkName != None:
    networkID = None

    # Get Networkd ID
    for net in networks:
        if net["name"] == claimNetworkName:
            networkID = net.id

    # Get Serial Numbers from Excel and Claim 
    for index, row in pdConfigFile.iterrows():
        sn = row['Serial Numbers']
        dashboard.networks.claimNetworkDevices(networkID, [sn])


# Update Device Name / Data
for index, row in pdConfigFile.iterrows():
    sn = row['Serial Numbers']
    name = row['Name']
    tags = row['Tags'].split()
    address = row['Address']
    dashboard.devices.updateDevice(sn,name = name, tags=tags, address= address)








