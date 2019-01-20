import json



# with open('response2004.json') as R:
# 	text = json.loads(R.read())

new_Truck = []
data = text['data']
# print(data)
for i in data:
	if i["basicVehClass"] == 20 or i["basicVehClass"] == 25:
		new_Truck.append(i)
# print(new_Truck)


with open('responseSummary.json') as S:
	text_S = json.loads(S.read())

data_S = text_S['data']
all_device = []
for i in data_S:
	all_device.append(i['device'])


# print(len(set(all_device)))




