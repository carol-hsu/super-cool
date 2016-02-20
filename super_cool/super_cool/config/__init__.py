import os
import ConfigParser

class ConfigNotFoundError(Exception):
    pass

class ApplicationConfig(object):

    @staticmethod
    def get_config_dir():
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def _get_config(name):
        config = ConfigParser.SafeConfigParser()
        filename = os.path.join(ApplicationConfig.get_config_dir(), name) + '.ini'
        if len(config.read(filename)) == 0:
            raise ConfigNotFoundError("config file not found: %s" % filename)

        #config.read(filename)
        return config

    @staticmethod
    def get_source(type):
        return ApplicationConfig._get_config('location').get('source', type)
