#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Lista telefonow i cen z Euro.com.pl i z Saturn.pl (do pliku)
"""

import urllib
import re

def stworz_zestawienie_euro(link_euro):
    url = link_euro
    html = urllib.urlopen(url).read()
    name = re.findall("\',\'name\':\'(.+?)\'", html)
    price = re.findall("\',\'price\':\'(.+?)\'", html)
    zestawienie = dict()
    for i in range(0,len(name)):
        zestawienie[name[i]]=price[i]
    return zestawienie

def stworz_zestawienie_saturn(link_saturn):
    url = link_saturn
    html = urllib.urlopen(url).read()
    name = re.findall("alt=\"Smartfon (.+?)\"", html)
    price = re.findall("<div class=\"clearfix priceContainer\">\s*(.*)\.", html)
    zestawienie = dict()
    for i in range(0,len(name)):
        zestawienie[name[i]]=price[i]+'.00'
    return zestawienie

if __name__ == '__main__':
    plik = open('zestawienie.txt', 'w')
    #Telefony LTE i 2gb RAMu do 1000PLN
    link_euro = 'http://www.euro.com.pl/telefony-komorkowe,e30,s1,x2,do1000.bhtml'
    #Telefony LTE i ponad 5 cali do 1000PLN
    link_saturn = 'http://www.saturn.pl/poznan-pestka/telefony-i-smartfony_smartfony?query=&os=&outlet=&id_listy=&kat_id=669&id_dostepnosc=&cena_od=&cena_do=1000&cena_od=&cena_do=1000&filter%5B8370%5D%5B789391%5D=5+-+5.9&filter%5B8448%5D%5B818729%5D=LTE'
    zestawienie_euro = stworz_zestawienie_euro(link_euro)
    zestawienie_saturn = stworz_zestawienie_saturn(link_saturn)
    plik.write('--------------------\n')
    plik.write('Euro.com.pl:\n')
    for i in sorted(zestawienie_euro, key = zestawienie_euro.get, reverse = False):
        plik.write(i+' '+zestawienie_euro[i]+'\n')
    plik.write('--------------------\n')
    plik.write('Saturn.pl:\n')
    for i in sorted(zestawienie_saturn, key = zestawienie_saturn.get, reverse = False):
        plik.write(i+' '+zestawienie_saturn[i]+'\n')
    plik.write('--------------------\n')
    plik.close()



