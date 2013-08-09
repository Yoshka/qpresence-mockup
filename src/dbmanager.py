'''
@author: Gutyk Iurii
'''
import pymongo
from gridfs import GridFS
from bson.objectid import ObjectId

class DbManager:
    
    def __init__(self):
        self.db = self.get_db()
    
    def get_db(self):
        client = pymongo.MongoClient("localhost", 27017)#connect to mongodb
        return client.fdb                                 #use fdb database
    
    def save_finger(self, finger_data, file_name):
        fs = GridFS(self.db)
        return fs.put(finger_data, filename=file_name) #return file ObjectId 
    
    def get_all_fingers_data(self):
        cursor_for_files = self.db.fs.files.find()
        fs = GridFS(self.db)
        all_fingerprint_files_ids = []
        for current_file in cursor_for_files:
            all_fingerprint_files_ids.append(current_file["_id"])
            all_fingerprint_files_data = []
            for file_id in all_fingerprint_files_ids:
                all_fingerprint_files_data.append(fs.get(file_id).read())
            return all_fingerprint_files_data
    
    def check_no_fprints(self):
        return self.db.fs.files.count() > 0
        