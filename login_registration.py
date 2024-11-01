# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(20)
# Account = driver.find_element_by_css_selector("#menu-item-50 a")
# Account.click()
# time.sleep(5)
# Email_field = driver.find_element_by_id("reg_email")
# Email_field.send_keys("ivanjulius@mail.com")
# Password_field = driver.find_element_by_id("reg_password")
# Password_field.send_keys("321AbH135")
# driver.find_element_by_name("register").click()
# driver.quit()

#Проверить последний пункт
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(20)
driver.find_element_by_link_text("My Account").click()
time.sleep(5)
Username_field = driver.find_element_by_id("username")
Username_field.send_keys("ivanjulius@mail.com")
Password_field = driver.find_element_by_id("password")
Password_field.send_keys("321AbH135")
driver.find_element_by_name("login").click()
Logout = driver.find_element_by_link_text("Logout") # нашли элемент по составному селектору
logout_text = Logout.text # добавили новую переменную и получили текст элемента с помощью .text
assert "Logout" in logout_text # добавили проверку, что слово "Logout" есть в тексте
#driver.quit()

