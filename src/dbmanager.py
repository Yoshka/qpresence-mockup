'''
@author: Gutyk Iurii
'''
import pymongo
from gridfs import GridFS
from bson.objectid import ObjectId

def get_db():
    client = pymongo.MongoClient("localhost", 27017)#connect to mongodb
    return client.fdb                                 #use fdb database

def save_finger(database, finger_data, file_name):
    fs = GridFS(database)
    return fs.put(finger_data, filename=file_name) #return file ObjectId 

def get_all_fingers_data(database):
    cursor_for_files = database.fs.files.find()
    fs = GridFS(database)
    all_fingerprint_files_ids = []
    for current_file in cursor_for_files:
        all_fingerprint_files_ids.append(current_file["_id"])
        all_fingerprint_files_data = []
        for file_id in all_fingerprint_files_ids:
            all_fingerprint_files_data.append(fs.get(file_id).read())
        return all_fingerprint_files_data
    