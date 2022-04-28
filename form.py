from selenium import webdriver
import time

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/u/0/d/e/1FAIpQLSenVW3MyfC0U7o1HA-dbkiApgLwtVy4rfpkiorHn_qUGV_X2A/viewform?usp=form_confirm')

time.sleep(2)

input = web.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
input.send_keys("yashwanth6675@gmail.com")

input = web.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
input.send_keys("yashu")

input = web.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
input.send_keys("19B11000")

input = web.find_element_by_xpath('//*[@id="i18"]/div[2]')
input.click()

input = web.find_element_by_xpath('//*[@id="i25"]/div[3]/div')
input.click()

input = web.find_element_by_xpath('//*[@id="i35"]/div[3]/div')
input.click()

input = web.find_element_by_xpath('//*[@id="i45"]/div[3]/div')
input.click()

input = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div/span/span')
input.click()
