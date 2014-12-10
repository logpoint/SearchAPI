SearchAPI
=========
REST api to fetch search logs from LogPoint

Edit "Config.py" file and enter logpoint's IP address, request_type(http ot https), username created in logpoint and user's secret key as seen under My Preferences -> Misc.

Then run: python main.py

The search queries, result limit, time_range and repos to search for can be edited in LogPointSearcher.py

<b>SEARCH_TIME_RANGE examples:</b>

Last x minute(s), hour(s), day(s), month(s), year(s)

2012/08/12 00:00:00 To 2012/08/14 00:00:00

2012/08/12 12:00:00 AM To 2012/08/13 12:00:00 PM

Last 4 hours

<b>SEARCH_REPOS examples:</b>

[] -> allowed repos for user

['127.0.0.1:5504'] -> all local LogInspect repos

['127.0.0.1:5504/default'] -> particular repos
