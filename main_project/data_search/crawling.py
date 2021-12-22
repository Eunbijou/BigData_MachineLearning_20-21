from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
# pip install pyautogui , selenium , Keys , time 하나씩


# >>>>>!!실행된 크롬을 전체화면으로 설정해주세요!!<<<<<
def A():
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get('https://data.seoul.go.kr/')
    # 공공데이터 클릭
    data = browser.find_element_by_xpath('//*[@id="baseNav"]/ul/li[1]/a')
    time.sleep(2)
    data.click()

    # 검색
    find = browser.find_element_by_xpath('//*[@id="searchKeyword"]')
    time.sleep(1)
    find.click()
    find.send_keys('서울시 년도별 유동인구 및 사업체 정보')
    time.sleep(1)

    find.send_keys(Keys.ENTER)
    time.sleep(1)

    # 페이지 클릭
    click = browser.find_element_by_xpath('//*[@id="datasetVO"]/div[2]/div/section/div[2]/dl/dt/a/strong')
    click.click()
    time.sleep(1)

    # 파일 전체보기 클릭
    more = browser.find_element_by_xpath('//*[@id="listDownload"]/a')
    more.click()
    time.sleep(2)

    # 다운로드
    down_0 = browser.find_element_by_xpath('//*[@id="fileTr_8"]/td[6]/a')
    down_0.click()
    time.sleep(1)

    down_1 = browser.find_element_by_xpath('//*[@id="fileTr_5"]/td[6]/a')
    down_1.click()
    time.sleep(20)
    browser.close()


def B():
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get('https://data.seoul.go.kr/')
    # 마우스 포인터 움직이기
    time.sleep(1)
    pyautogui.moveTo(900,200,1)
    time.sleep(1)
    pyautogui.moveTo(900,300,0.5)
    pyautogui.moveTo(1050,300,0.5)
    pyautogui.click()
    time.sleep(1)

    # 유동인구 조사 클릭
    people = browser.find_element_by_xpath('// *[ @ id = "seoulstats2"] / div[1] / div / button[10]')
    people.click()
    time.sleep(1)

    year = browser.find_element_by_xpath('//*[@id="treeMenu"]/li[4]/a/span')
    year.click()
    time.sleep(1)

    # 다운로드
    down_2 = browser.find_element_by_xpath('//*[@id="subMenu19"]/div[4]/span[2]/a/img')
    down_2.click()
    time.sleep(10)
    browser.close()


def C():
    browser = webdriver.Chrome("./chromedriver.exe")
    browser.get('https://data.seoul.go.kr/')
    # 공공데이터 클릭
    data = browser.find_element_by_xpath('//*[@id="baseNav"]/ul/li[1]/a')
    time.sleep(2)
    data.click()

    # 검색
    find = browser.find_element_by_xpath('//*[@id="searchKeyword"]')
    time.sleep(1)
    find.click()
    find.send_keys('서울특별시 공공자전거 대여이력 정보')
    time.sleep(1)

    find.send_keys(Keys.ENTER)
    time.sleep(1)

    # 페이지 클릭
    click = browser.find_element_by_xpath('//*[@id="datasetVO"]/div[2]/div/section/div[2]/dl/dt/a/strong')
    click.click()
    time.sleep(1)

    # 파일 전체보기 클릭
    more = browser.find_element_by_xpath('//*[@id="listDownload"]/a')
    more.click()
    time.sleep(2)

    # 다운로드 24개
    for cnt in range(7,31):
        down_0 = browser.find_element_by_xpath('//*[@id="fileTr_'+str(cnt)+'"]/td[6]/a')
        down_0.click()
        time.sleep(0.5)

    time.sleep(100)
    browser.close()

print('실행된 크롬을 전체화면으로 설정해주세요.')
A()
time.sleep(1.5)
B()
time.sleep(1.5)
C()
time.sleep(1.5)
print('\n''다운로드 완료')