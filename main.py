# 패키지 포함
# 크롤링을 위한 셀레니움
from selenium import webdriver as wd
from datetime import datetime
from dateutil.relativedelta import *
import re

# DB 연결을 위한 Singleton 패턴 방식의 커텍터 구현
import DBConnect as db

# 대기 시간
wait_time = 5
# 드라이버 설정 90.0.4430
dv = wd.Chrome(executable_path="./exe/chromedriver.exe")

now_date = datetime.now().date()
prev_date = now_date + relativedelta(months=-1)

now_date = now_date.strftime('%Y%m%d')
prev_date = prev_date.strftime('%Y%m%d')

# DB 인스턴스 생성
my_db = db.Database('news')
page = 1

day_reg = re.compile('([0-9]{4}\.[0-9]{2}\.[0-9]{2} [0-9]{2}:[0-9]{2})')


def delay(ms=wait_time):
    dv.implicitly_wait(ms)


for i in range(0, 1):
    # 추출할 url
    main_url = "https://search.khan.co.kr/search.html?" \
               "stb=khan&dm=3&pg={}&d1={}~{}&q=%EC%96%B4%EB%A6%B0%EC%9D%B4%EB%82%A0".\
                format(page, prev_date, now_date)

    dv.get(url=main_url)
    delay()
    news_list = dv.find_elements_by_css_selector("div.news dl.phArtc dt a")  # 해당 페이지의 기사 리스트 추출
    list_size = len(news_list)  # 기사가 있는지 없는지 검사하기 위해 사용

    for idx, news in enumerate(news_list):
        news.click()
        tab = dv.window_handles[1]
        dv.switch_to.window(window_name=tab)

        '''                     추출                      '''
        try:
            title = dv.find_element_by_css_selector('h1.headline').text
            author = dv.find_element_by_css_selector('span.name').text
            author = str(author).split(' ')[0]
            t_day = dv.find_elements_by_css_selector('div.pagecontrol > div.byline > em')
            write_day, mod_day = t_day[0].text, t_day[1].text if len(t_day) != 1 else ''

            write_day = day_reg.findall(write_day)[0]
            mod_day = day_reg.findall(mod_day)[0] if len(t_day) != 1 else ''
            t_content = dv.find_elements_by_css_selector('div.art_cont > div.art_body > p.content_text')
            content = ''.join([tmp.text for tmp in t_content])

            print_msg = "{} {} {} {}".format(title, author, write_day, mod_day)
            print(print_msg)
            dv.close()
        except Exception as ex:
            continue
        finally:
            tab = dv.window_handles[0]
            dv.switch_to.window(window_name=tab)

'''
delay()
        tab = dv.window_handles[1]
        dv.switch_to.window(window_name=tab)
        '''

'''tab = dv.window_handles[1]
dv.switch_to.window(window_name=tab)

subject = dv.find_elements_by_css_selector("div.subject h1")
print(subject)'''
'''news.click()

dv.implicitly_wait(wait_time)
news_content = 
'''
'''content = dv.page_source
html = bs(content, 'html.parser')

print(dv.window_handles)
'''  # 지정한 url 크롬으로 엶

# dv.close()

