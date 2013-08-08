'''
@author: Gutyk Iurii
'''
import pyfprint.pyfprint as pyfp
import time

def stop_device():
    print 'I quit'
    pyfp.fp_exit()

def verify_finger(dev, fprints=None):
    fprint_list = []
    for fprint in fprints:
        fprint_list.append(pyfp.Fprint(serial_data = fprint))   
    n, fp, img = dev.identify_finger(fprint_list) 
    return n, fp #return only index of the element 

def scan_finger(dev):    
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

