from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random as rand
import pandas as pd

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

driver.get('https://www.inmotionhosting.com/shared-hosting')

plans = driver.find_elements(By.XPATH, "//button[contains(@class, 'imh-term-selector')]")


products = {'term':[], 'name': [], 'price': [], 'features': []}

for button in plans:
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    cards = driver.find_elements(By.XPATH, "//div[@class='imh-rostrum-container']/div[contains(@class, 'imh-rostrum-card')]")
    for card in cards:
        term = button.text
        name = card.find_element(By.CLASS_NAME, 'imh-rostrum-card-title').text
        price = card.find_element(By.XPATH, "//div[contains(@class, 'imh-rostrum-starting-at-price-discounted')]/span").text
        features = card.find_elements(By.XPATH, "//li[contains(@class, 'tooltips-rostrum')]")
        feature_list = [f.text for f in features if len(f.text)!=0]
        products['term'].append(term)
        products['name'].append(name)
        products['price'].append(price)
        products['features'].append(feature_list)

df = pd.DataFrame(products)
df.to_csv(path_or_buf='C:/', sep=',')