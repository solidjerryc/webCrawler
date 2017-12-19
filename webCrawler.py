# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 13:56:45 2017

@author: JerryC
"""

import urllib2
from StringIO import StringIO
import gzip
import requests

headers={
         'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
         'accept-encoding':'gzip, deflate, br',
         'accept-language':'zh-CN,zh;q=0.8',
         'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
         }

def use_requests(url,headers=headers):
    request=requests.get(url,headers=headers)
    request.raise_for_status()
    return request.text
    
def use_requests_proxy(url,proxy,headers=headers):
    request=requests.get(url,headers=headers,proxies=proxy,timeout=1)
    request.raise_for_status()
    return request.text

def getHTML(url):
    response = urllib2.urlopen(url)
    return response.read()
    
def decode_gzip(comp):#解压gzip
    buf=StringIO(comp)
    decompressed=gzip.GzipFile(fileobj=buf)
    return decompressed.read()
    
def getHTML_Headers(url,headers):
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    ret_html=response.read()
    if response.info().get('Content-Encoding')=='gzip':
        ret_html=decode_gzip(ret_html)
    return ret_html


def HTML(url,headers=headers):
    return getHTML_Headers(url=url,headers=headers)