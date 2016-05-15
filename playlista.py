#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Tworzenie playlisty z tagu na Wykopie
"""

import urllib
import re

def stworz_playliste(tag):
    url = 'http://www.wykop.pl/tag/' + tag
    html = urllib.urlopen(url).read()
    links = re.findall('href="https://www.youtube.com/watch\?v=([a-zA-Z0-9]+)"', html)
    powtorki = []
    lista_utworow = ""
    for link in links:
        if link in powtorki: continue
        powtorki.append(link)
        lista_utworow  = lista_utworow  + link + ","
    playlista = 'http://www.youtube.com/watch_videos?video_ids=' + lista_utworow
    return playlista

if __name__ == '__main__':
    tag = raw_input('Podaj nazwe tagu do stworzenia playlisty z Wykopu: ')
    print stworz_playliste(tag)
