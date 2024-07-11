from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
def serch_wiki():
    question = input('Что ищем? ')
    return question
def menu1():
    choise = input(
        "Выберите что делать: \n1 - если листать параграфы, \n2 - если посмотреть связанные статьи, \n3 - если выйти. ")
    if choise !="1":
        if choise !="2":
            if choise !="3":
                print('Некорректный ввод')
                menu1()
    return choise
def menu2():
    choise = input(
        "Выберите что делать: \n1 - если листать параграфы, \n2 - если посмотреть связанные статьи, \n3 - если выйти. ")
    if choise !="1":
        if choise !="2":
            if choise !="3":
                print('Некорректный ввод')
                menu2()
    return choise

browser = webdriver.Firefox()
browser.get('https://ru.wikipedia.org/wiki/')

assert 'Википедия' in browser.title
search_box = browser.find_element(By.ID, 'searchInput')
request_user = serch_wiki()
search_box.send_keys(request_user + Keys.RETURN)
time.sleep(3)
a = browser.find_element(By.LINK_TEXT, request_user)
time.sleep(2)
a.click()

choise = menu1()
if choise == '1':
    paragraphs = []
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    koll = len(paragraphs)
    for paragraph in paragraphs:
        print(paragraph.text)
        koll = koll - 1
        print("Осталось просмотреть параграфов: " + str(koll))
        input()
elif choise == '2':
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, 'div'):
        cl = element.get_attribute('class')
        if cl == 'hatnote navigation-not-searchable':
            hatnotes.append(element)

    if len(hatnotes) != 0:
        hatnote = random.choice(hatnotes)
        Link_a = hatnote.find_element(By.TAG_NAME, 'a')
        link = Link_a.get_attribute('href')
        title = Link_a.get_attribute('title')
        browser.get(link)
        print(f"Открыта статья {title}")
    else:
        print('Нет связанных статей')
    choise = menu2()
    if choise == '1':
        paragraphs = []
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        koll = len(paragraphs)
        for paragraph in paragraphs:
            print(paragraph.text)
            koll = koll - 1
            print("Осталось просмотреть параграфов: " + str(koll))
            input()
    elif choise == '2':
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, 'div'):
            cl = element.get_attribute('class')
            if cl == 'hatnote navigation-not-searchable':
                hatnotes.append(element)

        if len(hatnotes) != 0:
            hatnote = random.choice(hatnotes)
            Link_a = hatnote.find_element(By.TAG_NAME, 'a')
            link = Link_a.get_attribute('href')
            title = Link_a.get_attribute('title')
            browser.get(link)
            print(f"Открыта статья {title}")
        else:
            print('Нет связанных статей')
    else:
        print('Всего доброго')
else:
    print('Всего доброго')


time.sleep(2)
print("Работа программы окончена ! ")




