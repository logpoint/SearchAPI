__author__="bunkdeath"
__date__ ="$Jan 2, 2013 3:17:18 PM$"

from Rows import Rows

class Response:

    def __init__(self, response_string):
        """
        takes string response from search query

        determines the types of search query(simple, chart, timechart)

        parse response rows accordingly
        """
        # extracted from chart
        self._status = ''
        self._original_search_id = ''
        self._total_count = ''
        self._raw_row = ''
        self._extra_fields = []
        self._time_range = []
        self._elapsed_time = ''
        self._version = ''
        self._grouping = []
        self._final = False
        self._columns = []
        self._aliases = []

        # extracted from simple search query
        self._next_starts = ''
        self._fields = ''


        # values except in response
        self._index = 0
        self._count = 0
        self._rows = []


        self.response_string = response_string
        self.data = {}
        type = self.response_string.get('query_type')
        if (type == "search"):
            self._parse_search_type()
            self._parse_simple_rows_data()

        if(type == "chart"):
            self._parse_chart_timechart_type()
            self._parse_chart_rows_data()

        if(type == "timechart"):
            self._parse_chart_timechart_type()
            self._parse_timechart_rows_data()


    def is_final(self):
        return self._final

    def get_version(self):
        return self._version

    
    def get_rows(self):
        '''
        when this method is called, it returns the
        Rows object that hold
            """
            get rows iteratively
            get complete data at once
            """
        '''
        return self._rows

    def get_raw_rows(self):
        '''
        this method upon called, returns raw row data that was
        returned in response as it is
        '''
        return self._raw_row


    def iterate(self):
        '''
        this method creates iterative way of accessing rows data
        '''
        rows = Rows(self._rows)
        return rows



    def _parse_search_type(self):
        '''
        this method is specially created to parse response rows
        according to type simple search
        '''
        response_string = self.response_string
        self._status = response_string.get('status')
        self._original_search_id = response_string.get('orig_search_id')
        self._total_count = response_string.get('estim_count')
        self._raw_row = response_string.get('rows')
        self._fields = response_string.get('fields')
        self._time_range = response_string.get('time_range')
        self._elapsed_time = response_string.get('elapsed_seconds')
        self._version = response_string.get('version')
        self._next_starts = response_string.get('next_starts')
        self._final = response_string.get('final')



    def _parse_chart_timechart_type(self):
        '''
        this method is specially created to parse response rows
        according to type chart and timechart.
        '''
        response_string = self.response_string
        self._status = response_string.get('status')
        self._original_search_id = response_string.get('orig_search_id')
        self._total_count = response_string.get('num_aggregated')
        self._raw_row = response_string.get('rows')
        self._extra_fields = response_string.get('extra_fields')
        self._time_range = response_string.get('time_range')
        self._elapsed_time = response_string.get('elapsed_seconds')
        self._version = response_string.get('version')
        self._grouping = response_string.get('grouping')
        self._final = response_string.get('final')
        self._columns = response_string.get('columns')
        self._aliases = response_string.get('aliases', [])


    def _parse_simple_rows_data(self):
        '''
        parse rows data and put it in list

        create list of normalized dictionary

        grouped data are parsed and put into dictionary according
        to group key name
        '''
        for row in self._raw_row:
            self._rows.append(row)


    def _parse_chart_rows_data(self):
        '''
        parse rows data and put it in list

        create list of normalized dictionary

        grouped data are parsed and put into dictionary according
        to group key name
        '''
        aliases = self._aliases
        group_index = self._find_grouping_index('group', aliases)
        grouping = self._grouping
        if group_index == -1:
            self._rows = self._raw_row
            return
        for row in self._raw_row:
            self._count += 1
            row_data = {}
            i = 0
            for item in row:
                if group_index == i:
                    j = 0
                    group_data = {}
                    for group in grouping:
                        group_data[group] = item[j]
                        j += 1

                    row_data[aliases[i]] = group_data
                else:
                    row_data[aliases[i]] = item
                i += 1

            self._rows.append(row_data)


    def _parse_timechart_rows_data(self):
        '''
        parse rows data of timechart type and put it in list

        create list of normalized dictionary

        grouped data are parsed and put into dictionary according
        to group key name
        '''

        aliases = self._aliases
        group_index = self._find_grouping_index('group', aliases)
        grouping = self._grouping

        for row in self._raw_row:
            self._count += 1
            row_data = {}
            i = 0
            for item in row:
                if group_index == i:
                    j = 1
                    group_data = {}
                    for itm in item:
                        group_data[grouping[j]] = itm
                        j += 1

                    row_data[aliases[i]] = group_data
                else:
                    row_data[aliases[i]] = item
                i += 1

            self._rows.append(row_data)
            

    def _find_grouping_index(self, key, list):
        '''
        this method finds the index of grouped index from response rows

        help in creating dictionary for grouped data
        '''
        index = 0
        for item in list:
            if item == key:
                return index
            index += 1

        return -1