
#coding:utf-8
import urllib2

try:
    urllib2.urlopen("http://baidu.com", timeout=2)
    print ("可以上网")

except urllib2.URLError:
    print ("不可以上网")
