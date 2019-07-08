import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

x1=browser.find_element_by_id("num1").text
x2=browser.find_element_by_id("num2").text
y=str(int(x1)+int(x2))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(y)

browser.find_element_by_css_selector("button.btn").click()

