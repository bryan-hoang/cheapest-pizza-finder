# this is a test script

import time
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
	
	# This is some thing
	driver = webdriver.Chrome()
	driver.get('chrome://settings/')

	time.sleep(3);
	
	driver.quit();
	
	return render_template('scrape.html', template_address = address)