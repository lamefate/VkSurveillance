from json import loads, dumps
import vk_api


class Surveillance:
    def __init__(self, api, params):
        self.api = api

