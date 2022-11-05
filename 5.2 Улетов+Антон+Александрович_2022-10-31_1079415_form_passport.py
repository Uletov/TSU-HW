# Перед запуском теста нужно в админке перевести форму паспорт в ожидание
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# подтянуть вебдрайвер
s=Service('C:/Users/User/Desktop/TSU/Autotests/chromedriver.exe')
driver = webdriver.Chrome(service=s)
# открыть сайт
driver.get("https://qa.neapro.site/login/")
# в максимальном окне
driver.maximize_window()
# ввести в поле логин значение uletov.test@test.ru
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("uletov.test@test.ru")
# ввести в поле пароль значение 123456
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
# нажать на кнопку
driver.find_element(By.CSS_SELECTOR, ".btn").click()
# пауза 2 сек, без нее ошибка, не успевает найти кнопку паспорта
time.sleep(2)
# открыть паспорт
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Иванов")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Иван")
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Иванович")
driver.find_element(By.CSS_SELECTOR, "#birthday > div > input").click()
driver.find_element(By.CSS_SELECTOR, "#birthday > div > input").clear()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#birthday > div > input").send_keys("01.10.2002")
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("1111")
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("111111")
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys("111111")
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("11111111111")
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue > div > input").click()
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue > div > input").clear()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue > div > input").send_keys("11.10.2008")
driver.find_element(By.ID, "issued").click()
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("УВД г. Иваново")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г. Москва, г Зеленоград")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys(8888888888)
driver.execute_script("window.scrollTo(0, 1080)")
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("C:\\Users\\User\\Desktop\\test.jpg")
# далее клик по кнопке отправить, он закоментен, чтобы форма не отправлялась
# driver.find_element(By.CSS_SELECTOR, ".fill").click()