# simple util file to get the price of a website using selenium

from selenium import webdriver

def get_price(website):

	driver = webdriver.Chrome()
	driver.get(website)
	
	driver.quit()
	
	return 1234;