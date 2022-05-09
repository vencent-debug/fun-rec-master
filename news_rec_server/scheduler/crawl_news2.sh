#!/bin/bash
. /etc/profile

# python 环境需要换成自己的虚拟环境中的Python
python=python3
home_path=/usr/local

news_recsys_path=${home_path}"/news_recsys/news_rec_server"

# 得跳转到这个目录才能执行下面爬虫的命令
cd ${news_recsys_path}/materials/news_scrapy

# 系统正式运行的时候需要修改pages的值
pages=30
min_news_num=1000

echo "$(date -d today +%Y-%m-%d-%H-%M-%S)"
# 爬虫
${python} ${news_recsys_path}/materials/news_scrapy/sinanews/run.py  --pages=${pages}
if [ $? -eq 0 ]; then
    echo "scrapy crawl sina_spider --pages ${page} success."
else   
    echo "scrapy crawl sina_spider --pages ${page} fail."
fi


${python} ${news_recsys_path}/materials/news_scrapy/renmingwang/scarpy2.py  --pages=${pages}
if [ $? -eq 0 ]; then
    echo "scrapy renmingwang/scarpy2.py success."
else
    echo "scrapy renmingwang/scarpy2.py fail."
fi
