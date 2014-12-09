# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="bunkdeath"
__date__ ="$Jan 2, 2013 1:52:58 PM$"

class Rows:
    def __init__(self, rows):
        '''
        rows is the list of row normalized into unit row
        '''
        self._index = 0
        self._count = len(rows)
        self._rows = rows


    def has_next(self):
        '''
        this method checks if there is any more data left
        in the list
        '''
        if self._index < self._count:
            return True
        else:
            return False
        pass

    def next(self):
        '''
        this method returns next data from row
        where current curser is present
        '''
        if self._index < self._count:
            ret = self._rows[self._index]
            self._index += 1
            return ret
        else:
            return 'Sorry, no more data'

    def reset(self):
        '''
        this method is created in case one wants
        to retrieve data from beginning for testing
        '''
        self._index = 0