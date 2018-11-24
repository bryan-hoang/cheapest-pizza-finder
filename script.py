# this is a test script

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape/<address>')
def scrape(address):
	# This will do the actual web scraping
	
	# This is some thing
	
	return render_template('scrape.html', template_address = address)