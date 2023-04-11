from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

import time
import locale
from datetime import date

import pandas as pd

opts = FirefoxOptions()
#opts.add_argument("--headless")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=opts)

# Get Previous Data
#csv_path = "/home/aw/projects/britt_frost_vand/temperatur.csv"
#df = pd.read_csv(csv_path, sep=",")

## ------ Start Browser Bot ------ ##
driver.get(
    "https://thehub.io/startups?industries=robotics&numberOfEmployees=1-10&numberOfEmployees=11-50&countryCodes=DK")
driver.implicitly_wait(30)
time.sleep(0.2)
print("Website Opened")
entries = driver.find_element(By.CSS_SELECTOR, ".d-flex > h6:nth-child(1)").text
print(entries)
card = driver.find_element(By.CSS_SELECTOR, "div.mb-30:nth-child({0})".format("2")).click()






# input_lat = driver.find_element(By.ID, "txtCoordinateLat")
# input_lat.clear()
# input_lat.send_keys(locale.format_string("%.8f", gps_lat))
# input_long = driver.find_element(By.ID, "txtCoordinateLon")
# input_long.clear()
# input_long.send_keys(locale.format_string("%.8f", gps_long))
# input_data_from = driver.find_element(By.ID, "datePickFrom_dateInput")
# input_data_from.clear()
# input_data_from.send_keys(today.strftime("%d-%m-%Y"))
# input_data_to = driver.find_element(By.ID, "datePickTo_dateInput")
# input_data_to.clear()
# input_data_to.send_keys(today.strftime("%d-%m-%Y"))
# radio_soil = driver.find_element(By.ID, "chkParameters_3").click()
# btn_update = driver.find_element(By.ID, "Button1").click()
# 
# while (time.time() < time.time()+30):
#     soil_temp = driver.find_element(
#         By.XPATH, "//*[@id='GridView1']/tbody/tr[2]/td[7]").text
#     if (soil_temp != "Nan"):
#         break
# soil_temp_float = locale.atof(soil_temp)
# driver.quit()
# 
# df.to_csv(csv_path, sep=",", header=True, index=False)
# print("Temperatur: {:.02f} °C".format(soil_temp_float))

#function getCompanyInfo():

