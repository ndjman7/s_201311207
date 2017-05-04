#!/usr/bin/env python
# coding: utf-8
import os
import requests
import mylib

def doIt():
    _url='http://openAPI.seoul.go.kr:8088'
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    _key=key['dataseoul']
    _type='json'
    _service='CardSubwayStatisticsService'
    _start_index=1
    _end_index=5
    _maxIter=2
    _iter=0
    while _iter<_maxIter:
        for index in range(12):
            _use_mon='201301'
            _use_mon = str(int(_use_mon) + index)
            _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
            response = requests.get(_api).text
            print response
        _start_index+=5
        _end_index+=5
        _iter+=1
if __name__ == "__main__":
    doIt()