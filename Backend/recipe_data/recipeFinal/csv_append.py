import pandas as pd

results = pd.DataFrame([])

namedf = pd.read_csv('recipe_final-100.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-200.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-300.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-400.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-500to1500.csv', skiprows=0 , usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-1500to2500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-2500to3000.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-3000to3300.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-3300to3500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-3500to3600.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-3600to3700.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-3700to3720.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-3750to3800.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-3800to3900.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-3900to4000.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-4001to4100.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-4100to4150.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-4200to4300.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-4300to4400.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-4400to4500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-4500to5500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-4815to5500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-4840to5500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-5500to6500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)
namedf = pd.read_csv('recipe_final-6500to9500.csv', skiprows=0, usecols=['num','course_cuisine','cusine','course','flavor','id','small_image',
                                                                  'rating','name', 'another_small_image','provider','time',
                                                                  'big_image','ingredient_amount','serving_number','nutrition'])
results = results.append(namedf)

results.to_csv('data_Recipe.csv')
