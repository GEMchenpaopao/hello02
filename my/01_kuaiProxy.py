"""
create database proxydb charset utf8;
use proxydb;
create table proxytab(
ip varchar(50),
port varchar(10)
)charset=utf8;
"""

import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
import pymysql

class KuaiProxy:
    def __init__(self):
        self.url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.test_url = 'http://httpbin.org/get'
        self.headers = {'User-Agent':UserAgent().random}
        self.db = pymysql.connect('localhost', 'root', '123456', 'proxydb', charset='utf8')
        self.cur = self.db.cursor()

    def get_proxy(self, url):
        html = requests.get(url=url, headers=self.headers).text
        # 解析提取数据
        # 依次测试每个代理IP是否可用,能用的保存到数据库表中
        # 不能用的不做任何处理
        eobj = etree.HTML(html)
        tr_list=eobj.xpath('//table/tbody/tr')
        for tr in tr_list:
            ip=tr.xpath('./td[1]/text()')[0]
            port = tr.xpath('./td[2]/text()')[0]
            self.test_proxy(ip,port)
    def test_proxy(self,ip,port):
        proxies={
            'http':'http://{}:{}'.format(ip,port),
            'https':'http://{}:{}'.format(ip,port)
        }