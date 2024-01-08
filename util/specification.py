import json
import os
import configparser

# def read_json_config(path, charset="utf-8"):
#     """ read a config """
#     spec = "spec.json" if specarg == None else specarg
#     spec_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", spec)
#     with open(spec_path, 'r',encoding=charset) as f:
#         config = json.load(f)
#         return config
    
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
