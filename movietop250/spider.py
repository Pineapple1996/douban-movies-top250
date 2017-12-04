import requests
import re
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time

def gethtml(url):
    '''
    获取网页源代码
    :param url:
    :return:
    '''
    response = requests.get(url)
    # print (response.content)
    html = response.content
    html=html.decode('utf-8')
    return html

def htmlparse(html):
    '''
    解析网页，使用正则表达式匹配需要的内容
    :param html:
    :return:
    '''
    soup = BeautifulSoup(html,"lxml")
    # for item in soup.find_all('div',class_='item'):
    pattern = re.compile(r'<em class="">(\d+)</em>.*?src="(.*?)".*?<span class="title">(.*?)</span>.*?<p class="">(.*?)<br/>(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span class="inq">(.*?)</span>',re.S)
    items = re.findall(pattern,str(soup))
    # print(title)
    for i in items:
        yield {
            'num':i[0],
            'title':i[2],
            'actors':i[3].strip(),
            'year':i[4].strip(),
            'score':i[5],
            'image': i[1],
            'views':i[6]
        }

def save_file(results):
    '''
    将获取信息存到文件
    :param results:
    :return:
    '''
    with open('top250movies','a',encoding='utf-8') as f:
        f.write(results+'\n\n')

def main(page):
    url = "https://movie.douban.com/top250?start="+str(page)
    html=gethtml(url)
    for item in htmlparse(html):
        # print(item)
        content=item['num']+'\n'+'电影名称:'+item['title']+'\n'+'演员/导演：'+item['actors']+'\n'+'年份：'+item['year']+'\n'+'评分：'+item['score']+'\n'+'短评：'+item['views']+'\n'+'电影海报：'+item['image']
        print(content)
        save_file(content)


if __name__ == '__main__':
    start = time.time()
    for i in range(10):
        main(i*25)

    # pool=Pool()
    # pool.map(main,[i*25 for i in range(0,10)])
    end = time.time()
    print('执行时间：'+str(end-start))