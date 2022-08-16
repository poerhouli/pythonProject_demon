import csv
import random
import re
import time
from urllib import request


class Maoyan:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        self.i = 0

    # 请求
    def get_html(self, url):
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        self.pare_html(html)
        # 解析

    def pare_html(self, html):
        re_dbs = ''
        pattern = re.compile(re_dbs, re.S)
        r_list = pattern.findall(html)
        # 直接调用写入函数
        self.write_html(r_list)

    # 保存
    def write_html(self, r_list):
        item = {}
        with open('maoyan.csv', 'a') as f:
            write = csv.writer(f)
            for r in r_list:
                item['name'] = r[0].strip()
                item['star'] = r[1].strip()
                item['time'] = r[2].strip()[5:15]
                print(item)
                L = [
                    item['name'], item['star'], item['time']
                ]
                write.writerow(L)
                self.i += 1

    # 启动
    def run(self):
        for offset in range(0, 91, 10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1, 3))
        print('数量', self.i)


if __name__ == '__main__':
    spider = Maoyan()


    spider.run()


