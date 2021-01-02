# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import json
from settings import APP_STATIC
from flask import jsonify
from collections import OrderedDict
import csv
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity



application = Flask(__name__)
application.debug = True

def finddishes(idx,similar_cuisine=False):
    yum_ingr = pd.read_pickle('yummly_ingr.pkl')
    yum_ingrX = pd.read_pickle('yummly_ingrX.pkl')
    yum_tfidf = pd.read_pickle('yum_tfidf.pkl')
    yum_cos = cosine_similarity(yum_tfidf)
    print (yum_cos)
    # reset index yum_ingr
    yum_ingr2 = yum_ingr.reset_index(drop=True)

    cuisine = yum_ingr2.iloc[idx]['cuisine']
    print ('Dishes similar to', yum_ingr2.ix[idx, 'recipeName'], '('+yum_ingr2.ix[idx, 'cuisine']+')')
    match = yum_ingr2.iloc[yum_cos[idx].argsort()[-21:-1]][::-1]
    print (match['id'])
    print (len(match))
    return match['id']
 

@application.route('/recommend')
def recommend():
    index = request.args.get('index')
    idx = int(index)
    # plot similar dishes for Fettucini Bolognese
    #idx = 320
    xlim = [0.81, 1.0]
    output = finddishes(idx, similar_cuisine=False)
    listRecipe = list(OrderedDict.fromkeys(output))
    return jsonify(listRecipe)

@application.route('/indianRecipes')
def indianRecipes():
	data = []
	with open('yummly_clean.csv', encoding='utf8') as f:
		for row in csv.DictReader(f):
			data.append([row['index'],row['recipeName']])
	json_data = json.dumps(data)
	return json_data


if __name__ == "__main__":
    application.debug = True
    application.run()
