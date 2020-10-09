"""
from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import ipldb

app = Flask(__name__)

app.secret_key = "siddharth"

@app.route("/")
def index():
	cursor = ipldb.get_players()
	userinfolist = []
	for d in cursor:
		userinfolist.append(d)
	return render_template('base.html', userlist =[])

@app.route("/", methods=['POST'])
def update_players():
	newdata = {}
	name = request.form['name']
	matches = request.form['matches']
	runs = request.form['runs']
	centuries = request.form['centuries']
	average = request.form['average']
	#send data to db
	newdata["name"] = name
	newdata["matches"] = matches
	newdata["runs"] = runs
	newdata["centuries"] = centuries
	newdata["average"] = average
	print (newdata)
	ipldb.save_players(newdata)
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)

"""
from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import database_emp

app = Flask(__name__)


app.secret_key="dst5wukhsyurshjmuxy987"



#Its the entry point to the browser
@app.route("/")
def index():
	#get all data from db
	empinfo = database_emp.get_emplyoee_details()
	empdetailslist = []
	for e in empinfo:
		empdetailslist.append(e)
	return render_template('base.html', emplist = empdetailslist )



@app.route("/", methods=['POST'])
def update_emp_record():
	empdata = {}
	name = request.form['uname']
	designation = request.form['desig']
	phone_num = request.form['phone_num']
	address = request.form['address']
	email = request.form['email']
	#send data to db
	empdata["name"] = name
	empdata["designation"] = designation
	empdata["phone_num"] = phone_num
	empdata["address"] = address
	empdata["email"] = email
	print (empdata)
	database_emp.save_emplyoee_details(empdata)
	return redirect(url_for('index'))

@app.route("/delete", methods=['POST'])
def deleteInstaller(empinfo):
    store_id = empinfo
    database_emp.delete_emplyoee_details(store_id)
    return redirect(url_for('index'))

@app.route("/activate", methods=['POST'])
def activateInstaller(empinfo):
    store_id = empinfo
    database_emp.activate_emplyoee_details(store_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)



