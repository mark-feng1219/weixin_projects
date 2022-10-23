# -*- coding: utf-8 -*-
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

'''
url不变,用js进行页面跳转,解决方法是实现浏览器模拟人工翻页
'''

options = Options()
options.add_argument('--headless')
pd_arr = pd.DataFrame()
driver = webdriver.Edge(r'D:\Program Files\Python\Python39\msedgedriver.exe',options=options)  # 使用webdriver
url = "http://www.shanghairanking.cn/rankings/bcur/2020"
driver.get(url)
page = 0
name_array = []
rank_array = []
province_array = []
type_array = []
score_array = []
while page < 10:
    soup = BeautifulSoup(driver.page_source, "lxml")
    rank_list = soup.select("tr > td")
    for i in range(30):
        rank_array.append(int(rank_list[6 * i].text.split('\n')[1]))
        name_array.append(rank_list[6 * i + 1].text.split("    ")[0])
        province_array.append(rank_list[6 * i + 2].text.split('\n')[1][12:])
        type_array.append(rank_list[6 * i + 3].text.strip())
        score_array.append(rank_list[6 * i + 4].text.strip())
    driver.find_element(By.XPATH, "//li[@title='下一页']").click()
    page = page + 1
driver.quit()
pd_arr['排名'] = rank_array
pd_arr['学校名称'] = name_array
pd_arr['省份'] = province_array
pd_arr['类型'] = type_array
pd_arr['总分'] = score_array
print(pd_arr)
pd_arr.to_json(r'result.json')
