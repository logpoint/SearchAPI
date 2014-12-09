from Error import Error
from LogPointSearcher import LogPointSearcher

searcher = LogPointSearcher()


def display_rows(response):
    rows = response.get_rows()
    print

    for row in rows:
        print row

def display_iterative(response):
    print
    i = response.iterate()
    while i.has_next():
        dic =  i.next()
        for key in dic.keys():
            print key, ': ', dic[key]
        print '\n\n'



#print 'Getting LogPoints'
#logpoints = searcher.get_log_points()
#if isinstance(logpoints, Error):
#    print 'Error : ', logpoints.get_error_message()
#else:
#    print '\n\nGetting all allowed logpoints'
#    print '-------------------------------'
#    for logpoint in logpoints:
#        print logpoint
#print '------------------'
#print '\n\n'






#print 'Getting All Allowed Repos'
#print
#repos = searcher.get_repos()
#if isinstance(repos, Error):
#    print 'Error : ', repos.get_error_message()
#else:
#    for repo in repos:
#        print repo
#print '-----------------------'
#print '\n\n'




#print 'Getting Repos From Provided LogPoints'
#print '\n\n\nGetting Repos from ', logpoints[1]
#repos = searcher.get_repos([logpoints[1]])
#
#if isinstance(repos, Error):
#    print 'Error : ', repos.get_error_message()
#else:
#    for repo in repos:
#        print repo
#print '-----------------------'
#print '\n\n'
#



#print 'Getting All Allowed Devices'
#print
#devices = searcher.get_devices()
#if isinstance(devices, Error):
#    print 'Error : ', devices.get_error_message()
#else:
#    for device in devices:
#        print device
#print '-----------------------'
#print '\n\n'


#print 'Getting Devices from Particular LogPoint'
## uncomment line 8 to 10 to make this working
#print 'Getting Repos from ', logpoints[0]
#print
#devices = searcher.get_devices([logpoints[0]])
#if isinstance(devices, Error):
#    print 'Error : ', devices.get_error_message()
#else:
#    for device in devices:
#        print device
#print '-----------------------'
#print '\n\n'




#
#print 'Getting TimeZone'
#time_zone = searcher.get_timezone()
#print 'Getting Logpoint TimeZone'
#if isinstance(time_zone,Error):
#    print time_zone.get_error_message()
#else:
#    print time_zone
#print '-----------------------'
#print '\n\n'





#print 'Query Search from all available LogPoints'
# type = simple
#query = 'error'
# type = chart
#query = "| chart count() as Count, sum(sig_id) as SID by device_ip, source_name"
# type = timechart
#query = "| timechart count() as C, sum(sig_id) as SSID by device_ip, col_type"

#search_job = searcher.search(query)
#
#if isinstance(search_job, Error):
#    print 'Error : ', search_job.get_error_message()
#    exit()
#
#if search_job.has_error():
#    print 'Query has error'
#    print 'Error Message : ',  search_job.get_error()
#else:
#    print
#    print 'Getting response from SearchJob'
#    print
#    response = search_job.get_response()
#    if isinstance(response, Error):
#        print 'Error : ', response.get_error_message()
#        exit()
#
#    display_rows(response)
##    display_iterative(response)
#
#    while not response.is_final():
#        response = search_job.get_response()
#        if isinstance(response, Error):
#            print 'Error : ', response.get_error_message()
#            exit()
#
#        display_rows(response)
##        display_iterative(response)
#print '\n\n'







#print 'Query Search from particular LogPoints'
## uncomment line 8 to 10
#print
## type = simple
#query = 'error'
## type = chart
##query = "| chart count() as Count, sum(sig_id) as SID by device_ip, source_name"
## type = timechart
##query = "| timechart count() as C, sum(sig_id) as SSID by device_ip, col_type"
#repos = logpoints[1].get_repos()
#if isinstance(repos, Error):
#    print 'Error : ', repos.get_error_message()
#    exit()
#
#repos_list = []
#for rep in repos:
#    repos_list.append(rep.get_search_format())
#
#
#print repos_list
#search_job = searcher.search(query, 'Last 30 days', repos_list)
#
#if isinstance(search_job, Error):
#    print 'Error : ', search_job.get_error_message()
#    exit()
#
#if search_job.has_error():
#    print 'Query has error'
#    print 'Error Message : ',  search_job.get_error()
#else:
#    response = search_job.get_response()
#    if isinstance(response, Error):
#        print 'Error : ', response.get_error_message()
#        exit()
#
#    display_rows(response)
##    display_iterative(response)
#
#    while not response.is_final():
#        response = search_job.get_response()
#        print response
#        if isinstance(response, Error):
#            print 'Error : ', response.get_error_message()
#            exit()
#
#        display_rows(response)
##        display_iterative(response)
#print '\n\n'







print 'Getting LiveSearch'
livesearches  = searcher.get_live_searches()
if isinstance(livesearches,Error):
    print livesearches.get_error_message()
else:
    for livesearch in livesearches:
        if not isinstance(livesearch,Error):
            print "\n Livesearch-id[life_id] =>",livesearch.get_id(),"\n" \
            "\n Livesearch-query => ",livesearch.get_query(),"\n" \
            "\n Livesearch-name => ",livesearch.get_name(),"\n"

            response = livesearch.get_response()
            if isinstance(response,Error):
                print "\n\n\nError\t\t\t\t\n\n\n",response.get_error_message(),"\n\n\n\n"
            else:
                rows = response.get_rows()
                print '\n\n'
                print 'Displaying data from list returned from get_rows()'
                print '\n\n'

                for row in rows:
                    print row

                print '\n\n'
                print 'Iterative process for search response'
                print '\n\n'

            i = response.iterate()
            while i.has_next():
                dic =  i.next()
                for key in dic.keys():
                    print key, ': ', dic[key]
                print '\n\n'
        else:
            print livesearch.get_error_message()
print '\n\n'