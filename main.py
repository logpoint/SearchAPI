from Error import Error
from LogPointSearcher import LogPointSearcher

searcher = LogPointSearcher()
class Searcher(object):
  def display_rows(self, response):
      rows = response.get_rows()
      print

      for row in rows:
          print row

  def display_iterative(self, response):
      print
      i = response.iterate()
      while i.has_next():
          dic =  i.next()
          for key in dic.keys():
              print key, ': ', dic[key]
          print '\n\n'

  def get_logpoints(self, ):
    print 'Getting LogPoints'
    logpoints = searcher.get_log_points(True)
    if isinstance(logpoints, Error):
       print 'Error : ', logpoints.get_error_message()
    else:
       print 'Getting all allowed logpoints'
       print '-------------------------------'
       count = 1
       for logpoint in logpoints:
           print '%s. %s' %(count,logpoint)
           count += 1
    print '-------------------------------'
    print '\n\n'


  def get_allowed_repos(self, ):
    print 'Getting All Allowed Repos'
    print
    repos = searcher.get_repos()
    if isinstance(repos, Error):
       print 'Error : ', repos.get_error_message()
    else:
      count = 1
      for repo in repos:
        print '%s. %s' %(count,repo)
        count +=1
    print '-----------------------'
    print '\n\n'


  def get_allowed_repos_from_logpoints(self, ):
    logpoints = searcher.get_log_points()
    
    if isinstance(logpoints, Error):
       print 'Error : ', logpoints.get_error_message()
       return
    '''change this value accordingly'''
    selected_logpoint = logpoints[0]
    print'---------------------------------------------'
    print 'Getting Repos from particular LogPoint \n', selected_logpoint
    print'---------------------------------------------'
    repos = searcher.get_repos([selected_logpoint])
    
    if isinstance(repos, Error):
       print 'Error : ', repos.get_error_message()
    else:
      count = 1
      for repo in repos:
        print '%s. %s' %(count,repo)
        count +=1
    print '-----------------------'
    print '\n\n'


  def get_allowed_devices(self, ):
    print 'Getting All Allowed Devices'
    print
    devices = searcher.get_devices()
    if isinstance(devices, Error):
       print 'Error : ', devices.get_error_message()
    else:
       count = 1
       for device in devices:
           print '%s. %s' % (count,device)
           count +=1
    print '-------------------------------------------'
    print '\n\n'


  def get_allowed_devices_from_logpoints(self, ):
    logpoints = searcher.get_log_points(False)

    
    
    if isinstance(logpoints, Error):
       print 'Error : ', logpoints.get_error_message()
       return
    
    '''change this value accordingly'''
    selected_logpoint = logpoints[1]
    
    print'\n\n---------------------------------------------'
    print 'Getting Devices from particular LogPoint \n', selected_logpoint
    print'---------------------------------------------'
    devices = searcher.get_devices([selected_logpoint])
    if isinstance(devices, Error):
       print 'Error : ', devices.get_error_message()
    else:
       count = 1
       for device in devices:
           print '%s. %s' % (count,device)
           count +=1
    print '-------------------------------------------'
    print '\n\n'


  def get_timezone(self, ):
    print 'Getting TimeZone'
    time_zone = searcher.get_timezone()
    print 'Getting Logpoint TimeZone'
    if isinstance(time_zone,Error):
       print time_zone.get_error_message()
    else:
       print 'Time Zone: %s' % time_zone
    print '-----------------------'
    print '\n\n'


  def get_queries(self, ):
    print 'Query Search from all available LogPoints'
    # type = simple
    query = ''
    
    repos_list = []
    time_range = 'Last 24 hours'
    search_job = searcher.search(query, time_range, repos_list)
    print type(search_job)
    if isinstance(search_job, Error):
       print 'Error : ', search_job.get_error_message()
       exit()

    if search_job.has_error():
       print 'Query has error'
       print 'Error Message : ',  search_job.get_error()
    else:
       print
       print 'Getting response from SearchJob'
       print
       response = search_job.get_response()
       if isinstance(response, Error):
           print 'Error : ', response.get_error_message()
           exit()

       self.display_rows(response)
    #    self.display_iterative(response)
       while not response.is_final():
           response = search_job.get_response()
           if isinstance(response, Error):
               print 'Error : ', response.get_error_message()
               exit()
           self.display_rows(response)
    #        self.display_iterative(response)
    print '\n\n'


  def get_queries_from_logpoints(self, ):
    logpoints = searcher.get_log_points()
    if isinstance(logpoints, Error):
       print 'Error : ', logpoints.get_error_message()
       return
   
    print 'Query Search from particular LogPoints'
    # uncomment line 8 to 10
    print
    # type = simple
    query = 'error'
    # type = chart
    #query = "| chart count() as Count, sum(sig_id) as SID by device_ip, source_name"
    # type = timechart
    #query = "| timechart count() as C, sum(sig_id) as SSID by device_ip, col_type"
    repos = logpoints[0].get_repos()
    if isinstance(repos, Error):
       print 'Error : ', repos.get_error_message()
       exit()
    
    repos_list = []
    for rep in repos:
       repos_list.append(rep.get_search_format())
    
    
    print repos_list
    search_job = searcher.search(query,  time_range, repos_list)
    
    if isinstance(search_job, Error):
       print 'Error : ', search_job.get_error_message()
       exit()
    
    if search_job.has_error():
       print 'Query has error'
       print 'Error Message : ',  search_job.get_error()
    else:
       response = search_job.get_response()
       if isinstance(response, Error):
           print 'Error : ', response.get_error_message()
           exit()
    
       self.display_rows(response)
    #    self.display_iterative(response)
    
       while not response.is_final():
           response = search_job.get_response()
           if isinstance(response, Error):
               print 'Error : ', response.get_error_message()
               exit()
    
           self.display_rows(response)
    #        self.display_iterative(response)
    print '\n\n'


  def get_livesearches(self, ):
    print 'Getting LiveSearch'
    livesearches  = searcher.get_live_searches()
    if isinstance(livesearches,Error):
        print livesearches.get_error_message()
    else:
        for livesearch in livesearches:
            if not isinstance(livesearch,Error):
                print "\n Livesearch-id[life_id] => ",livesearch.get_id(), \
                "\n Livesearch-query       => ",livesearch.get_query(), \
                "\n Livesearch-name        => ",livesearch.get_name(),"\n"
                # response = livesearch.get_response()
                # if isinstance(response,Error):
                #     print "\n\n\nError\t\t\t\t\n\n\n",response.get_error_message(),"\n\n\n\n"
                # else:
                #     rows = response.get_rows()
                #     print '\n\n'
                #     print 'Displaying data from list returned from get_rows()'
                #     print '\n\n'

                #     for row in rows:
                #         print row

                #     print '\n\n'
                #     print 'Iterative process for search response'
                #     print '\n\n'

                # i = response.iterate()
                # while i.has_next():
                #     dic =  i.next()
                #     for key in dic.keys():
                #         print key, ': ', dic[key]
                #     print '\n\n'
            else:
                print livesearch.get_error_message()
    print '\n\n'
    

def main():
  apisearcher = Searcher()
  # apisearcher.get_logpoints()
  # apisearcher.get_timezone()  
  # apisearcher.get_allowed_repos()
  # apisearcher.get_allowed_repos_from_logpoints()
  apisearcher.get_allowed_devices()
  # apisearcher.get_allowed_devices_from_logpoints()
  # apisearcher.get_queries()
  # apisearcher.get_queries_from_logpoints()
  # apisearcher.get_livesearches()


if __name__ == '__main__':
    main()
