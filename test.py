import json


with open('verses.json') as f:
    data = json.load(f)

for item in data:
	

	temp = (item['meaning']).encode('UTF8')
	print(type(temp))
