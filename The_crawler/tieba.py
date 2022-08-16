from urllib import request, parse
import random
import time
from The_crawler import userager
class TieBa:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    #获取响应内容
    def get_con(self, url):
        # headers = {'User-Agent':random.choice(user_agent_list_1)}
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        return html
    #解析提取数据
    def pase_page(self):
        pass
    def write_page(self,filname,html):
        with open(filname, 'w', encoding='utf-8') as f:
            f.write(html)
    def run(self):
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        kw = parse.quote(name)
        for i in range(start, end+1):
            pn = (i-1)*50
            url = self.url.format(kw, pn)
            html = self.get_con(url)
            filename = '{}-第{}页.html'.format(name, i)
            self.write_page(filename, html)
            print('第%d页抓取成功' % i)
            # 每爬取1个页面随机休眠1-3秒
            time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    bengin = time.time()
    p = TieBa()
    p.run()
    stop = time.time()
    print('执行时间: %.2f' % (stop-bengin))