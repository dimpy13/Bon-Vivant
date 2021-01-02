# all the imports
import os
import sqlite3
from mysql import connector
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flaskext.mysql import MySQL
from mysql.connector import (connection)
import mysql
import constraint
import ast
import json
from settings import APP_STATIC
from flask import jsonify
from collections import OrderedDict
import csv

import numpy as np


import sys
reload(sys)
sys.setdefaultencoding("utf-8")

application = Flask(__name__)
application.debug = True

mysql = MySQL()

application.config['MYSQL_DATABASE_USER'] = ''
application.config['MYSQL_DATABASE_PASSWORD'] = ''
application.config['MYSQL_DATABASE_DB'] = ''
application.config['MYSQL_DATABASE_HOST'] = ''
application.config['MYSQL_DATABASE_PORT'] = 3306


mysql.init_app(application)

@application.route('/show')
def show_recipes():
    cur_flavor = request.args.get('flavor')
    cur_height = float(request.args.get('height'))/100
    cur_weight = request.args.get('weight')
    cur_age = request.args.get('age')
    cur_gender = request.args.get('gender')
    cur_activity = request.args.get('activityLevel')
    #cur.execute("SELECT name FROM recipes WHERE flavor = %s;", [cur_flavor])
    if cur_flavor == 8:
        flavor_name = "Slow Cooker Irish Beef Stew"
    elif cur_flavor == 7:
        flavor_name = "Cilantro Lime Chicken Tacos"
    elif cur_flavor == 6:
        flavor_name = "Shumai with Crab and Pork"
    elif cur_flavor == 5:
        flavor_name = "Cuban Style Lamb"
    elif cur_flavor == 4:
        flavor_name = "Southwestern Beef Wraps"
    elif cur_flavor == 3:
        flavor_name = "Chicken and Avocado Burritos"
    elif cur_flavor == 2:
        flavor_name = "Chicken Stir-Fry with Noodles"
    elif cur_flavor == 1:
        flavor_name = "Mexican Beef Lasagna"
    else:
        flavor_name = "Asian Garlic Tofu"
		

    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT name, nutrition, provider FROM recipe_info WHERE dbscan_label = %s;", [cur_flavor])
    fetch_result = cur.fetchmany(200)
    #return jsonify(len(fetch_result))
    satisfied_recipes = constraint.nutritional_constraints(fetch_result, cur_age, cur_weight, cur_height, cur_gender, cur_activity)
    unique = { each[0] : each for each in satisfied_recipes }.values()
  
    error = None
    entries = []
    count = 0
    #for group in satisfied_recipes:
    #    templist = []
    """for i in range(listLen):
		cur.execute("SELECT name, cuisine, provider, big_image, ingredient_amount FROM recipe_info WHERE num = %s and dbscan_label = %s;", [listRecipe[i], cur_flavor])
		temp = cur.fetchall()
		entries.append(temp)
		count = count + 1
		if count > 20:
			break"""
    conn.close()


    return jsonify(unique);

