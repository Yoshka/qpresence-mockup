'''
@author: Gutyk Iurii
'''
def before_scan():
    print 'Place your finger on the reader'
def after_save(file_id):
    print 'Fingerprint saved with id: ' + str(file_id)
def user_authenticated():
    print "Yeah, you are in the system"
def user_not_authenticated():
    print "See you first time"
    
    
