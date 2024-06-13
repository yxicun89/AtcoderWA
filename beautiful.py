import re
import time
import pandas as pd
import datetime
import csv
import requests, html
from bs4 import BeautifulSoup


def source_to_csv(code_list):
    for code in code_list:
        html = requests.get(code)
        soup = BeautifulSoup(html.content, "html.parser")
        source_codes=[]
        source_codes.append(soup.pre.string)
    
    csv_date = datetime.datetime.today().strftime("%Y%m%d")
    csv_file_name = 'source' +'_'+ csv_date + '.csv'
    pd.DataFrame(source_codes).to_csv(csv_file_name)