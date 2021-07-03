import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# путь к драйверу chrome
chromedriver = '/usr/bin/chromedriver' #'/usr/local/bin/chromedriver'

def init_driver():
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')  # для открытия headless-браузера
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    driver.wait = WebDriverWait(driver, 5)
    return driver


def search_in_google_url(driver, query):
    search_url = f"https://www.google.ru/search?as_q={query['q']}\
        &as_epq={query['as_epq']}\
        &as_oq={query['as_oq']}\
        &as_eq={query['as_eq']}\
        &as_nlo={query['as_nlo']}\
        &as_nhi={query['as_nhi']}\
        &lr={query['lr']}\
        &cr={query['cr']}\
        &as_qdr={query['as_qdr']}\
        &as_sitesearch={query['as_sitesearch']}\
        &as_occt={query['as_occt']}\
        &safe={query['safe']}\
        &as_filetype={query['as_filetype']}\
        &tbm={query['tbm']}\
        &num={query['num']}\
        &tbs={query['tbs']}"
    driver.get(search_url)

def search_in_google_doc(driver, query):
    search_url = f"https://www.google.ru/search?as_q={query['q']}\
        &as_epq={query['as_epq']}\
        &as_oq={query['as_oq']}\
        &as_eq={query['as_eq']}\
        &as_nlo={query['as_nlo']}\
        &as_nhi={query['as_nhi']}\
        &as_rq={query['as_rq']}\
        &lr={query['lr']}\
        &cr={query['cr']}\
        &hl={query['hl']}\
        &gl={query['gl']}\
        &as_qdr={query['as_qdr']}\
        &as_sitesearch={query['as_sitesearch']}\
        &as_occt={query['as_occt']}\
        &safe={query['safe']}\
        &as_filetype={query['as_filetype']}\
        &tbs={query['tbs']}\
        &as_rights={query['as_rights']}\
        &tbm={query['tbm']}\
        &num={query['num']}\
        &start={query['start']}\
        &newwindow={query['newwindow']}\
        &filter={query['filter']}\
        &pws={query['pws']}"
    driver.get(search_url)

# подробное описание в заметке https://www.evernote.com/shard/s220/sh/9e6083a5-9e68-4cc6-b4e7-446ae748db1d/3b9a8c335c6ea38a92a5172760173d5c
query = {
    'q': "",              # базовый запрос
    'as_epq': "",         # поиск по фразе в точной форме, аналог оператора “” (кавычки)
    'as_oq': "",          # поиск по любому слову фразы, аналог оператора OR
    'as_eq': "",          # исключаемая из запроса фраза, аналог оператора – (минус)
    'as_nlo': "",         # задают начало и конец цифрового диапазона соответственно,
    'as_nhi': "",         # аналог оператора .. (две точки)
    'as_sitesearch': "",  # сужают область поиска на заданный сайт, аналог оператора site:
    'as_rq': "",          # – ищет страницы, похожие на заданный документ (в качестве
                          # значения используется URL документа), аналог оператора related:
    'as_occt': "any",     # задает область документа для поиска, принимает значения
    # - as_occt=title (поиск в теге title, аналог оператора allintitle:)
    # - as_occt=body (поиск в тексте страницы, аналог оператора allintext:)
    # - as_occt=url (поиск в URL страницы, аналог оператора allinurl:)
    # - as_occt=links (поиск в текстах ссылок на страницу, аналог оператора allinanchor:)
    'as_filetype': "",    # задает формат документов для поиска (аналог оператора filetype:)
                          # и принимающий значения pdf,ps,dwf,kml,kmz,xls,ppt,doc,rtf,swf.
    'lr': "",             # язык документа lang_ru lang_en
    'hl': "ru",           # язык интерфейса (приминает значения в виде индекса языка).
    'cr': "",             # страна документа (принимает значения в виде countryRU).
    'gl': "",             # страна документа, принимает значения в виде  ru для России,
                          # аналог оператора cr, однако выдачу строит отличную от него.
                          # Стоит заметить, что при использовании операторов cr и gl в топ
                          # выдачи подмешиваются сайты из региона или страны пользователя,
                          # если она не совпадает со страной, заданной оператором
    'as_qdr': "all",      # поиск по документам, имеющим определенную дату обновления
                          # (при совместном использовании приоритет имеет параметр tbs)
    'tbs': "",            # as_qdr=h9 сузит выдачу на документы, обновленную за последние 9 часов,
                          # а комбинация tbs=m24 – за последние 24 месяца.
    # Также с помощью оператора tbs можно задавать произвольный диапазон дат обновления
    # документа, в этом случае, он принимает значение следующего формата:
    # tbs=cdr:1,cd_min:01.07.2016,cd_max:01.08.2016
    # (в данном примере указан диапазон от 01.07.1016 до 01.08.2016)

    # Параметры фильтрации контента:
    'safe': "on",         # значения active и on включают фильтр непристойных результатов
                          # с помощью безопасного поиска, значение off отключает фильтр в
                          # случае, если в настройках поиска был включен режим «Безопасный
                          # поиск»; этот параметр может быть весьма полезен для определения,
                          # не попал ли конкретный сайт или документ под данный фильтр
    'as_rights': "",      # задание различных вариантов прав на использование контента
    'tbm': "",            # поиск по различным типам контента, принимает значения
                          # - app – поиск по приложениям
                          # - bks – поиск по книгам
                          # - isch – поиск по изображениям
                          # - nws – поиск по новостям
                          # - pts – поиск по патентам
                          # - shop – поиск по магазинам
                          # - vid – поиск по видео
    # Параметры управления результатами поиска:
    'num': "50",          # количество результатов на странице поиска, от 1 до 100
    'start': "",          # показ выдачи, начиная с заданной позиции (например, start=100)
    'newwindow': 0,       # 1 - открывать ссылки в новом окне
    'filter': 0,          # показать скрытые результаты, которые очень похожи на уже
                          # представленные
    'pws': ""             # управление персональными результатами поиска, принимает
                          # значения 0 (персональные результаты скрыты)
                          # 1 (персональные результаты включены)
}

if __name__ == "__main__":
    driver = init_driver()
    query['q'] = "Курс UX дизайнер"
    query['as_sitesearch'] = "netology.ru"
    query['tbs'] = "m24"
    query['num'] = "50"

    search_in_google_url(driver, query)
    time.sleep(5)
    element = driver.find_element_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a")
    element.text()
    print(element.text())
    driver.quit()
