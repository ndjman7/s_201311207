# -*-coding: utf-8-*-
import lxml.html
import requests

from lxml.cssselect import CSSSelector

keyword='빅뱅'
r = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
_html = lxml.html.fromstring(r.text)
sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
nodes = sel(_html)
_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
print u"{:30} {:10} {:20} {:10} {:20}\n".format('Music title','---','Artist','---','Album')
for node in nodes:
    _name=_selName(node)
    _artist=_selArtist(node)
    _album=_selAlbum(node)
    if _name:
        print u"{:30}".format(_name[0].text_content()),
        print "{:10}".format("---"),
        print u"{:20}".format(_artist[0].text_content().strip()),
        print "{:10}".format("---"),
        print u"{:20}".format(_album[0].text_content())