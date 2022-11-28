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
        config.add_section('Start')
        config.set('Start', 'first_run', 'true')
        config.add_section('Auth')
        config.set('Auth', 'vk_login', 'none')
        config.set('Auth', 'vk_password', 'none')

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

        # checks if this is the first launch
        if config['Start']['first_run'] == 'true':
            input('wait: configure config.ini and then press Enter')
            config.set('Start', 'first_run', 'false')
            # save changed first_run state
            with open(filename, 'w') as config_file:
                config.write(config_file)
        elif config['Start']['first_run'] == 'false':
            print('info: config.ini is already configured, skipped')
        else:
            print('error: first_run in config.ini has an invalid value, it should be true/false')
            quit(0)

        config.read(filename)

        # return read config
        return config


Main()
