import json
import configparser

def read_json_config(path, charset="utf-8"):
    """ read a config """

    with open(path, 'r',encoding=charset) as f:
        config = json.load(f)
        return config

def read_cfg_config(path):
    """read a config"""
    
    config = configparser.ConfigParser()
    config.read(path + "message.cfg")
    return config
