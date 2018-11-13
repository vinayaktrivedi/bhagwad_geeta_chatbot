import csv 
import json
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile
import numpy as np 

fname = get_tmpfile("my_doc2vec_model")
num_features = 5

model = Doc2Vec.load(fname)
query = raw_input("Enter your query\n")
q_features = model.infer_vector(query.split())

shloka = ''
dist_array = {}
with open('result.csv','r') as file:
	fd = csv.reader(file)

	for item in fd:
		temp = []
		for i in range(num_features):
			temp.append( float(item[i]) )

		dist = np.linalg.norm(q_features - temp)
		dist_array[item[-1]] = dist

final = sorted(dist_array, key=dist_array.__getitem__)

num_shlokas = 5
print("The Famous Quotes from Geeta says that")
print("\n")
for i in range(num_shlokas):
	print(final[i])
