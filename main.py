import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()



response = requests.get(os.getenv("ZILLOW_URL"))
zillow = response.text

soup = BeautifulSoup(zillow, "html.parser")


addresses = [address.getText().split("\n")[1].strip() for address in soup.find_all(name="address")]
print(addresses)
prices = [price.getText().split("+")[0].split("/")[0] for price in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
print(prices)
links = [link.get("href") for link in soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")]
print(links)
types = [type.getText().split("\n")[1:4] for type in soup.find_all(name="ul", class_="StyledPropertyCardHomeDetailsList")]
print(types)

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

driver.get(os.getenv("FORM_LINK"))
wait = WebDriverWait(driver, 5)



info = list(zip(addresses, prices, links))

for n in range(0, len(info)):
    addrs = info[n][0]
    price = info[n][1]
    lnk = info[n][2]

    message = f"This is{addrs} for price {price}, check it out: {lnk}"
    print(message)

    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "Uc2NEf")))

    address_input = driver.find_element(By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')
    address_input.click()
    address_input.send_keys(addrs)

    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.click()
    price_input.send_keys(price)


    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.click()
    link_input.send_keys(lnk)
    #
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    # if input.get("data-intial-value") is ""
    # address = div.StyledPropertyCardDataWrapper a address

    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Submit another response"))).click()