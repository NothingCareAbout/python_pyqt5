import os
import time
import requests,os
import sys,re,xlwt,urllib.request,urllib.error,sqlite3
from bs4 import BeautifulSoup

def main():
    global find_link
    find_link=re.compile(r'<a href="(.*?)">')
    getData()
    
def askURL(url):
    #url="https://movie.douban.com/top250?start=0"

    headers={"User-Agent" :"Mozilla/5.0"} 
    req=urllib.request.Request(url,headers=headers)#模拟登录
    response=urllib.request.urlopen(req)
    return response

def getData():  
    baseurl="https://movie.douban.com/top250?"
    for index in range(0,1):
        url=baseurl+"start="+str(index*25)
        html=askURL(url)
        data=[]
        soup=BeautifulSoup(html,"html.parser") #解析数据
        for item in soup.find_all('div',class_="item"):
            link=re.findall(find_link,item)[0] #使用正则表达式找到所需东西第一个
            time.sleep(2)
def saveData():
    pass


if __name__ == '__main__':
    main()