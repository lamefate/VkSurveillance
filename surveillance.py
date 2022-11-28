from json import loads, dumps
import vk_api


class Surveillance:
    def __init__(self, api, params):
        self.api = api
        self.timeout = params['Surveillance']['api_timeout']

    def friends(self):
        pass

    def posts(self):
        pass

    def comments(self):
        pass

    def online(self):
        pass
