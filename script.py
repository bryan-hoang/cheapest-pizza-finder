# this is a test script

import time
from price_scraper import get_price
from selenium import webdriver
from flask import Flask, render_template

# setup
app = Flask(__name__)

# main page
@app.route('/')
def index():
    return render_template('index.html')

# results page
@app.route('/scrape/<address>')
def scrape(address):
	# This will do the actual web scraping
		
	formatted_address = address.replace(' ', '%20')
	
	dict = {}
	driver = webdriver.Chrome()
	driver.get('https://www.yellowpages.ca/search/si/1/pizza/%s' % formatted_address)
	
	boxes = driver.find_elements_by_class_name('listing__content__wrapper')
	amount_to_check = 2
	for box in boxes:
		try:
			box_element = box.find_element_by_tag_name('h3')
			box_name = box_element.text
			box_link = box_element.find_element_by_tag_name('a').get_attribute('href')
			#use a second driver?
			driver2 = webdriver.Chrome()
			box_price = get_price(driver2, box_link)
			driver2.quit()
			
			dict[box_name] = box_price
			amount_to_check -= 1
		except Exception:
			pass
		
		if amount_to_check == 0:
			break
	
	#time.sleep(3)
	driver.quit()
	
	#example_price = get_price('https://www.yellowpages.ca/bus/Alberta/Calgary/GS-Square-Deep-Dish-Pizza/2302759.html')
	#dict['GS Square Deep Dish Pizza'] = example_price
	
	return render_template('scrape.html', template_address = address, price_dict = dict)