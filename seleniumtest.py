from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs" , prefs)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/macbook/Desktop/chromedriver')

driver.get("https://vi-vn.facebook.com/")

text = driver.find_element_by_xpath('//*[@id="email"]')

password = driver.find_element_by_xpath('//*[@id="pass"]')

text.send_keys('ndkhanh09090901@gmail.com')

password.send_keys('nothepassword')

clicking = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

print(driver.title)

n_list = ["jm1wdb64"]

cu_list = ["_1mf" , "_1mj" , "notranslate", "_5rpu"]

for i in n_list:
    
    try:
        
        clicking_newfeed = driver.find_element_by_class_name(i).click()
        
        print(i)
        
    except NoSuchElementException or ElementClickInterceptedException:
        
        print("Khong Nhan Duoc")
        
for j in cu_list:
    
    try:
        
        text_box = driver.find_element_by_class_name(j)
        
        print(j)
        
        text_box.send_keys("khanh khong co cu hehe")
        
        break
        
        
    except NoSuchElementException or ElementClickInterceptedException:
        
        print("NHAN KHONG DUOC")
    
post_status = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div').click()
