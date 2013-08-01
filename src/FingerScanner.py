import pyfprint.pyfprint as pyfp
import pymongo
from gridfs import GridFS
from bson.objectid import ObjectId
import time
import atexit
import signal
import sys

def verify_finger(dev, fprints=None):
    fprint_list = []
    for fprint in fprints:
        fprint_list.append(pyfp.Fprint(serial_data = fprint))   
    print 'Place your finger on the reader'
    n, fp, img = dev.identify_finger(fprint_list) 
    return n #return only index of the element 

def scan_finger(dev):    
    print 'Place your finger on the reader'
    fprint, img = dev.enroll_finger()
    return fprint.data()

def detect_printreader():
    FingerDevice = None
    while not FingerDevice:
        devs = pyfp.discover_devices()
        if len(devs) == 0:
            print "No devices available\n"
        else:
            FingerDevice = devs[0]
            break
        time.sleep(1)

    FingerDevice.open()
    if not FingerDevice.supports_identification():
        raise "Device cannot do identification"
    print "Found a " + FingerDevice.driver().full_name()
    print 'Enroll stages: ' + str(FingerDevice.nr_enroll_stages())
    print 'Supports imaging: ' + str( FingerDevice.supports_imaging())
    print 'Supports identification:  ' + str(FingerDevice.supports_identification())
    return FingerDevice

@atexit.register
def close_pyfprint():
    print 'I quit'
    pyfp.fp_exit()
    
def cleanup(sig, func=None):
    print 'Exiting'
    pyfp.fp_exit()
    sys.exit(1)

if __name__ == "__main__":
#     mode = 1 - registration mode
#     mode = 2 - identification mode
    mode = 1 
    dev = detect_printreader()                          #try to detect fingerprint reader
     
    if dev !=None :
        client = pymongo.MongoClient("localhost", 27017)#connect to mongodb
        db = client.fdb                                 #use fdb database    
        fs = GridFS(db)                                     
        if mode==1:
            print '-------------------------------------------------------------registration mode'
            current_finger = scan_finger(dev)
            current_finger_file_id = fs.put(current_finger, filename="employee")
            print 'Fingerprint saved with id: ' + str(current_finger_file_id)
        elif mode==2:
#             python run some code when the program is killed by a signal
#             signal.signal(signal.SIGABRT, cleanup)
#             signal.signal(signal.SIGINT, cleanup)
#             signal.signal(signal.SIGKILL, cleanup) http://crunchtools.com/unixlinux-signals-101/
#             signal.signal(signal.SIGTERM, cleanup)
            print '------------------------------------------------------------identification mode'
            while True:
                cursor_for_files = db.fs.files.find()
                all_fingerprint_files_ids = []
                for current_file in cursor_for_files:
                    all_fingerprint_files_ids.append(current_file["_id"])
                    all_fingerprint_files_data = []
                    for file_id in all_fingerprint_files_ids:
                        all_fingerprint_files_data.append(fs.get(file_id).read())
                        if verify_finger(dev, all_fingerprint_files_data)!=None:
                            print "Yeah, you are in the system"
                        else:
                            print "See you first time"
    

       