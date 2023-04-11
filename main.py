from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
import time
import pandas as pd

def checkCompanyPage(number, df, backlink):
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, "div.mb-30:nth-child({0})".format(str(number))).click()
    time.sleep(0.2)
    data = pd.DataFrame(
        {"Name": [driver.find_element(By.CSS_SELECTOR, ".startup-header__name").text],
        "Employees": [driver.find_element(By.CSS_SELECTOR, ".key-value-list > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > b:nth-child(1)").text],
        "Industries": [driver.find_element(By.CSS_SELECTOR, ".key-value-list > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > b:nth-child(1)").text],
        "Link": [driver.find_element(By.CSS_SELECTOR, ".text-blue-900 > b:nth-child(1)").text]}
    )
    if df.empty:
        df = data
    else:
        df = df.append(data)
    driver.get(backlink)
    return df

opts = FirefoxOptions()
#opts.add_argument("--headless")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=opts)
df = pd.DataFrame(columns=["Name", "Employees", "Industries", "Link", "Note"])

## ------ Start Browser Bot ------ ##
link = "https://thehub.io/startups?industries=robotics&numberOfEmployees=1-10&numberOfEmployees=11-50&countryCodes=DK"
driver.get(link)
driver.implicitly_wait(30)
time.sleep(0.2)
print("Website Opened")
driver.find_element(By.CSS_SELECTOR, ".coi-consent-banner__agree-button").click()
print("Cookie banner closed")
print(driver.find_element(By.CSS_SELECTOR, ".d-flex > h6:nth-child(1)").text)

# Find number of pages
driver.find_element(By.CSS_SELECTOR, "li.page-item:nth-child(9)").click()
pages = int(driver.find_element(By.CSS_SELECTOR, ".nuxt-link-exact-active").text)
print("Pages found: "+str(pages))
driver.get(link)

# Scrape pages for data
for j in range(1, pages+1):
    elements = len(driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/content/div/div/div[2]/div[2]/content/div/*"))
    for i in range(1,elements+1):
        df = checkCompanyPage(i, df, link + "&page={0}".format(str(j)))
    if j != pages:
        driver.get(link + "&page={0}".format(str(j+1)))

# Save to CSV
df.to_csv("data.csv", sep=",", header=True, index=False)
driver.quit()
