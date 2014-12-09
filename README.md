SearchAPI
=========
REST api to fetch search logs from LogInspect

Edit "search.conf" file and enter LogInspect IP address, request_type(http ot https), username created in LogInspect and user's secret key as seen at the bottom of the user preference page.

Then run: python search.py

The search queries, result limit, time_range and repos to search for can be edited in search.py

SEARCH_TIME_RANGE examples:
===========================

Last x minute(s), hour(s), day(s), month(s), year(s)

2012/08/12 00:00:00 To 2012/08/14 00:00:00

2012/08/12 12:00:00 AM To 2012/08/13 12:00:00 PM

SEARCH_REPOS examples:
======================

[] -> allowed repos for user

['127.0.0.1:5504'] -> all local LogInspect repos

['127.0.0.1:5504/default'] -> particular repos
