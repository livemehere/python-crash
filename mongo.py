def get_database():
    from pymongo import MongoClient
    CONNECTION_STRING = "mongodb+srv://root:1234@cluster0.yn8vc.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['kong']
