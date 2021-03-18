import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
payload=response.json()
pprint(payload)
response = requests.get(
    'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
    headers={'X-Auth-Token': payload['Token']})
Dict = response.json()['response']
nameList = []
for i in range(len(Dict)):
	
	nameList.append([Dict[i]['family'],Dict[i]['hostname'],
                    Dict[i]['apManagerInterfaceIp'],Dict[i]['lastUpdated'],
                    Dict[i]['reachabilityStatus']])
pprint(nameList)

