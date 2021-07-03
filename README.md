# parser-vacancy
Подготовка к Хакатону - парсер Вакансий

Парсер реализован как проект на джанго - с отображением результатов через браузер.
Сбор данных с сайтов будет реализован через облачный сервер с Селеноидом или через доступные АПИ.

Для проекта не важен регион - важно собрать достаточное количество вакансий, для анализа
требований работодателей и составления карты специальностей и требований к специалистам.

Собирать данные для начала будем для разработчиков, аналитиков, тестировщиков, дизайнеров,
девопс инженеров, системных администраторов

Для парсинга будет использоваться Selenium или Selenoid
# For Linux
# First make sure first that you have chrome browser installed on your system.

# a simple way to get the driver is: 
sudo apt-get install chromium-chromedriver
# this will download 75MB of files.

# another way is:
1. Download the lastest version of driver from:
  https://sites.google.com/a/chromium.org/chromedriver/ # only 5-7MB
2. Unzip the file.
3. Paste the file in /usr/local/bin using this command:
  sudo mv chromedriver /usr/local/bin # this makes sure that the directory is in your PATH variable.
4. Make your file executable:
  sudo chmod +x /usr/local/bin/chromedriver

Загрузить драйвер Chrome:
чтобы загрузить веб-драйверы, вы можете выбрать любой из следующих способов:
Вы можете напрямую загрузить драйвер Chrome по
ссылке ниже - https://chromedriver.chromium.org/downloads
Или вы можете загрузить его напрямую, используя следующую строку кода: 
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().Install())

Now you can use this in python:
  >>from selenium import webdriver
  >>browser = webdriver.Chrome()