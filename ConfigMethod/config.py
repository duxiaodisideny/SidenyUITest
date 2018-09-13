import os
from Utils.File_reader import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH,'ConfigMethod','configdr.yml')
DATA_PATH = os.path.join(BASE_PATH,'Data')
DRIVER_PATH = os.path.join(BASE_PATH,'Drivers')
LOG_PATH = os.path.join(BASE_PATH,'Log')
REPORT_PATH = os.path.join(BASE_PATH,'Report')
print(REPORT_PATH)



class ConfigMethod:
    def __init__(self,config1=CONFIG_FILE):
        self.config = YamlReader(config1).data

    def get(self,element,index=0):
        return self.config[index].get(element)
