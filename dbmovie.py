import mongo

db = mongo.get_database()

data = db['movies'].update_one({'title':'가버나움'},{'$set':{
    'point':'0.00'
}})

