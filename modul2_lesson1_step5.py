from selenium import webdriver
import time
import math
link='http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

try:
	x = browser.find_element_by_id('input_value')
	x1 = (x.text)
	def calc(x1):
		return str(math.log(abs(12*math.sin(int(x1)))))
	y = calc(x1)
	print(y)
	input = browser.find_element_by_css_selector('#answer')
	input.send_keys(y)
	check = browser.find_element_by_id('robotCheckbox')
	check.click()
	radio = browser.find_element_by_id('robotsRule')
	radio.click()
	button = browser.find_element_by_css_selector('[type="Submit"]')
	button.click()
finally:
	time.sleep(20)
	browser.quit()

