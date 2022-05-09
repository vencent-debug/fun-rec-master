from ecloud import CMSSEcloudNlpClient

accesskey = 'your_ak'
secretkey = 'your_sk'
url = 'https://api-wuxi-1.cmecloud.cn:8443'


# 1-1 sentiment for weibo
def request_sentiment_wb():
    requesturl = '/api/nlp/v1/sentiment/wb'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 1-2 sentiment for news
def request_sentiment_news():
    requesturl = '/api/nlp/v1/sentiment/news'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    params['title'] = '天气说明'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 1-3 sentiment for forum
def request_sentiment_forum():
    requesturl = '/api/nlp/v1/sentiment/forum'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    params['title'] = '天气说明'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)


# 1-4 sentiment for negative judgement
def request_sentiment_genative():
    requesturl = '/api/nlp/v1/sentiment/negative'
    params = {}
    params['textId'] = '123'
    params['content'] = '今天天气不错'
    params['title'] = '天气说明'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 2-1 segmentation
def request_segmentation():
    requesturl = '/api/nlp/v1/segmentation'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 3-1 keywords
def request_keyswords():
    requesturl = '/api/nlp/v1/keywords'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    params['initial'] = 'words'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 4-1 convert doc
def request_convertdoc():
    requesturl = "/api/nlp/v1/convertdoc"
    params = {}
    # use your own file name here
    params['auditFile'] = open('C:\\Users\\CMSS\\Desktop\\extract.pdf','rb')
    file_path = 'C:\\Users\\CMSS\\Desktop\\extract.pdf'
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, file_path)
        if response is not None:
            print(response.text)
    except ValueError as e:
        print(e)

# 4-2 announcement
def request_announcement():
    requesturl = '/api/nlp/v1/announcement-ie'
    params = {}
    params['textId'] = '123'
    params['htmlText'] = '招标人：中国移动'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 4-3 summary
def request_summary():
    requesturl = '/api/nlp/v1/summary'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    params['count'] = 3
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 4-4 comment mining
def request_comment_mining():
    requesturl = '/api/nlp/v1/comment-mining'
    params = {}
    params['textId'] = '123'
    params['textlist'] = ['今天天气不错','今天天气很差']
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-1 industry
def request_industry():
    requesturl = '/api/nlp/v1/industry'
    params = {}
    params['textId'] = '123'
    params['content'] = '乔丹退役'
    params['title'] = '篮球巨星乔丹选择退役'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-2 filter
def request_filter():
    requesturl = '/api/nlp/v1/filter'
    params = {}
    params['textId'] = '123'
    params['content'] = '今天天气不错'
    params['title'] = '天气说明'
    params['type'] = 'bbs'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-3 viewpiont
def request_viewpoint():
    requesturl = '/api/nlp/v1/viewpoint'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-4 rumor
def request_rumor():
    requesturl = '/api/nlp/v1/rumor'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-5 text similarity
def request_text_similarity():
    requesturl = '/api/nlp/v1/text-similarity'
    params = {}
    params['textId'] = '123'
    params['source'] = '北京是中国的首都'
    params['target'] = '中国的首都是北京'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 5-6 theme matcher
def request_theme_matcher():
    requesturl = '/api/nlp/v1/theme-matcher'
    params = {}
    params['textId'] = '123'
    params['content'] = '今天天气不错'
    params['title'] = '天气说明'
    params['keyString'] = "天气"
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 6-1 emotion recognize
def request_emotion():
    requesturl = '/api/nlp/v1/emotion'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 6-2 weibo emotion recognize
def request_wbemotion():
    requesturl = '/api/nlp/v1/wbemotion'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 7-1 named entity recoginize
def request_entity():
    requesturl = '/api/nlp/v1/entity'
    params = {}
    params['textId'] = '123'
    params['text'] = '今天天气不错'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 7-2 location entity recognize
def request_location():
    requesturl = '/api/nlp/v1/location'
    params = {}
    params['textId'] = '123'
    params['content'] = '北京是中国的首都城市'
    params['title'] = '北京'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

# 7-3 transmit
def request_transmit():
    requesturl = '/api/nlp/v1/transmit'
    params = {}
    params['textId'] = '123'
    params['text'] = '甘肃张掖网讯（张掖日报融媒体记者 杨静文,10月26日,市人大常委会党组书记王海峰在甘州区检查督导疫情防控工作'
    items = {}
    items['items'] = [params]
    try:
        nlp_client = CMSSEcloudNlpClient(accesskey, secretkey, url)
        response = nlp_client.request_nlp_service(requesturl, items)
        print(response.text)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    request_sentiment_wb()
    request_sentiment_forum()
    request_sentiment_news()
    request_sentiment_genative()

    request_segmentation()

    request_keyswords()

    request_announcement()
    #request_convertdoc()

    request_industry()
    request_filter()
    request_viewpoint()
    request_rumor()
    request_text_similarity()
    request_theme_matcher()

    request_emotion()
    request_wbemotion()

    request_entity()
    request_location()
    request_transmit()