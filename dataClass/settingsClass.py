import json
import sys


class GameSettingsClass:
    _settings = {}

    def __init__(self):
        global _settings

        with open(sys.path[0] + '/client_config.cfg', 'r') as f:
            _settings = json.load(f)

    def getSettings(self):
        return _settings
