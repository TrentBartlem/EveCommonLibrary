import xml.etree.ElementTree as ET
import time
import requests


class BaseAPIConnector(object):
    def __init__(self, user_agent='', verbose=False):

        self.user_agent = user_agent
        self.verbose = verbose

    def construct_url(self):
        return None

    def html_request(self):
        if self.user_agent == '':
            raise UserWarning('Please specify a user agent.')

        url = self.construct_url()
        if self.verbose:
            print(url)

        request = None
        exception_count = 0
        while exception_count < 10:
            try:
                request = requests.get(url, headers={'User-Agent': self.user_agent})
            except Exception as e:
                print("Exception '%s' while querying url: '%s', trying again..." % (e, url))
                time.sleep(10)
                exception_count += 1
            else:
                break

        return request

    def get_xml_from_url(self):
        try:
            return ET.fromstring(self.html_request().text)
        except:
            return None

    def get_json_from_url(self):
        return self.html_request().json()