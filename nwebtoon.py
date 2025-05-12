from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# 브라우저 설정
options = webdriver.ChromeOptions()
options.add_argument  # 브라우저 안 띄움 (테스트 시 끄려면 이 줄 지워도 됨)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 네이버 웹툰 요일별 페이지 접속
url = "https://comic.naver.com/webtoon/weekday"
driver.get(url)
time.sleep(2)

# 월요일 웹툰 리스트 가져오기
webtoons = driver.find_elements(By.CSS_SELECTOR, 'ul.PosterList__list--ZyGDL li')

results = []
죽을
for webtoon in webtoons:
    try:
        title = webtoon.find_element(By.CLASS_NAME, 'Poster__title--dX3MH').text
        img = webtoon.find_element(By.TAG_NAME, 'img').get_attribute('src')
        author = webtoon.find_element(By.CLASS_NAME, 'Poster__author--tFAl_').text
        rating = webtoon.find_element(By.CLASS_NAME, 'Poster__star--WjPbT').text

        results.append({
            'title': title,
            'thumbnail': img,
            'author': author,
            'rating': rating
        })
    except Exception as e:
        print("오류 발생:", e)
        continue

driver.quit()

# 결과 출력
for r in results:
    print(r)