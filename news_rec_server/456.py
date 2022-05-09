from ecloud import CMSSEcloudNlpClient
import json

accesskey = 'ec8be13a837c48528234ddd1defcee27'
secretkey = 'a017e2600c0046d490ab25273a6cffda'
url = 'https://api-wuxi-1.cmecloud.cn:8443'

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
       # print(response['body'])
       print(response.json())
       return response.json()
   except ValueError as e:
       print(e)
if __name__ == "__main__":
   asd = request_industry()

   a = asd['body']
   b = a['items'][0]
   c = b['industries']
   d = c[0]['labelName']
   print(asd)