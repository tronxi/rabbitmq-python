import json


class Event:

    def __init__(self, datetime, payload=None):
        self.datetime = datetime
        self.payload = payload

    def to_json(self):
        return json.dumps(self.__dict__, default=str)
