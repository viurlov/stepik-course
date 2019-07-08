from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

browser.find_element_by_tag_name("button").click()

alert = browser.switch_to.alert
alert.accept()

browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
browser.find_element_by_tag_name("button").click()

alert = browser.switch_to.alert
print(alert.text.split()[-1])
alert.accept()
browser.close()
browser.quit()

