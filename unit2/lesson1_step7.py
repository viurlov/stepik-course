import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("treasure").get_attribute("valuex")))
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_css_selector("button.btn").click()

