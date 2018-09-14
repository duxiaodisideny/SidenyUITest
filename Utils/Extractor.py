"""
    数据抽取器，对于传递的数据进行一个简单的数据抽取
"""
import json
import jmespath


class JMESPathExtractor(object):
    """
    用JMESPath实现抽取器，对于json格式的数据实现简单方式的抽取。
    """
    def extract(self, query=None, body=None):
        try:
            return jmespath.search(query, json.loads(body))
        except Exception as e:
            raise ValueError("Invalid query: " + query + " : " + str(e))


if __name__ == '__main__':
    from Utils.Client import HTTPclient
    res = HTTPclient(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101010100').send()
    print(res.text)

    j = JMESPathExtractor()
    j_1 = j.extract(query='data.forecast[1].date', body=res.text)
    j_2 = j.extract(query='data.ganmao', body=res.text)
    print(j_1, j_2)