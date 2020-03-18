import requests


def pull_request(url):
    response = requests.get(url=url).json()
    return response


class Incident:
    def __init__(self, filters):
        viable_parameters = ['page', 'per_page', 'occurred_before', 'occurred_after',
                             'incident_type', 'proximity', 'proximity_square', 'query']
        url = 'https://bikewise.org:443/api/v2/incidents?'
        filters_url = ''
        for key in filters:
            if key not in viable_parameters:
                self.response = None
                return None
            filters_url += str(filter)+'='+str(filters[key])+'&'
        filters_url = filters_url[:-1]
        self.response = pull_request(url+filters_url)

    def get_image_urls(self):
        image_urls = []
        if self.response is None:
            return image_urls

        for i in self.response['incidents']:
            if(i["media"]["image_url"]) is not None:
                image_urls.append(i["media"]["image_url"])
        return image_urls

    def get_titles(self):
        titles = []
        if self.response is None:
            return titles

        for i in self.response['incidents']:
            if(i["title"]) is not None:
                titles.append(i["title"])
        return titles
