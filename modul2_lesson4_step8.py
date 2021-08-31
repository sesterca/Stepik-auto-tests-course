from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
	browser.get(link)
	price = WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), '100')
	)
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()
	x = (browser.find_element(By.ID, "input_value").text)
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)
	answer = browser.find_element(By.ID, "answer")
	answer.send_keys(y)
	submit = browser.find_element(By.ID, "solve")
	submit.click()
	time.sleep(10)

finally:
	browser.quit()

#пустая строка для запуска