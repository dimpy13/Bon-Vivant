import pandas as pd

results = pd.DataFrame([])

namedf = pd.read_csv('data_Recipe.csv', skiprows=0, usecols=['index','course_cuisine','course','cuisine','flavor','id','small_image','rating','name','another_small_image','provider','time','big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final.csv', skiprows=0, usecols=['index','course_cuisine','course','cuisine','flavor','id','small_image','rating','name','another_small_image','provider','time','big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)


results.to_csv('recipe_info.csv')
