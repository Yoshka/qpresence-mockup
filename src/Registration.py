'''
Created on Aug 5, 2013

@author: nik
'''
import fingerdevice as fdev
import notifications as notificate


class registrator:
    
    def __init__(self, dev):
        self.dev = dev        

    def register_user(self):      
        
        pass
    
    def register_admin(self):
        notificate.before_scan()
        
        fprint = fdev.scan_finger(self.dev)
        result, fprint2 = self.reg_attempt(fprint)
        
        while not result:
            result, fprint2 = self.reg_attempt(fprint)
        
        
                
    
    def reg_attempt(self, fprint):
        notificate.before_scan()
        return fdev.verify_finger(self.dev, [fprint]) 
            
    
    def save_info(self):
        pass
