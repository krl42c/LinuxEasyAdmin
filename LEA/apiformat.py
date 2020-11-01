class APIResponse:
    def __init__(self,auth_type,status,response_type=None, response_value=None):
        self.name = "LEA v0.1"
        self.auth_type =  auth_type
        self.status = status
        self.response_type = response_type
        self.response_value = response_value
        

    def toJSON(self):
        return { "Server": self.name, 
                 "Status": self.status,
                 "Auth_type:" : self.auth_type,
                 "Response_type" : self.response_type,
                 "Response_value": self.response_value
               }



