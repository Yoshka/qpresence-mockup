'''
Created on Aug 6, 2013

@author: nik
'''

import fingerdevice as fdev
import notifications as notificate 
from Registration import registrator
import msvcrt 

class State:
    Undefined = 0
    RegularScan = 1
    AdminRegistration = 2
    RegularRegistration = 3
    

class StateMachine(object):
    '''
    classdocs
    '''

    def __init__(self, dbManager):
        '''
        Constructor
        '''
        self.state = State.Undefined
        self.db = dbManager
        
        self.start()
    
         
    def start(self):
        '''
        machine cycle initialization
        '''
        if self.db.check_no_fprints():
            self.state = State.AdminRegistration
        else:
            self.state = State.RegularScan
      
        while True:    
            self.cycle()
            
            
    def cycle(self):
        '''
        machine cycle
        '''
        self.kbfunc()
        
        if self.state == State.RegularScan:
            print 'RegularScan'
            pass        
        elif self.state == State.RegularRegistration:
            pass
        elif self.state == State.AdminRegistration:
            print 'AdminRegistration'
            self.admin_registration()
        else:
            print 'Machine state error!!!!'
            
        
    def admin_registration(self):
        '''
        Admin user registration function. Executes if no user records.  
        '''
        dev = fdev.detect_printreader()
        self.state = State.RegularScan
        
        
            
            
            
        
        
        
        
        
        
        
            
        
            
            