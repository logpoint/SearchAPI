'''
Created on Dec 21, 2012

@author: mama
'''
class LogPoint:
    
    def __init__(self, ip, name=None):
        """
        logpoint ip address
        logpoint name
        """
        self.ip = ip
        if name:
            self.name = name
        else:
            self.name = self.ip.replace(".", "_")

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def get_repos(self):
        from LogPointSearcher import LogPointSearcher
        searcher = LogPointSearcher()
        return searcher.get_repos([self])
    
    def __str__(self):
        info = 'LogPoint Info\n'
        info += '\tName : ' + self.name + '\n'
        info += '\tIP   : ' + self.ip + '\n'
        return info