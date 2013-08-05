import fingerdevice as fdev
import dbmanager as dbm
import notifications as ntfs
import atexit

@atexit.register
def cleanup():
    fdev.stop_device()

if __name__ == "__main__":
#     mode = 1 - registration mode
#     mode = 2 - identification mode
    mode = 2 
    dev = fdev.detect_printreader()                          #try to detect fingerprint reader
    if dev !=None :
        db = dbm.get_db()
        if mode==1:
            print '-------------------------------------------------------------registration mode'
            current_finger = fdev.scan_finger(dev)
            ntfs.before_scan()
            current_finger_file_id = dbm.save_finger(db, current_finger, "employee")
            ntfs.after_save(current_finger_file_id)
        elif mode==2:
            print '------------------------------------------------------------identification mode'
            while True:
                all_fingers = dbm.get_all_fingers_data(db)
                ntfs.before_scan()
                if fdev.verify_finger(dev, all_fingers) != None:
                    ntfs.user_authenticated()
                else:
                    ntfs.user_not_authenticated()