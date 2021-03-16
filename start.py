import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import configparser

import random

# 설정파일 읽기
config = configparser.ConfigParser()    
config.read('config.ini', encoding='utf-8') 

# 설장파일 색션 확인
config.sections()

# 섹션값 읽기
link = config['OnLineClass']['URL']
email = config['OnLineClass']['email']
id = config['OnLineClass']['id']
integrationname = config['OnLineClass']['integrationname']
name = config['OnLineClass']['name']
grade = config['OnLineClass']['grade']
type = config['OnLineClass']['type']
host = config['OnLineClass']['host']
atnlcNo = config['OnLineClass']['atnlcNo']
lctreSn = config['OnLineClass']['lctreSn']
userSn = config['OnLineClass']['userSn']
count = config['OnLineClass']['count']
proxy = config['OnLineClass']['proxy']
proxyurl = config['OnLineClass']['proxyurl']

# count에 수를 string 에서 int로 변환
n = int(count)

# URL 설정
#URL = link + '?email=' + email + '&id=' + id + '&integrationname=' + integrationname + '&name=' + name + '&grade=' + grade + '&type=' + type + '&host=' + host + '&atnlcNo=' + atnlcNo + '&lctreSn=' + lctreSn + '&userSn=' + userSn


driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("file:///C:/Users/codn5/Downloads/um/EBS%20%EC%98%A8%EB%9D%BC%EC%9D%B8%20%ED%81%B4%EB%9E%98%EC%8A%A4.html")

driver.implicitly_wait(3)

x = str(input()) # 입력받은 값을 변수에 저장


index = 0 # 몇번째 반복인지 기억하는 변수


if x == 'start':
    while index < n:  # index 변수가 count 수 보다 작은 동안 반복
        random_id = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
        print("id= " + random_id + " / name= " + name)
        # 신규 URL
        R_URL = link + '?email=' + random_id + '@ebsoc.co.kr' + '&id=' + random_id + '&integrationname=' + integrationname + '&name=' + name + '&grade=' + grade + '&type=' + type + '&host=' + host + '&atnlcNo=' + atnlcNo + '&lctreSn=' + lctreSn + '&userSn=' + userSn
        driver.execute_script("window.open('" + R_URL + "','_blank')") # 새탭 오픈
        driver.implicitly_wait(3)

        element = driver.find_element_by_class_name('start-button-text')
        element.click() # 입장 버튼 클릭

        index += 1 

if x == 'end':
    driver.quit()