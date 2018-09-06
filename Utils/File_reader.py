import yaml
import os


class YamlReader:

    def __init__(self,yamlf):

        if os.path.exists(yaml):
            self.yamlf = yamlf

        else:
            raise FileExistsError('文档不存在')
        self._data = None

    @property
    def data(self):

        if not self._data:
            with open(self.yamlf,'rb') as f:
                self._data = list(yaml.safe_load_all(f))
                print(self._data)
        return self._data