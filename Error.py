'''
Created on Jan 3, 2013

@author: mama
'''
class Error:
    def __init__(self,error_message):
        
        self._has_error = True
        self._error_message = error_message
    
    def has_error(self):
        '''
        get_has_error() => Boolean
        Returns true if the object has an error otherwise false.
        ''' 
        return self._has_error
    
    def get_error_message(self):
        '''
        get_error_message() => error message associated with the object. 
        
        '''
        return self._error_message