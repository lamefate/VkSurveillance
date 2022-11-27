from json import dumps, loads
from random import randint
from time import sleep
from os import path
import configparser
import vk_api


class MainMenu:
    def __init__(self):
        self.config_filename = 'config.ini'
        self.params = self.load_config(self.config_filename)

    def generate_config(self, filename):
        # setting parameters and sections
        config = configparser.ConfigParser()
        config.add_section('Auth')
        config.set('Auth', 'Phone', '+7')
        config.set('Auth', 'Password', 'q')

        # save config to .ini file
        with open(filename, 'w') as config_file:
            config.write(config_file)

    def load_config(self, filename):
        # if config.ini doesn't exist
        if not path.exists(filename) and not path.isfile(filename):
            self.generate_config(filename)

        # read config file
        config = configparser.ConfigParser()
        config.read(filename)

        # return read config
        return config

