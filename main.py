from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from dosya import parola,K_adi

driver = webdriver.Chrome()
driver.get(
    "https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoidHIifQ%3D%3D%22%7D")
time.sleep(10)
giris = driver.find_element_by_tag_name("input").send_keys(K_adi)
driver.find_element_by_tag_name("input").send_keys(Keys.RETURN)
time.sleep(3)
sifre = driver.find_element_by_name("password").send_keys(parola)
driver.find_element_by_name("password").send_keys(Keys.RETURN)
time.sleep(5)
for i in range(1, 10):
    twit = driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/span")
    twit.send_keys(". #deprem ", i)
    time.sleep(4)
    at = driver.find_element_by_xpath(
        "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
    at.click()
    time.sleep(4)
