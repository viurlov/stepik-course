import os
from selenium import webdriver
from selenium.webdriver.common.by import By


name="Вася"
lname="Пупкин"
email="vasya@example.com"

current_dir = os.path.abspath(os.path.dirname('.'))
file_path = os.path.join(current_dir, 'file.txt')

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element_by_css_selector('[placeholder="Введите имя"]').send_keys(name)
browser.find_element_by_css_selector('[placeholder="Введите фамилию"]').send_keys(lname)
browser.find_element_by_css_selector('[placeholder="Введите Email"]').send_keys(email)
browser.find_element_by_id("file").send_keys(file_path)
browser.find_element_by_tag_name("button").click()

alert = browser.switch_to.alert
print(alert.text.split()[-1])
alert.accept()

browser.close()
browser.quit()

