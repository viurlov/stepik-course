from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button=browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
button.click()

browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
browser.find_element_by_id("solve").click()

alert = browser.switch_to.alert
print(alert.text.split()[-1])
alert.accept()
browser.close()
browser.quit()

