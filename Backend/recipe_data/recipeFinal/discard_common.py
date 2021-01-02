import csv
import numpy as np
import time
import pandas as pd

df = pd.read_csv('recipe_info.csv')

j=0
print(df['id'][j])
print(df['id'][j+1])


count=0
j=0
i=1

print(df['id'].count())

for j in range(27426):
    j=j+1
    for i in range(27426):
        i=i+1
        if df['id'][j] == df['id'][i]:
            print(df['id'][j], df['id'][i])
            count=count+1


print(df['id'].count())
print(count)





        #if a == b :
        #    count=count+1
        #    print (recipes[j][6],recipes[i][6])
        #    recipes.remove(recipes[j])






