#!/usr/bin/env python
# coding: utf-8

import os
import requests
import mylib

def quiz5():
    _url='http://openAPI.seoul.go.kr:8088'
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    _key=str(key['dataseoul'])
    _type='json'
    _service='CardSubwayStatisticsService'
    _start_index=1
    _end_index=5
    _use_mon='201501'
    for index in range(12):
        _use_mon='201501'
        _use_mon = str(int(_use_mon) + index)
        _api=os.path.join(_url,_key,_type,_service,
                          str(_start_index),str(_end_index),_use_mon)
        response = requests.get(_api).text
        print response
    
if __name__ == '__main__':
    quiz5()