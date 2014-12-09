import json
import time
import Config
import requests
from Config import Config
from LogPoint import LogPoint
from Device import Device
from SearchJob import SearchJob
from Repos import Repo
from LiveSearch import LiveSearch
from Error import Error

class LogPointSearcher:
    '''
    Searcher class to search for following
    '''
    def __init__(self):
        config = Config()
        self.ip = config.ip
        self.username = config.username
        self.secert_key = config.secret_key
        self.request_type = config.request_type


    def get_log_points(self):
        '''
        Returns list of LogPoint object
        '''
        """
            send requests to given IP using username and secret_key for type = "logpoints"
            our webserver should return [{"name": "", "ip":""}]
        """

        logpoints = []
        
        response = self._get_allowed_data('loginspects')
        if isinstance(response, Error):
            return response
        else:
            if not response.get('success'):
                return Error(response.get('message'));
            
            allowed_logpoint = response['allowed_loginspects'];
            for data in allowed_logpoint:
                logpoints.append(LogPoint(data["ip"], data["name"]))

            return logpoints


    def get_repos(self, logpoint_object=None):
        ''' 
        Search for repos for which the user have permission to access
        according to credential provided

        If no parameter passed, it searches for the repos within
        all logpoints

        If logpoint object is passed as a parameter,
        it searches for the repos within the logpoint referenced
        by the logpoint object

        Returns list of Repo object
        '''

        if not logpoint_object:
            logpoint_object = []
                
        repos = []
        logpoint = {}
        logpoint_list = []
        
        for logpoint_row in logpoint_object:
            lp = logpoint_row.get_ip()
            logpoint_list.append(lp)

        response =  self._get_allowed_data("logpoint_repos", logpoint_list)

        if isinstance(response, Error):
            return response

        if not response.get('success'):
            return Error(response.get('message'))
        
        allowed_repos = response.get('allowed_repos')
        response_logpoint_string = response.get('logpoint')

        if response_logpoint_string:
            '''
            get all the logpoints

            if only results have logpoint key and its value

            if it is not contained, most probable the logpoint
            object list is passed in the method
            '''
            for logpt in response_logpoint_string:
                logpoint_ip = logpt.get('ip')
                logpoint_name = logpt.get('name')
                #TODO
                # what if, instead of logpoint object,
                # logpoint name is provided?
                logpoint[logpoint_ip] = LogPoint(logpoint_ip, logpoint_name)
        else:
            '''
            if logpoint objects were passed in method parameter

            generate logpoint list
            '''
            for logpt in logpoint_object:
                logpoint[logpt.get_ip()] = logpt


        '''
        get repo_name and its ip, and reference back to logpoint
        '''
        for repo in allowed_repos:
            address, repo_name = repo.get('address'), repo.get('repo')
            logpoint_ip, port = address.split(':')
            repos.append(Repo(logpoint[logpoint_ip], repo_name))
        return repos

    def get_devices(self, logpoint=None):
        '''
        Search for devices for which the user have permission to access
        according to credential provided

        If no parameter passed, it searches for the devices within
        all logpoints

        If logpoint object is passed as a parameter,
        it searches for the devices within the logpoint referenced
        by the logpoint object

        Returns list of Device object
        '''
        
        devices = []
        logpoint = {}

        response = self._get_allowed_data('devices')
        if isinstance(response, Error):
            return Response
        
        if not response.get('success'):
            return Error(response.get('message'))
        
        allowed_devices = response['allowed_devices'];
        logpoints = response['logpoint']

        '''
        get all the logpoints
        '''
        for logpt in logpoints:
            logpoint_ip = logpt.get('ip')
            logpoint_name = logpt.get('name')
            logpoint[logpoint_ip] = LogPoint(logpoint_ip, logpoint_name)
        

        for i in range(len(allowed_devices)):
            data = allowed_devices[i]
            if type(data) is dict:
                for row in data:
                    lp, ip = row.split('/')
                    devices.append(Device(ip, data[row], logpoint[lp]))
        
        return devices

    def get_live_searches(self):
        '''
        Returns list of LiveSearch object
        '''
        
        live_searches_lists = []
        try:
            live_searches =  self._get_allowed_data('livesearches')
            if live_searches.get("success"):
                for live_search in live_searches["livesearches"]:
                    live_searches_lists.append(LiveSearch(live_search["life_id"],live_search["searchname"],live_search["query"]))#,"livesearch"))
                return live_searches_lists
            else:
                return Error(live_searches["message"])
        except Exception, e:
            
            return Error(str(e))

    def get_timezone(self):
        '''
        Returns timezone of user according to credential provided
        '''
        """
            webserver should return UTC or Asia/Kathmandu
        """
        time_zone = self._get_allowed_data('user_preference')
        if isinstance(time_zone, Error):
            return time_zone
        else:
            if not time_zone.get("success"):
                return Error(time_zone.get("message"))
                
            else:
                return time_zone.get("timezone")

    def search(self, query, timerange=None, repo=None, timeout=30, limit=100):
        '''
        Returns SearchJob object
        '''

        return self._get_search_job(query, timerange, repo, timeout, limit)

    def _get_allowed_data(self, data_type, logpoints=None):
        url = "%s://%s/%s" % (self.request_type, self.ip, "getalloweddata")

        data = {
                "username": self.username,
                "secret_key": self.secert_key,
                "type": data_type,
                "logpoints": json.dumps(logpoints)
                }

        
        try:
	    print 'url=%s' % url
            ack = requests.post(url, data=data, timeout=10.0, verify=False)
            print ack.content
        except Exception, e:
            return Error(str(e))
