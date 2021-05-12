# 패키지 포함
from selenium import webdriver as wd

# 드라이버 설정
driver = wd.Chrome(executable_path="chromedriver.exe")

# 추출할 url
url = "http://search.khan.co.kr/search.html?stb=khan&q=%EC%96%B4%EB%A6%B0%EC%9D%B4%EB%82%A0"