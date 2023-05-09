# -*- coding:utf-8 -*-
"""
作者：fc
日期：2023年05月05日
"""
import json
import requests
from access_token import AccessToken
import datetime
from datetime import datetime


class SendMessage(object):
    # 消息接收者
    TOUSER = 'oDCvo5vnQwHKOotNjqdqMudawU8M'
    # 消息模板id
    TEMPLATE_ID = 'MfA5aOWI176n6IKVMbVoNzCKOkvlzDSwT6ADs0z-Pbk'

    def __init__(self, touser=TOUSER, template_id=TEMPLATE_ID) -> None:
        """
        构造函数
        :param touser: 消息接收者
        :param template_id: 消息模板id
        """
        self.access_token = AccessToken().get_access_token()
        self.touser = touser
        self.template_id = template_id

    def get_count_day(self, nowday, brithday):
        if nowday < brithday:
            return (brithday-nowday).days
        else:
            return (datetime(nowday.year+1, brithday.month, brithday.day)-nowday).days

    def get_send_data(self, json_data) -> object:
        """
        获取发送消息data
        :param json_data: json数据对应模板
        :return: 发送的消息体
        """
        return {
            "touser": self.touser,
            "template_id": self.template_id,
            "url": "http://stars.chromeexperiments.com/",
            "topcolor": "#FF0000",
            # json数据对应模板
            "data": {
                "date": {
                    "value": json_data["result"]["date"],
                    # 字体颜色
                    "color": "#FF44AA"
                },
                "week": {
                    "value": json_data["result"]["week"],
                    # 字体颜色
                    "color": "#00FFFF"
                },
                "weather": {
                    "value": json_data["result"]["weather"],
                    "color": "#00FF00"
                },
                "city": {
                    "value": json_data["result"]["area"],
                    "color": "#FF44AA"
                },
                "min_temperature": {
                    "value": json_data["result"]["lowest"],
                    "color": "#2894FF"
                },
                "max_temperature": {
                    "value": json_data["result"]["highest"],
                    "color": "#2894FF"
                },
                "wind": {
                    "value": json_data["result"]["wind"],
                    "color": "#173177"
                },
                "tips": {
                    "value": json_data["result"]["tips"],
                    "color": "#173177"
                },
                "love_day": {
                    "value": (datetime.today()-datetime(2023, 4, 9)).days,
                    "color": "#FF44AA"
                },
                "birthday1": {
                    "value": self.get_count_day(datetime.today(), datetime(datetime.today().year, 7, 5)),
                    "color": "#173177"
                },
                "birthday2": {
                    "value": self.get_count_day(datetime.today(), datetime(datetime.today().year, 1, 17)),
                    "color": "#FF44AA"
                },
            }
        }

    def send_message(self, json_data) -> None:
        """
        发送消息
        :param json_data: json数据
        :return:
        """
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.access_token}"
        data = json.dumps(self.get_send_data(json_data))
        resp = requests.post(url, data=data)
        result = resp.json()
        if result["errcode"] == 0:
            print("消息发送成功")
        else:
            print(result)
