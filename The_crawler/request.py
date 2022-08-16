# import urllib.request
#
# import requests
#
# response = urllib.request.urlopen('http://www.baidu.com/')
# #1.html为字符串
# html = response.read().decode()
# print(html)

'''
        字符串拼接
'''
import time
from urllib import parse
from urllib import request


def get_url(word):
    baseurl = 'http://baidu.com/s?'
    paeams = parse.urlencode({'wd': word})
    url = baseurl + paeams
    return url


# i请求+保存
def write_html(url, word):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    # 拿到相应内容
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    # 保存本地文件
    filename = word + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    word = input('请输入要搜索的内容:')
    url = get_url(word)
    while True:
        try:
            write_html(url, word)
            break
        except Exception as e:
            time.sleep(2)
