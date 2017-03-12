from configparser import ConfigParser
from aw_core.config import load_config

default_settings = {
    "timeout": 180,
    "update_interval": 30,
    "check_interval": 5,
}
default_testing_settings = {
    "timeout": 20,
    "update_interval": 5,
    "check_interval": 1,
}

default_config = ConfigParser()
default_config['aw-watcher-afk'] = default_settings
default_config['aw-watcher-afk-testing'] = default_testing_settings
watcher_config = load_config("aw-watcher-afk", default_config)
