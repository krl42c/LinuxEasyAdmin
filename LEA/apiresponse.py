import json

class APIResponse:
    def __init__(self):
        self.json_response = {}

    def insert_value(self,key,value):
        self.json_response[key] = value 

    def get_json_response(self):
        return self.json_response
