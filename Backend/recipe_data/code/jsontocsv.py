import json
import csv



with open('D:/recipe_data/thai.json', 'r', encoding="utf8") as f:
    datastore = json.load(f)

recipeComp=[[0]*3 for i in range(592)]
j=-1
for trees in datastore:
    j=j+1
    trees = datastore[j]
    recipeComp[j][0]= j
    recipeComp[j][1]= trees['id']
    recipeComp[j][2]= trees['ingredients']
    with open("D:/recipe_data/thai_csv.csv", "w", encoding="utf8", newline='') as f1:
        writer = csv.writer(f1)
        writer.writerows(recipeComp)