#            print resp
#            return resp

        ret = ''
        try:
            ret = json.loads(ack.content)
        except:
            pass
#            print ack.content

        return ret


    def _get_search_job(self, query, timerange=None, repo=None, timeout=None, limit=None):
        SEARCH_QUERY = query
        
        if not timerange:
            SEARCH_TIME_RANGE = 'Last 10 minutes'
        else:
            SEARCH_TIME_RANGE = timerange

        if not repo:
            # TODO
            # check if repo is list of string or repo object
            SEARCH_REPOS = []
        else:
            SEARCH_REPOS = repo

        if not timeout:
            timeout = 10

        if not limit:
            RESULT_LIMIT = 30
        else:
            RESULT_LIMIT = limit

        url = "%s://%s/%s" % (self.request_type, self.ip, "getsearchlogs")
        data = {
                "username":self.username,
                "secret_key": self.secert_key,
                "requestData": json.dumps({
                               "timeout": 30,
                               "client_name": "gui",
                               "repos": SEARCH_REPOS,
                               "starts": {},
                               "limit": RESULT_LIMIT,
                               "time_range": SEARCH_TIME_RANGE,
                               "query": SEARCH_QUERY
                            })
                }

        try:
            ack = requests.post(url, data=data, timeout=10.0, verify=False)#verify = True => SSL certificate will be verified.
        except Exception, e:
            return Error(str(e))
        
        response = json.loads(ack.content)
        return SearchJob(response)
        

    def get_response(self, search_id, version=None):
        if not version:
            version = 0
        url = "%s://%s/%s" % (self.request_type, self.ip, "getsearchlogs")
        if search_id:
            data = {
                "username":self.username,
                "secret_key": self.secert_key,
                "requestData": json.dumps({
                           "search_id": search_id,
                           "waiter_id": "%s" % time.time(),
                           "seen_version": version
                           })
                }
            start_time = time.time()
            response = {}
            while time.time() - start_time < 10.0:
                try:
                    ack = requests.post(url, data=data, timeout=10.0, verify=False)
                    #TODO 
#                   check the error if any occoured in ack. 
                    res = json.loads(ack.content)
#                    print ack.content
                    if res.get('success'):
                        response = res
                    else:
#                        print res
                        return Error(res.get("message"))
                    if res['final'] == True:
                        break
                except Exception, e:
#                    print 'LPS line 321', str(e)
                    return Error(str(e))

            if not response:
                return Error('No data from merger')
            
#            print response
            return response
