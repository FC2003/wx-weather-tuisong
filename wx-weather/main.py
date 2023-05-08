# -*- coding:utf-8 -*-
"""
作者：fc
日期：2023年05月05日
"""
from send_message import SendMessage
import http.client
import urllib
import json


class Main(object):
    def __init__(self) -> None:
        """
        构造函数
        """
        pass

    def main(self) -> None:
        # 实例SendMessage
        sm = SendMessage()
        conn = http.client.HTTPSConnection('apis.tianapi.com')  # 接口域名
        params = urllib.parse.urlencode({'key': '8fcf6b4c04cc339690ca9df5d441eb53', 'city': '101250101', 'type': '1'})
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        conn.request('POST', '/tianqi/index', params, headers)
        tianapi = conn.getresponse()
        result = tianapi.read()
        data = result.decode('utf-8')
        dict_data = json.loads(data)
        sm.send_message(json_data=dict_data)
        print(dict_data)
        # 发送消息


if __name__ == '__main__':
    main = Main()
    main.main()
