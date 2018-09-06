import os
from Utils.File_reader import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print(BASE_PATH)
CONFIG_FILE = os.path.join(BASE_PATH,'Config','config.yml')
print(CONFIG_FILE)
DATA_PATH = os.path.join(BASE_PATH,'Data')
print(DATA_PATH)
DRIVER_PATH = os.path.join(BASE_PATH,'Drivers')
print(DRIVER_PATH)
LOG_PATH = os.path.join(BASE_PATH,'Log')
print(LOG_PATH)
REPORT_PATH = os.path.join(BASE_PATH,'Report')
print(REPORT_PATH)


class ConfigMethod:
    def __init__(self,config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self,element,index=0):
        return self.config[index].get(element)
