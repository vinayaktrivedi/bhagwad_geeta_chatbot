
from flask import Flask, redirect, url_for, request, make_response,render_template, jsonify
import csv
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile
import os
import json
from phrase_extract import main
from thesaurus import Word


app = Flask(__name__)


@app.route('/api')
def success():
   if(request.args.get('query')):
      query = request.args.get('query')

      fname = '/var/www/chatbot/chatbot/model_save'
      num_features = 5

      model = Doc2Vec.load(fname)
      
      q_features = model.infer_vector(query.split())

      shloka = ''
      dist_array = {}
      with open('/var/www/chatbot/chatbot/result.csv','r') as file:
         fd = csv.reader(file)

         for item in fd:
            temp = []
            for i in range(num_features):
               temp.append( float(item[i]) )

            dist = np.linalg.norm(q_features - temp)
            dist_array[item[-1]] = dist

      final = sorted(dist_array, key=dist_array.__getitem__)
      phrase = main(query)
      arr = []
      arr.append(Word(str(phrase[0][0])).synonyms())

      if(len(phrase) > 1):
         arr.append(Word(str(phrase[1][0])).synonyms())

      print(arr)
      with open('/var/www/chatbot/chatbot/sins.json','r') as filen:
         sins = json.load(filen)

      sin_array ={}

      for key,value in sins.iteritems():

         for sin in value:
            count = 0
            distance = 0.0
            for syn in arr: 
               for word in syn:
                  vector1 = model.infer_vector([word])
                  vector2 = model.infer_vector([sin])
                  count += 1
                  distance += np.linalg.norm(vector2 - vector1)

         if(count == 0):
            sin_array[key] = 0
         else:

            sin_array[key] = distance/count


      with open('/var/www/chatbot/chatbot/verses.json','r') as ver:
         data_verse = json.load(ver)

      final2 = sorted(sin_array, key=sin_array.__getitem__)
      sin_index = 0

      if (final2[0] == 'depression'):
         sin_index = 0

      if (final2[0] == 'gluttony'):
         sin_index = 1

      if (final2[0] == 'greed'):
         sin_index = 2

      if (final2[0] == 'sloth'):
         sin_index = 3

      if (final2[0] == 'angry'):
         sin_index = 4

      if (final2[0] == 'envy'):
         sin_index = 5

      if (final2[0] == 'pride'):
         sin_index = 6

      rating = {}
      for item in data_verse:
         if('vector' in item):
            rating[item['meaning']] = 0.6*item['vector'][sin_index]

         else:
            rating[item['meaning']] = 0
      
         iter_v = len(final)

         for j in range(iter_v):
            if(item['meaning'].encode('UTF8') == final[j]):
               rating[item['meaning']] += 4*((iter_v-j)/(iter_v*1.0))

      final_out = sorted(rating, key=rating.__getitem__)
      num_shlokas = 5
      
      response_json = {}
      response_json['success'] = 1

      metadata_arr = []

      for i in range(num_shlokas):
         for search in data_verse:
            if search['meaning'].encode('UTF8') == final_out[i]:
               metadata_arr.append(search['chapter_number'])
               metadata_arr.append(search['verse_number'])


      for i in range(num_shlokas):
         obj = {}
         obj['text'] = final_out[i]
         obj['chapter'] = metadata_arr[2*i]
         obj['verse_id'] = metadata_arr[2*i+1]
         response_json['shloka'+str(i)] = obj

      return jsonify(response_json)

   else:
      response_json = {}
      response_json['success'] = 0
      return jsonify(response_json)
   

@app.route("/")
def hello():
    return "Hello, Welcome"

if __name__ == "__main__":
    app.run()

