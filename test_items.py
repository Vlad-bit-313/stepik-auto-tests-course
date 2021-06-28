# Урок 3.6 шаг 9
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_(browser):
    browser.get(link)
    time.sleep(30)
    cart_button = browser.find_element_by_css_selector("[type='submit'].btn-add-to-basket")
    assert cart_button, "Should be a button!"