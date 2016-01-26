import requests


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
        params = {"api_key": self.api_key}
        if title:
            params["title"] = title
        if language:
            params["language"] = language
        if duration:
            params["duration"] = duration
        if max_views:
            params["max_views"] = max_views

        response = requests.post(
            "https://www.pastery.net/api/paste/",
            files={"file": body},
            params=params,
            headers={'User-Agent': u'Mozilla/5.0 (Python) bakeit library'},
        )
        if 500 <= response.status_code < 600:
            raise RuntimeError("There was a server error, please try again later.")
        else:
            rd = response.json()
            if rd.get("result") == "error":
                raise RuntimeError(rd["error_msg"])

        return rd["url"]
