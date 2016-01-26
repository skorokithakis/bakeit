try:
    from urllib.request import urlopen, Request, HTTPError
except ImportError:
    from urllib2 import urlopen, Request, HTTPError
import json


class PasteryUploader():
    def __init__(self, api_key):
        """
        Initialize an Uploader instance with the given API key.
        """
        self.api_key = api_key

    def upload(self, body, title="", language=None, duration=None, max_views=0):
        """
        Upload the given body with the specified language type.
        """
        pass

        url = "https://www.pastery.net/api/paste/?api_key=%s" % self.api_key
        if title:
            url += "&title=%s" % title
        if language:
            url += "&language=%s" % language
        if duration:
            url += "&duration=%s" % duration
        if max_views:
            url += "&max_views=%s" % max_views

        req = Request(url, data=bytes(body), headers={'User-Agent': 'Mozilla/5.0 (Python) bakeit library'})
        try:
            response = urlopen(req)
        except HTTPError as e:
            response = json.loads(e.read())
            raise Exception(response["error_msg"])
        response = json.loads(response.read())
        return response["url"]
