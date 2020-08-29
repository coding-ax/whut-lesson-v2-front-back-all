#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 23:27
# @Author  : AX
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

import requests
import re
from bs4 import BeautifulSoup
import hashlib
from lxml import etree

'''
@:param:username password
@:return data:[{
    class:
    start:
    end:
    place:
    time:
    where:
}]
'''


def req(username, password):
    # 预处理武汉理工大学登陆数据
    # 编码(根据js得知加密源码格式）
    username1 = hashlib.md5(bytes(username.encode("utf-8")))
    username1 = username1.hexdigest()
    temp = username + password
    password1 = hashlib.sha1(bytes(temp.encode("utf-8")))
    password1 = password1.hexdigest()
    print(username1, password1)
    # 根据webfinger获取code
    code = requests.post(url="http://sso.jwc.whut.edu.cn/Certification/getCode.do", data={
        "webfinger": "bea9b70bfc62874bfeda5e0fe4b26923"
    })
    print(code.text)
    # 设置params
    data = {
        "MsgID": "",
        "KeyID": "",
        "UserName": "",
        "Password": "",
        "rnd": 64183,
        "return_EncData": "",
        "code": code,
        "userName1": username1,
        "password1": password1,
        "webfinger": "bea9b70bfc62874bfeda5e0fe4b26923",
        "type": "xs",
        "userName": username,
        "password": password,
    }
    # url切换
    url = "http://sso.jwc.whut.edu.cn/Certification/login.do"
    # 伪装为浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    }
    # 发起请求
    session = requests.Session()
    session.get(headers=headers, url=url)
    html = session.post(url=url, headers=headers, params=data).text
    # 解析数据
    data = []
    tree = etree.HTML(html)
    # 获取到总表格
    tables = tree.xpath('//tbody[contains(@class,"table-class-even")]')[0]
    # 解析trs
    trs = tables.xpath('./tr')
    # 利用count标记位置
    count = 0
    for tr in trs:
        # 解析每个td 并去掉那两个 上午 第一节
        tds = tr.xpath('./td[contains(@style,"text-align: center")]')
        for td in tds:
            # 标记位置
            count = count + 1
            divs = td.xpath('./div')
            if len(divs) != 0:
                for div in divs:
                    texts = div.xpath('./a//text()')
                    time = re.findall('\((.*?)\)', texts[3])[0]
                    week = re.findall('(第(.*?)周)', texts[3])[0]
                    # print(week)
                    # print(time)
                    data.append({
                        'lesson-name': texts[0].strip(),
                        'place': texts[1].strip(),
                        'week_num': week[1],
                        'week_desc': week[0],
                        'time_num': time[:-1],
                        'time_desc': time,
                        'count': count
                    })
                    # print(count)
    return data


# if __name__ == "__main__":
#     req('0121810870217', 'xgpax.top/React123')
