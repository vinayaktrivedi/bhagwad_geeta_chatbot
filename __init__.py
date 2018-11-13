
from flask import Flask, redirect, url_for, request, make_response,render_template, jsonify
import csv
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import get_tmpfile
import os
cwd = os.getcwd()

app = Flask(__name__)


@app.route('/api')
def success():
   if(request.args.get('query')):
      query = request.args.get('query')

      fname = cwd+'/model_save'
      num_features = 5

      model = Doc2Vec.load(fname)
      
      q_features = model.infer_vector(query.split())

      shloka = ''
      dist_array = {}
      with open(cwd+'/result.csv','r') as file:
         fd = csv.reader(file)

         for item in fd:
            temp = []
            for i in range(num_features):
               temp.append( float(item[i]) )

            dist = np.linalg.norm(q_features - temp)
            dist_array[item[-1]] = dist

      final = sorted(dist_array, key=dist_array.__getitem__)

      num_shlokas = 5
      
      response_json = {}
      response_json['success'] = 1
      for i in range(num_shlokas):
         response_json['shloka'+str(i)] = final[i]

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

