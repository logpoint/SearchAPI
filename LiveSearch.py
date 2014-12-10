__author__="bunkdeath"
__date__ ="$Dec 21, 2012 1:56:50 PM$"

from Response import Response
from Error import Error
class LiveSearch:
    
    def __init__(self, id, name, query):
        """
        """
        if not id.startswith("life_"):
            self._id = "life_%s" % id
        else:
            self._id = id
        
        self._name = name
        self._query = query
            
    def get_name(self):
        ''''
        get_livesearch_name() => livesearch_name.
        '''
        return self._name
    
    def get_id(self):
        '''
        get_livesearch_id() => livesearch_id.
        livesearch_id is life_id.
        '''
        return self._id
    
    def get_query(self):
        '''
        get_livesearch_query() => livesearch_query.
        livesearch_query is query for the livesearch.
        '''
        return self._query
    
    def get_response(self):
        '''
        get_response() => returns response object

        This method returns the response object for the live search
        '''
        from LogPointSearcher import LogPointSearcher
        searcher = LogPointSearcher()
         
        self._response_string = searcher.get_response(self.get_id())
        if not isinstance(self._response_string,Error):
            return Response(self._response_string)
        else:
            return self._response_string
        