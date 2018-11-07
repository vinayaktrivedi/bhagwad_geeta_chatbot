import json 
import numpy as np 

for i in range(4):
    print("\n\n")
    print('Chapter '+str(i+1))
    print("\n\n")
    with open('chapter'+str(i+1)+'.json') as f:
    	data = json.load(f)

    	verses = len(data)
    	random = []

    	count = 0
    	while(count<25):
    		x = np.random.randint(0,verses)

    		if x in random:
    			continue
    		else:
    			random.append(x)

    			print(data[x]['meaning'].encode('UTF8'))

    			count += 1