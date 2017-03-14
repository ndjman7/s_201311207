#-*- coding: utf-8 -*-
d = dict()
f=open('tmp.txt')
for e in f.readlines():
    for w in e.split(): 
        if w not in d:
            d[w]=1
        else:
            d[w]=d[w]+1
f.close()
print "키-키값",d 
print "저장된 문자의 갯수 (중복을 빼고)", len(d)
print "키: ",d.keys()
print "키값:", d.values()