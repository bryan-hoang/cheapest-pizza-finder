# simple util file to get the price of a website using selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def get_price(driver: WebDriver, website):
    driver.get(website)
    output = "Stuff:\n\n"

    # load the current active menu
    # menu = driver.find_element_by_xpath("//*[@class='menu__content
    # jsMenuContent']")

    # find all items in the menu
    menu_items = driver.find_elements(By.CLASS_NAME, "food-menu--item")

    # fallback
    rate_element = driver.find_element(
        By.XPATH,
        "//*[@class='merchant__item merchant__item--inline merchant__item--rates']",
    )
    rate_list_element = rate_element.find_element(By.TAG_NAME, "li")
    rate = rate_list_element.text
    # output += 'The rates are: %s' % rate

    for item in menu_items:
        try:
            item_title = item.find_element(By.CLASS_NAME, "food-menu--title").text
            output += "Item: %s\n" % item_title
        except Exception:
            output += "Item: ???\n"
            pass

        try:
            output += "Price: "
            item_price = item.find_element(By.CLASS_NAME, "food-menu--price")
            for price_element in item_price.find_elements(By.TAG_NAME, "span"):
                output += "%s, " % price_element.get_attribute("innerHTML")
        except Exception:
            output += "FAIL\n"
            pass
        output += "\n\n"

    return rate
