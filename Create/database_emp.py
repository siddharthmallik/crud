"""
from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/ipldb?retryWrites=true&w=majority')
	db = con.ipldb
	col = db.players

def get_players():
	global col
	connect_db()
	data_from_db = col.find({})
	return data_from_db

def save_players_info():
	global col
	connect_db()
	col.insert()
	return
"""

from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/Employee?retryWrites=true&w=majority')
	db = con.Employee
	col = db.employee_records


def get_emplyoee_details():
	global col
	connect_db()
	emp_data_from_db = col.find({})
	return emp_data_from_db


def save_emplyoee_details(empinfo):
	global col
	connect_db()
	col.insert(empinfo)
	return

def delete_emplyoee_details(empinfo):
    global col
    connect_db()
    myquery = {"_id": ObjectId(store_mid)}
    col.delete_one(myquery)
    return

def activate_emplyoee_details(empinfo):
    global col
    connect_db()
    emp_data_from_db = 'livestatus'
    col.update_one({"_id": ObjectId(store_mid)}, {'$set' : {emp_data_from_db : True}})
    return

def change_emplyoee_details(empinfo):
    global recipcol
    connect_db()
    emp_data_from_db = 'Lowes New record'
    col.update_one({'Lowes Store Number':id}, {'$set' : {emp_data_from_db : 7876}})
    return

def edit_retailer(store_mid, store_id, store_name, livestatus):
    global col
    connect_db()
    col.update_one({"_id": ObjectId(store_mid)}, {'$set' : { "storeid" : store_id, "storename" : store_name, "livestatus" : livestatus}})
    return
