import yaml
import os


class YamlReader:

    def __init__(self,yamlf):

        if os.path.exists(yamlf):
            self.yamlf = yamlf

        else:
            raise FileExistsError('文档不存在')
        self._data = None

    @property
    def data(self):

        if not self._data:
            with open(self.yamlf,'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data