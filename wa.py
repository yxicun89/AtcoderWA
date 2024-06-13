from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests, html
from bs4 import BeautifulSoup
import pandas as pd
# from mer2 import get_url, get_data
import sys
import re
import time
import datetime
import csv
# from wa import user_login, get_url 
# from beautiful import source_to_csv



def user_login(user_id,user_ps,browser):
    login = "https://atcoder.jp/login?lang=ja"
    browser.get(login)
    browser.implicitly_wait(5)
    
    user_id_path="#username"
    user_ps_path="#password"
    button_path="#submit"
    
    browser.find_element(By.CSS_SELECTOR,user_id_path).send_keys(user_id)
    browser.find_element(By.CSS_SELECTOR,user_ps_path).send_keys(user_ps)
    browser.find_element(By.CSS_SELECTOR,button_path).click()




def get_url(keyword,number,max_page,browser):
    url="https://atcoder.jp/contests/" + keyword + "/submissions?f.Task=" + keyword + "_" + number + "&f.LanguageName=Python&f.Status=WA&f.User="
    page = 1
    code_selector="#main-container > div.row > div:nth-child(3) > div > div.table-responsive > table > tbody > tr"
    item_url = []
    next_selector="#main-container > div.row > div:nth-child(3) > nav:nth-child(6) > ul > li:nth-child(2)"
    
    while page < max_page:
        try:
            browser.get(url)
            browser.implicitly_wait(5)
            codes = browser.find_elements(By.CSS_SELECTOR,code_selector)
            if len(codes) != 0:
                for item_elem in codes:
                    item_url.append(item_elem.find_element(By.CSS_SELECTOR, 'td:nth-child(10) > a').get_attribute('href'))
            else:
                break
            
            try:
                next_page=browser.find_elements(By.CSS_SELECTOR,next_selector)
                if len(next_page) != 0:
                    page+=1
                    next_url = "https://atcoder.jp/contests/"+ keyword +"/submissions?f.LanguageName=Python&f.Status=WA&f.Task=" +keyword + "_" + number + "&f.User=&page=" + str(page)
                    print(next_url)
                    url=next_url
                    print(url)
                    next_url=''
                else:
                    break
            except:
                break
        except:
            message=traceback.print_exc()
            print(message)
        
    return item_url


def code_to_csv_py(keyword,number,item_url):
    source_codes=[]
    count = 1
    for url in item_url:
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        time.sleep(3)
        source_codes.append(soup.pre.string)
        
    
    csv_date = datetime.datetime.today().strftime("%Y%m%d")
    csv_file_name = keyword + '_' + number + '_' + csv_date + '.csv'
    pd.DataFrame(source_codes).to_csv(csv_file_name)


def main():
    item_url=[]
    keyword=input('コンテスト名:')
    number=input("問題番号(小文字):")
    max_page=int(input('取得ページ数:'))
    user_id = input('ID:')
    user_ps = input('PASSWORD:')
    options=Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=options)
    user_login(user_id,user_ps,browser)
    item_url = get_url(keyword,number,max_page,browser)
    code_to_csv_py(keyword,number,item_url)


if __name__ == '__main__':
    main()