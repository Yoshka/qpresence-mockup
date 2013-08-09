'''
Created on Aug 5, 2013

@author: nik
'''

from dbmanager import DbManager
import FingerScanner as scanner
from statemachine import StateMachine


if __name__ == '__main__':
    
    dbManager = DbManager()
    statemachine = StateMachine(dbManager)
    statemachine.start()
    
    
    
#     scanner.start(2)
