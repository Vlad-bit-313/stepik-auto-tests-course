# Урок 3.6 шаг 9
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_cart(browser):
    browser.get(link)
    time.sleep(5)
    cart_button = browser.find_elements_by_css_selector("[type='submit'].btn-add-to-basket")
    assert cart_button, "Should be a button!"