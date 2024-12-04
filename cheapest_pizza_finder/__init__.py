from selenium.webdriver.common.by import By
from . import price_scraper
from selenium import webdriver
from flask import Flask, render_template

# setup
app = Flask(__name__)


# main page
@app.route("/")
def index():
    return render_template("index.html")


# results page
@app.route("/scrape/<address>/<radius>")
def scrape(address, radius):
    # This will do the actual web scraping

    formatted_address = (
        f'https://www.yellowpages.ca/search/si/1/pizza/{address.replace(" ", "%20")}'
    )

    dict = {}
    driver = webdriver.Chrome()
    driver.get(formatted_address)

    boxes = driver.find_elements(By.CLASS_NAME, "listing__content__wrapper")
    amount_to_check = 2
    for box in boxes:
        try:
            box_element = box.find_element(By.TAG_NAME, "h3")
            box_dist = box.find_element(By.CLASS_NAME, "listing__distance").text
            box_dist = box_dist[:-2]
            box_dist = float(box_dist)
            if box_dist > float(radius):
                continue

            box_name = box_element.text
            box_link = box_element.find_element(By.TAG_NAME, "a").get_attribute("href")
            # use a second driver?
            driver2 = webdriver.Chrome()
            box_price = price_scraper.get_price(driver2, box_link)
            driver2.quit()

            dict[box_name] = box_price
        except Exception:
            pass

        amount_to_check -= 1
        if amount_to_check == 0:
            break

    # time.sleep(3)
    driver.quit()
    # example_price = get_price('https://www.yellowpages.ca/bus/Alberta/Calgary/GS-Square-Deep-Dish-Pizza/2302759.html')
    # dict['GS Square Deep Dish Pizza'] = example_price
    return render_template("scrape.html", template_address=address, price_dict=dict)
