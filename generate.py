from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile
fname = get_tmpfile("my_doc2vec_model")
model = Doc2Vec.load(fname)
#vector = model.infer_vector(["system", "response"])
import json
import csv

with open('verses.json') as f:
    data = json.load(f)

list1 = []
list2 = []
num_features = 5

for item in data:
	
	temp = (item['meaning']).encode('UTF8')
	arr = temp.split()
	rep = model.infer_vector(arr)
	list1.append(rep)
	list2.append(temp)

i=0
with open('result.csv','w+') as file:
	wr = csv.writer(file)
	for item in list1:
		arr = []
		for temp in item:
			arr.append(str(temp))

		arr.append(list2[i])
		wr.writerow(arr)
		i += 1


