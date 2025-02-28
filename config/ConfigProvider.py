import configparser

global_config = configparser.ConfigParser()
global_config.read('global_options.ini')


class ConfigProvider:
    def __init__(self):
        self.config = global_config

    def get(self, section: str, prop: str):
        return self.config.get(section, prop)
