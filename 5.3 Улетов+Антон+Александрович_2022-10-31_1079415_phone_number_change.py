import time

import action as action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# подтянуть вебдрайвер
s=Service('C:/Users/User/Desktop/TSU/Autotests/chromedriver.exe')
driver = webdriver.Chrome(service=s)
# открыть сайт
driver.get("https://qa.neapro.site/login/")
# в максимальном окне
driver.maximize_window()
# ввести в поле логин значение uletov.test@test.ru
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input").send_keys("uletov.test@test.ru")
# ввести в поле пароль значение 123456
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[1]/div[2]/div/input").send_keys("123456")
# нажать на кнопку
driver.find_element(By.XPATH, "//*[@id='__layout']/div/section/div[2]/div/div/div/form/div[2]/button").click()
# пауза 2 сек, без нее ошибка, не успевает найти кнопку с аватаркой
time.sleep(3)
# клик на кнопку с аватаркой
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[2]/a").click()
time.sleep(1)
# клик на кнопку безопасность и вход
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/ul/li[2]/a").click()
time.sleep(1)
# клик на кнопку изменить номер телефона
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]").click()
# очистка поля телефно
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").clear()
# ввод нового значения в поле телефон
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/div/div/input").send_keys("8888888888")
# клик на кнопку подтвердить
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[2]/div/div/div/div[2]/form/button").click()
time.sleep(1)

# наведение курсора мыши на sidebar (нашел на stackoverflow)
action = ActionChains(driver)
menu = driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div")
action.move_to_element(menu).perform()

# выход из аккаунта
driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[1]/div[1]/div").click()