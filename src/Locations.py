import requests
from datetime import datetime


def pull_request(url):
    response = requests.get(url=url).json()
    return response


class Location:
    def __init__(self, filters):
        viable_parameters = ['occurred_before', 'occurred_after', 'incident_type', 'proximity',
                             'proximity_square', 'query', 'limit', 'all']
        url = 'https://bikewise.org:443/api/v2/locations?'
        filters_url = ''
        for key in filters:
            if key not in viable_parameters:
                self.response = None
                return None
            filters_url += str(filter)+'='+str(filters[key])+'&'
        filters_url = filters_url[:-1]
        self.response = pull_request(url+filters_url)

    def get_coordinates(self):
        coordinates = []
        if self.response is None:
            return coordinates

        for i in self.response['features']:
            if(i["geometry"]["coordinates"]) is not None:
                coordinates.append(i["geometry"]["coordinates"])
        return coordinates

    def get_dates(self):
        dates = []
        if self.response is None:
            return dates

        for i in self.response['features']:
            if(i["properties"]['occurred_at']) is not None:
                dates.append(datetime.fromtimestamp(i["properties"]['occurred_at']).strftime('%d/%m/%y %H:%M:%S'))
        return dates
