__author__="bunkdeath"
__date__ ="$Dec 21, 2012 1:56:59 PM$"

class Device:
#TODO
#what to print for device. device name format
    def __init__(self, ip, name, logpoint):
        """
        device ip address
        device name
        logpoint object(logpoint ip, logpoint name)
        """
        self.ip = ip
        self.name = name
        self.logpoint = logpoint

    def get_ip(self):
        '''
        get_ip() => returns IP
        
        This method returns the IP address of the device
        '''
        return self.ip


    def get_name(self):
        '''
        get_name() => returns name
        
        This method returns name of the device
        '''
        return self.name

    def get_logpoint(self):
        '''
        get_logpoint() => returns logpoint object
        
        This method returns the logpoint object respective to the device
        '''

        
        return self.logpoint

    def __str__(self):
        info = 'Device Info\n'
        info += '\tRespective LP Name  : ' + self.logpoint.get_name() + '\n'
        info += '\tDevice IP           : ' + self.ip + '\n'
        info += '\tDevice Name         : ' + self.name + '\n'
        return info
