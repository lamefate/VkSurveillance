from auth import Auth
from os import path
import configparser


class Main:
    def __init__(self):
        self.config_filename = 'config.ini'
        self.params = self.load_config(self.config_filename)
        self.auth_process = Auth(self.params)

    def generate_config(self, filename):
        # setting parameters and sections
        config = configparser.ConfigParser()
        config.add_section('Auth')
        config.set('Auth', 'phone', '+7')
        config.set('Auth', 'password', 'q')

        # save config to .ini file
        with open(filename, 'w') as config_file:
            config.write(config_file)

        print('info: config.ini created')

    def load_config(self, filename):
        # if config.ini doesn't exist
        if not path.exists(filename) and not path.isfile(filename):
            print('info: config.ini does not exist, creating...')
            self.generate_config(filename)

        print('info: loading config.ini params')
        # read config file
        config = configparser.ConfigParser()
        config.read(filename)

        # return read config
        return config


Main()
