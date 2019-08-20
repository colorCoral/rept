from selenium import webdriver
import requests
import json



dic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
driver = webdriver.Chrome(r'chromedriver.exe')


def get_music(msg):
    url1 = f'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w={msg}'
    driver.get(url1)
    driver.implicitly_wait(5)  # 5秒钟之内元素加载完即可，智能等待
    data = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[2]/span[1]/a').get_attribute('href')
    # print(data)
    data = {"mid":data}

    url2 = 'http://www.douqq.com/qqmusic/qqapi.php'
    req = requests.post(url2,data=data,headers=dic).text
    req = req.replace("\\",'')
    req = req.strip('"')
    req = json.loads(req)
    return req['mp3_l']

