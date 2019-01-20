import requests
import json

with open('responseSummary.json') as S:
	text_S = json.loads(S.read())

data_S = text_S['data']
all_device = []
device_S = []
for i in data_S:
	all_device.append(i['device'])
for  i in set(all_device):
	device_S.append(i)




for device in device_S:
	url = "https://ipacdev.hondaresearch.com:8443/hackathon/hondadsrc/rvbsm?device={}".format(device)

	headers = {
	    'key' : "AC85FK223FNP90AK72",
	    'cache-control' : "no-cache"
	}

	response = requests.request("GET", url, headers=headers)

	with open("response{}.json".format(device),'w') as r:
		json_obj = json.loads(response.text)
		r.write(json.dumps(json_obj, indent=4))




