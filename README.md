# douban-movies-top250
豆瓣电影top250爬虫

----------
爬取url：https://movie.douban.com/top250

用到的python库：
```python
requests
BeautifulSoup
multiprocessing
time
```
抓取的字段：

电影名称，演员/导演，年份，评分，短评，电影海报

目标：
使用多进程，获取豆瓣电影top250的电影相关信息

爬取结果：

![](http://chuantu.biz/t6/166/1512389869x-1404817776.png)

利用多进程爬取：

![](http://chuantu.biz/t6/166/1512390166x-1404775429.png)

未使用多进程：

![](http://chuantu.biz/t6/166/1512390209x-1566688303.png)