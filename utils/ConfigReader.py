import os
import configparser

config = configparser.ConfigParser()

path = os.path.abspath(os.getcwd())+"\\configurations\\config.ini"
config.read(path)

class ReadConfig:
    @staticmethod
    def get_property(key):
        return config.get("commonInfo",key)