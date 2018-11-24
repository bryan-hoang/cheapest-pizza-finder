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
	
	#driver = webdriver.Chrome()
	#driver.get('https://www.yellowpages.ca/search/si/1/pizza/%s' % formatted_address)

	#time.sleep(3)
	
	#driver.quit()
	
	dict = {}
	
	example_price = get_price('https://www.yellowpages.ca/bus/Alberta/Calgary/GS-Square-Deep-Dish-Pizza/2302759.html')
	dict['GS Square Deep Dish Pizza'] = example_price
	
	return render_template('scrape.html', template_address = address, price_dict = dict)
