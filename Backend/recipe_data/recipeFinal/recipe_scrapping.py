import csv
import pandas as pd
import numpy as np
import requests
import json
from addict import Dict
import urllib.request


df = pd.read_csv('D:/recipe_data/training set/recipeCompound.csv', nrows=660, skiprows=range(1,4840))
req_column = df['id']

# print (req_column)
recipeComp = [[0] * 16 for i in range(660)]
j = -1

for id in req_column:
    # print (id)
    # r = (requests.get("https://api.yummly.com/v1/api/recipe/"+ id +"?_app_id=50c895b7&_app_key=1bc3e6a3e47ae34d3d54c6b77bca40ee")).json()
    response = urllib.request.urlopen(
        "https://api.yummly.com/v1/api/recipe/" + id + "?_app_id=50c895b7&_app_key=1bc3e6a3e47ae34d3d54c6b77bca40ee")
    data = json.load(response)


    def get_value(listOfDicts, key):
        for subVal in listOfDicts:
            if key in subVal:
                return subVal[key]
            else:
                return " "

    req_nutrition =  data.get('nutritionEstimates')
    #print (req_nutrition)

    if req_nutrition != []:

        # print (data)
        j = j + 1
        print (j)

        recipeComp[j][0] = j
        recipeComp[j][1] = data.get('attributes')
        y = recipeComp[j][1]
        recipeComp[j][2] = y.get('cuisine')
        recipeComp[j][3] = y.get('course')
        recipeComp[j][4] = data.get('flavors')
        recipeComp[j][5] = data.get('id')

        # print (get_value(data['images'], 'hostedSmallUrl'))

        recipeComp[j][6] = get_value(data['images'], 'imageUrlsBySize')
        recipeComp[j][7] = data.get('rating')
        recipeComp[j][8] = data.get('name')
        recipeComp[j][9] = get_value(data['images'], 'hostedSmallUrl')
        z = data.get('source', " ")
        recipeComp[j][10] = z.get('sourceRecipeUrl')
        recipeComp[j][11] = data.get('totalTime')
        recipeComp[j][12] = get_value(data['images'], 'hostedMediumUrl')
        recipeComp[j][13] = data.get('ingredientLines')
        recipeComp[j][14] = data.get('yield')
        recipeComp[j][15] = data.get('nutritionEstimates')

        #print ("YOOOOO")
        with open("D:/recipe_data/recipeFinal/recipe_final-4840to5500.csv", "w", encoding="utf8", newline='') as f1:
            writer = csv.writer(f1)
            writer.writerows(recipeComp)