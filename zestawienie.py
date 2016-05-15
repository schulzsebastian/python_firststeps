#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Lista telefonow i cen z Euro.com.pl
"""

import urllib
import re

def stworz_zestawienie(link):
    url = link
    html = urllib.urlopen(url).read()
    name = re.findall("\',\'name\':\'(.+?)\'", html)
    price = re.findall("\',\'price\':\'(.+?)\'", html)
    zestawienie = dict()
    for i in range(0,len(name)):
        zestawienie[name[i]]=price[i]
    return zestawienie

if __name__ == '__main__':
    #Telefony LTE i 2gb RAMu
    link = 'http://www.euro.com.pl/telefony-komorkowe,e30,s1,x2,do1000.bhtml'
    zestawienie = stworz_zestawienie(link)
    for i in sorted(zestawienie, key = zestawienie.get, reverse = False):
        print i, zestawienie[i]