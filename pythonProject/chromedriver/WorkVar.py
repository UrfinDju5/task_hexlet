from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import pandas as pd

from fake_useragent import UserAgent
# Фэйковый юзэр агент из стандартной библиотеки пайтона

url = "https://oks.rosakadem.ru/Login?toPage=Examing?course=200"

useragent = UserAgent()

# Options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
options.add_argument("--disable-infobars")
options.add_argument("--disable-blink-fetures=AutomationControlled")


driver = webdriver.Chrome(options=options)
# executable_path="chromedriver.exe"

def go_to_page():

    driver.get(url=url)

    Login_input = driver.find_element(By.NAME, "login")
    Login_input.clear()
    Login_input.send_keys("rn-sz")

    Password_input = driver.find_element(By.NAME, "password")
    Password_input.clear()
    Password_input.send_keys("ht8PzPX5")

    time.sleep(1)

    Press_button = driver.find_element(By.NAME, "doAuthButton")
    Press_button.click()

    time.sleep(1)

    Surname_input = driver.find_element(By.NAME, "surname")
    Surname_input.clear()
    Surname_input.send_keys("Емельянова")

    Name_input = driver.find_element(By.NAME, "name")
    Name_input.clear()
    Name_input.send_keys("Елена")

    Fathername_input = driver.find_element(By.NAME, "fathername")
    Fathername_input.clear()
    Fathername_input.send_keys("Вадимовна")

    Job_input = driver.find_element(By.NAME, "job")
    Job_input.clear()
    Job_input.send_keys("Кассир ТЗ")

    time.sleep(2)

    Day_input = driver.find_element(By.NAME, "day_b")
    time.sleep(1)
    Day_input.is_selected()
    Day_input.send_keys("2")

    Month_input = driver.find_element(By.NAME, "month_b")
    Month_input.is_selected()
    Month_input.send_keys("9")

    Year_input = driver.find_element(By.NAME, "year_b")
    Year_input.is_selected()
    Year_input.send_keys("1995")

    time.sleep(1)

    Submit_button = driver.find_element(By.NAME, "submitRegistration")
    Submit_button.click()

    time.sleep(2)

    Select_otr = driver.find_element(By.LINK_TEXT, "Охрана труда").click()
    Select_BMP = driver.find_element(By.LINK_TEXT, "Безопасные методы и приемы выполнения работ при воздействии вредных и (или) опасных производственных факторов, источников опасности, идентифицированных в рамках специальной оценки условий труда и оценки профессиональных рисков").click()
go_to_page()
df = pd.DataFrame()
# Создаем датафрейм Добавляем данные, создаем имена колонок
col = ["Вопрос", "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5"]
df = pd.DataFrame(columns=col)

def take_data():
    global df
    # Пиздим вопрос
    Question_elem = driver.find_elements(By.CLASS_NAME, "question-text")
    question1 = []
    for question_elem in Question_elem:
        question1 = [question_elem.text]
        time.sleep(2)
    # Пиздим ответы
    answers_elem = driver.find_elements(By.ID, "answers-block")
    answers1 = []
    for answer_elem in answers_elem:
        answers1 = [answer_elem.text]
        time.sleep(2)
    # Разбираем ответы на части, записываем их в датафрейм
    for i in answers1:
        new_row = i.split("\n")
        if len(new_row) == 2:
            answer1 = new_row[0]
            answer2 = new_row[1]
            answer3 = "non"
            answer4 = "non"
            answer5 = "non"
            df.loc[len(df)] = [question1, answer1, answer2, answer3, answer4, answer5]
        elif len(new_row) == 3:
            answer1 = new_row[0]
            answer2 = new_row[1]
            answer3 = new_row[2]
            answer4 = "non"
            answer5 = "non"
            df.loc[len(df)] = [question1, answer1, answer2, answer3, answer4, answer5]
        elif len(new_row) == 4:
            answer1 = new_row[0]
            answer2 = new_row[1]
            answer3 = new_row[2]
            answer4 = new_row[3]
            answer5 = "non"
            df.loc[len(df)] = [question1, answer1, answer2, answer3, answer4, answer5]
        elif len(new_row) == 5:
            answer1 = new_row[0]
            answer2 = new_row[1]
            answer3 = new_row[2]
            answer4 = new_row[3]
            answer5 = new_row[4]
            df.loc[len(df)] = [question1, answer1, answer2, answer3, answer4, answer5]
        else:
            continue
select_answer = driver.find_element(By.ID, "1").click()
take_data()
for i in range(10):
    take_data()
    select_answer = driver.find_element(By.ID, "a1").click()
    push_button = driver.find_element(By.ID, "submitAnswer").click()
push_but = driver.find_element(By.ID, "submitExam").click()
push_but2 = driver.find_element(By.ID, "continueExaming").click()
# Записываем данные в таблицу Excel continueExaming
df.to_excel('data.xlsx', index=False)
print(df)
time.sleep(10)
