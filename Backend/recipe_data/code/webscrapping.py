
import requests
import json
import pandas as pd
import numpy as np
import time

def initial_df(cykey,scuisine1,scourse,sresults):

    r = (requests.get('http://api.yummly.com/v1/api/recipes?' + cykey + scuisine1 + scourse + sresults)).json()

    print(r.keys())
    print (r)
    #print (len(r['matches']))
    yum = pd.DataFrame(r['matches'])
    yum['cuisine'] = yum['attributes'].apply(lambda x: x['cuisine'][0])
    yum['course'] = yum['attributes'].apply(lambda x: x['course'][0])
    print (yum['cuisine'].value_counts())
    yum = yum[yum['cuisine']=='Indian']
    return yum

def grow_df(cuisinedic,cykey,scourse,sresults,yum):

    for cs in cuisinedic:
        try:
            scuisine = '&allowedCuisine[]=cuisine^cuisine-' + cs
            r = (requests.get('http://api.yummly.com/v1/api/recipes?' + cykey + scuisine + scourse + sresults)) .json()
            print (scuisine)

            newrecipes = pd.DataFrame(r['matches'])

            course = []
            cuisine = []
            for item in r['matches']:
                course.append(item['attributes'].get('course', None)[0])
                cuisine.append(item['attributes'].get('cuisine', None)[0])
            newrecipes['course'] = course
            newrecipes['cuisine'] = cuisine

            newrecipes = newrecipes[newrecipes['cuisine']==cuisinedic[cs]]
        
            yum = pd.concat([yum,newrecipes],axis=0,ignore_index=True)
            print (yum.shape)
        except:
            print("Skipping one ......\n")
            pass

        #time.sleep(300)
    return yum



if __name__ =='__main__':

    cykey = '_app_id=50c895b7&_app_key=1bc3e6a3e47ae34d3d54c6b77bca40ee'
    scuisine1 = '&allowedCuisine[]=cuisine^cuisine-' + 'chinese'
    scourse = '&allowedCourse[]=course^course-Main Dishes'
    sresults = '&maxResult=' + '50'

    yum = initial_df(cykey,scuisine1,scourse,sresults)

       cuisinedic = {'italian':'Italian', 'mexican':'Mexican', 'southern':'Southern & Soul Food', 'french':'French', 'southwestern':'Southwestern', 'indian':'Indian', 'cajun':'Cajun & Creole', 'english':'English', 'mediterranean':'Mediterranean', 'greek':'Greek', \
    'spanish': 'Spanish', 'german':'German', 'thai':'Thai', 'moroccan':'Moroccan', 'irish':'Irish', 'japanese':'Japanese', 'cuban':'Cuban', 'swidish':'Swidish', 'hungarian':'Hungarain', 'portuguese':'Portuguese','american':'American'}

    yum = grow_df(cuisinedic,cykey,scourse,sresults,yum)

    yum.to_pickle('data/yummly.pkl')