@application.route('/showr')	
def show_recipes_r():
    cnx = connection.MySQLConnection(user='recommend', password='recommend',host='recommend.c2egdgr31tgn.ap-south-1.rds.amazonaws.com', database='recipe')
    cur_flavor = request.args.get('flavor')
    cur_height = float(request.args.get('height'))/100
    cur_weight = request.args.get('weight')
    cur_age = request.args.get('age')
    cur_gender = request.args.get('gender')
    cur_activity = request.args.get('activityLevel')
    #cur.execute("SELECT name FROM recipes WHERE flavor = %s;", [cur_flavor])
    if cur_flavor == 8:
        flavor_name = "Slow Cooker Irish Beef Stew"
    elif cur_flavor == 7:
        flavor_name = "Cilantro Lime Chicken Tacos"
    elif cur_flavor == 6:
        flavor_name = "Shumai with Crab and Pork"
    elif cur_flavor == 5:
        flavor_name = "Cuban Style Lamb"
    elif cur_flavor == 4:
        flavor_name = "Southwestern Beef Wraps"
    elif cur_flavor == 3:
        flavor_name = "Chicken and Avocado Burritos"
    elif cur_flavor == 2:
        flavor_name = "Chicken Stir-Fry with Noodles"
    elif cur_flavor == 1:
        flavor_name = "Mexican Beef Lasagna"
    else:
        flavor_name = "Asian Garlic Tofu"
		
    
	cur2 = cnx.cursor(buffered=True)
	cur2.execute("SELECT id, nutrition FROM recipe_info1 WHERE dbscan_label = %s;", [cur_flavor])
	fetch_result = cur2.fetchall()
	satisfied_recipes = constraint.nutritional_constraints2(fetch_result, cur_age, cur_weight, cur_height, cur_gender, cur_activity)
	unique = { each[0] : each for each in satisfied_recipes }.values()
	#listLen = len(listRecipe)
    error = None
    entries = []
    count = 0
    #for group in satisfied_recipes:
    #    templist = []
    """for i in range(listLen):
		cur2.execute("SELECT name, cuisine, provider, big_image, ingredient_amount FROM recipe_info1 WHERE name = %s and dbscan_label = %s;", [listRecipe[i], cur_flavor])
		temp = cur2.fetchall()
		entries.append(temp)
		count = count + 1
		if count > 20:
			break"""
    cnx.close()


    return jsonify(unique);
	
@application.route('/showq')	
def show_recipes_q():
    cnx = connection.MySQLConnection(user='recommend', password='recommend',host='recommend.c2egdgr31tgn.ap-south-1.rds.amazonaws.com', database='recipe')
    cur_flavor = request.args.get('flavor')
    cur_height = float(request.args.get('height'))/100
    cur_weight = request.args.get('weight')
    cur_age = request.args.get('age')
    cur_gender = request.args.get('gender')
    cur_activity = request.args.get('activityLevel')
    #cur.execute("SELECT name FROM recipes WHERE flavor = %s;", [cur_flavor])
    if cur_flavor == 8:
        flavor_name = "Slow Cooker Irish Beef Stew"
    elif cur_flavor == 7:
        flavor_name = "Cilantro Lime Chicken Tacos"
    elif cur_flavor == 6:
        flavor_name = "Shumai with Crab and Pork"
    elif cur_flavor == 5:
        flavor_name = "Cuban Style Lamb"
    elif cur_flavor == 4:
        flavor_name = "Southwestern Beef Wraps"
    elif cur_flavor == 3:
        flavor_name = "Chicken and Avocado Burritos"
    elif cur_flavor == 2:
        flavor_name = "Chicken Stir-Fry with Noodles"
    elif cur_flavor == 1:
        flavor_name = "Mexican Beef Lasagna"
    else:
        flavor_name = "Asian Garlic Tofu"
		
    
	cur2 = cnx.cursor(buffered=True)
    cur2.execute("SELECT num, nutrition FROM recipe_info2 WHERE kmean_label = %s;", [cur_flavor])
    fetch_result = cur2.fetchmany(200)
    satisfied_recipes = constraint.nutritional_constraints(fetch_result, cur_age, cur_weight, cur_height, cur_gender, cur_activity)
    listRecipe = list(OrderedDict.fromkeys(satisfied_recipes))
    listLen = len(listRecipe)
    error = None
    entries = []
    count = 0
    #for group in satisfied_recipes:
    #    templist = []
    for i in range(listLen):
		cur2.execute("SELECT name, cuisine, provider, big_image, ingredient_amount FROM recipe_info2 WHERE num = %s and kmean_label = %s;", [listRecipe[i], cur_flavor])
		temp = cur2.fetchall()
		entries.append(temp)
		count = count + 1
		if count > 20:
			break
    cnx.close()


    return jsonify(entries);   
	
	


@application.route('/', methods=['GET', 'POST'])
def choose_flavor():
    if request.method == 'POST':
        flavor = request.form['flavor']
        height = request.form['height']
        weight = request.form['weight']
        age = request.form['age']
        gender = request.form['gender']
        return redirect(url_for('show_recipes', flavor=flavor, height=height, weight=weight, age=age, gender=gender))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    application.debug = True
    application.run()
