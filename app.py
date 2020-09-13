from flask import Flask, request, Response
import json

from jsonschema import validate

from schema import *
    

app = Flask(__name__)

###   Connecting to mongodb atlas
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://dbuser:0000@cluster0.jbocx.mongodb.net/Wander_Force?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Wander_Force')


###

from bson import json_util 

@app.route('/history/<usertype>/<string:userid>', methods=['GET'])
def history(userid, usertype):
    
    data = db.history.find()

    print(data)
    print(type(data))

    me = []
    for doc in data:
        print(doc)
        me.append(doc)

    z = []

    for obj in me:
            #if usertype == 'user':
            if obj[usertype+'id'] == userid:
                print(obj)
                z.append(obj)
        # elif usertype == 'worker':
        #     if obj['worker'] == userid:
        #         print(obj)
        #         z.append(obj)
    
    print(type(z))


    #print(me)
    #print(type(me[0]))
    x = json.dumps(me, default=str)
    #print(x)
    #print(type(x))

    y = json.loads(x)
    
    #print("****")
    #print(y)
    #print(type(y))
    #print("****")
    #this is now a list

    return json.dumps(z, default=str)


@app.route('/create/user', methods=['POST'], endpoint='createUser')
def createUser():
    indata = request.get_json()

    try:
        validate(instance = indata, schema=userschema)
    except Exception as e:
        return Response(str(e), status=400)
    
    id = db.Users.insert_one(indata)

    newid = str(id.inserted_id)
    resp = Response(newid, status=200)
    
    return resp


@app.route('/create/worker', methods=['POST'], endpoint='createWorker')       
def createWorker():
    indata = request.get_json() 

    try:
        validate(instance = indata, schema=workerschema)
    except Exception as e:
        return Response(str(e), status=400)

    id = db.Workers.insert_one(indata)

    newid = str(id.inserted_id)
    resp = Response(newid, status=200)
    
    return resp

    
