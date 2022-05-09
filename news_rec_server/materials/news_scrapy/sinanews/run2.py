import datetime
import time

from scrapy import cmdline
def doSth():
  # 把爬虫程序放在这个类里 zhilian_spider 是爬虫的name
  cmdline.execute('scrapy crawl sina_spider --nolog -a pages=50'.split())

  # cmdline.execute('scrapy crawl zhilian_spider'.split())
# 想几点更新,定时到几点
def time_ti(h=15, m=55):
  while True:
    now = datetime.datetime.now()
    # print(now.hour, now.minute)
    if now.hour == h and now.minute == m:
      print("start")
      doSth()
    # 每隔60秒检测一次
    time.sleep(60)
time_ti()