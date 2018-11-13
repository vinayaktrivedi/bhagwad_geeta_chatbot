import json
import numpy as np

for i in range(8):

    ch = raw_input("Enter chapter Number between 10 and 18 [both inclusive]\n")
    with open('chapter'+str(ch)+'.json','r') as f:
        data = json.load(f)

        verses = len(data)
        random = []

        count = 0
        while(count<7 and count<verses):

            x = np.random.randint(0,verses)

            if x in random:
                continue
            else:
                random.append(x)

                ann = raw_input("\nThe Shloka is\n"+data[x]['meaning'].encode('UTF8')+'\n')
                ann = ann.split(',')

                list_v = []

                for item in ann:
                    temp = int(item)
                    list_v.append(temp)

                with open('verses.json','r') as file:
                    list_d = json.load(file)
                index = -1
                for shloka in list_d:
                    index += 1
                    if(shloka['meaning'].encode('UTF8') == data[x]['meaning'].encode('UTF8')):
                        list_d[index]['vector'] = list_v

                with open('verses.json','w') as file:
                    file.write(json.dumps(list_d))

                count += 1
