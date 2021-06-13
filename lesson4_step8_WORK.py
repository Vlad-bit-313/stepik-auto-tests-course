from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium import  webdriver
import time
import re

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    # жду пока дойдёт до определенного момента и жду этот результат 10 секунд

    wait = WebDriverWait(browser, 10)
    button_wait = wait.until(
            EC.text_to_be_present_in_element((By.ID, "price"),'100')
        )
    if button_wait:
        button = browser.find_element_by_id('book')
        button.click()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    #x_element = browser.find_element_by_id('input_value')
    x_element = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "input_value"))
    )
    x = x_element.text
    y = calc(x)
    # вставляем результат

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button_send = browser.find_element_by_id('solve')
    button_send.click()
    alert = browser.switch_to.alert
    alert_text = alert.text

    # ищем что нам нужно
    pattern =  r'\d.*'
    answer = re.search(pattern, alert_text)
    print(answer.group(0))


finally:
    time.sleep(2)
    browser.quit()
