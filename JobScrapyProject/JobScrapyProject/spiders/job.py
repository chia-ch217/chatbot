# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from bs4 import BeautifulSoup
from scrapy.exceptions import CloseSpider
from selenium import webdriver

#from ..items import JobscrapyprojectItem
#import pandas as pd
#import numpy as np

#1111
class JobSpider1(scrapy.Spider):
    n = 1
    #a = pd.read_csv(r'C:\Users\GIGABYTE\output.csv') 
    #kw = np.array(a['keyword'])
    #kw1 = kw[0]
    #url = 'https://www.1111.com.tw/search/job?ks={}'.format(kw1)
    #keyword = input('enter key - ')
    name = 'job1'
    allowed_domains = ['1111.com.tw']
    url =  'https://www.1111.com.tw/search/job?ks=java'
    start_urls = [url]
    #print(url)
    def parse(self,response):
        self.logger.info('A response from %s just arrived',response.url)
        soup = BeautifulSoup(response.text,'html.parser')
        title = soup.select("div.position0 > a.text-truncate")
        company = soup.select("div.d-none > a.d-block")
        href = soup.select("div.position0 > a.text-truncate")
        for t, c, h in zip(title, company, href):
            item = {
                    'title':t.get("title"),
                    'company':c.get("title"),  #title抓公司名稱+行業類別+公司住址 , 如果抓text 有些公司名稱會在span那層
                    'link':'https://www.1111.com.tw/' + h.get("href")
                    }
            yield(item)
        '''    
        page_num = soup.select_one('select.custom-select').text.split("/")
        totle_page = int(page_num[1].lstrip())
        
        if self.n <= totle_page:
            self.n = self.n+1
            page_link = (self.url+('&fs=1&page={}'.format(self.n)))
            next_page = response.urljoin(page_link)
        else:
            raise CloseSpider('close it')
            
        yield scrapy.Request(next_page, callback = self.parse, dont_filter=True )
        '''
#104    
class JobSpider2(scrapy.Spider):
    name = 'job2'
    allowed_domains = ['104.com.tw']
    url =  'https://www.104.com.tw/jobs/search/?keyword=java&order=1'
    start_urls = [url]
    print(url)
        
    def parse(self,response):
        self.logger.info('A response from %s just arrived',response.url)
        soup = BeautifulSoup(response.text,'html.parser')
        href = soup.select('div > h2 > a')
        company = soup.select('div.b-block__left > ul > li > a')
        for h,c in zip(href, company):
            item = {
                    'title':h.text,
                    'company':c.text,  
                    'link':'https:' + h.get("href")
                    }
            yield(item)
            
            
        
    
if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(JobSpider1)
    process.crawl(JobSpider2)
    process.start()
       
    
'''    
    #取得連結 
    def parse(self, response):
        
        soup = BeautifulSoup(response.text,'html.parser')
        #總頁數
        
        page_num = soup.select_one('select.custom-select').text.split("/")
        page = page_num[1].lstrip()
        n = 1
        for i in range(1,page+1):
            resp = scrapy.Request('https://www.1111.com.tw/search/job?ks=java&fs=1&page={}'.format(n)) 
 
        title = soup.select("div.position0 > a.text-truncate")
        company = soup.select("div.d-none > a.d-block")
        href = soup.select("div.position0 > a.text-truncate")
        for t, c, h in zip(title, company, href):
            item = {
                    'title':t.get("title"),
                    'company':c.get("title"),  #title抓公司名稱+行業類別+公司住址 , 如果抓text 有些公司名稱會在span那層
                    'link':'https://www.1111.com.tw/' + h.get("href")
                    }
            yield(item)
            
        page_num = soup.select_one('select.custom-select').text.split("/")
        totle_page = int(page_num[1].lstrip())
        
        if self.n <= totle_page:
            self.n = self.n+1
            page_link = (self.url+('&fs=1&page={}'.format(self.n)))
            next_page = response.urljoin(page_link)
        else:
            raise CloseSpider('close it')
            
        yield scrapy.Request(next_page, callback = self.parse, dont_filter=True )
            
        
        
    #進入內文 - items - -o .json    
    #def jobparse(self, response):
'''       
