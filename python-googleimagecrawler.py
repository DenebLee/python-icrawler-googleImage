from icrawler.builtin import GoogleImageCrawler
import os
from datetime import date


a = str(input("다운받을 이미지 키워드 입력 : "))
b = int(input("다운받을 이미지 갯수 입력 : "))

dir_path = "./img"
dir_name = a

save_dir = os.path.join('./img')
filters = {
    'size': 'large',
    'license': 'noncommercial,modify', # 비상업용도, 수정 가능
    }
# GoogleImageCrawler 객체 생성
google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
google_crawler.crawl(keyword=a, max_num=b, filters=filters)