# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(20)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(10)
# Username_field = driver.find_element_by_id("username")
# Username_field.send_keys("ivanjulius@mail.com")
# Password_field = driver.find_element_by_id("password")
# Password_field.send_keys("321AbH135")
# driver.find_element_by_name("login").click()
# driver.find_element_by_css_selector("#menu-item-40  a").click()
# HTML5_img = driver.find_element_by_css_selector(".post-181 .attachment-shop_catalog")
# HTML5_img.click()
# html5_forms = driver.find_element_by_class_name("product_title.entry-title")
# html5_forms_text = html5_forms.text
# assert html5_forms_text == "HTML5 Forms"
# driver.quit()


#вторая задача пункт 44
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(20)
driver.find_element_by_css_selector("#menu-item-50 a").click()
#driver.find_element_by_link_text("My Account").click()
time.sleep(10)
Username_field = driver.find_element_by_id("username")
Username_field.send_keys("ivanjulius@mail.com")
Password_field = driver.find_element_by_id("password")
Password_field.send_keys("321AbH135")
driver.find_element_by_name("login").click()
driver.find_element_by_css_selector("#menu-item-40  a").click()
time.sleep(10)
driver.find_element_by_link_text("HTML").click()
time.sleep(10)
#HTML_count = driver.find_elements(By.CSS_SELECTOR, "cat-item.cat-item-19.current-cat .count")
#HTML_count = driver.find_elements_by_class_name("cat-item.cat-item-19.current-cat .count")
#some_element= (WebDriverWait(driver, 10).until
#( EC.text_to_be_present_in_element((By.CSS_SELECTOR, "cat-item.cat-item-19.current-cat .count"), "(3)")))

#HTML_count_text = HTML_count.text
#Print(HTML_count_text)
#assert "3" in HTML_count_text
# ###items_count = driver.find_elements_by_class_name("products.masonry-done") # находим список всех элементов в корзине
#items_count = driver.find_elements_by_class_name("woocommerce-breadcrumb") # находим список всех элементов в корзине
#проверка что в корзине действительно 3 товара (добавьте в конец теста)
#HTML_count = driver.find_elements_by_link_text("(3)") # находим список всех элементов в корзине
HTML_count = driver.find_elements_by_css_selector(".cat-item.cat-item-19 .count") # находим список всех элементов в корзине
#HTML_count = driver.find_elements_by_css_selector(".cat-item.cat-item-19")
#HTML_count = driver.find_elements_by_css_selector(".products.masonry-done")
if len(HTML_count) == 3: # после 1-го урока можем теперь создать небольшую конструкцию для проверки кол-ва товаров
    print("отображается 3 товара") # len здесь посчитает количество элементов, найденных при помощи find_elements
else:
    print("Ошибка. Количество товаров: " + str(len(HTML_count)))
time.sleep(5)
#driver.quit()


#третья задача
#import time
#from selenium import webdriver
#driver = webdriver.Chrome()
#driver.maximize_window()
#driver.get("https://practice.automationtesting.in/")
#time.sleep(20)
#driver.find_element_by_link_text("My Account").click()
#time.sleep(10)
#Username_field = driver.find_element_by_id("username")
#Username_field.send_keys("ivanjulius@mail.com")
#Password_field = driver.find_element_by_id("password")
#Password_field.send_keys("321AbH135")
#driver.find_element_by_name("login").click()
#driver.find_element_by_css_selector("#menu-item-40  a").click()
#time.sleep(10)
#Sort_window_selector_Default_sorting = driver.find_element_by_css_selector(".orderby :nth-child(1)")
#Sort_window_selector_Default_sorting_select = Sort_window_selector_Default_sorting.get_attribute("selected") #создали переменную, в которую поместим значение атрибута
#if Sort_window_selector_Default_sorting_select is None: #проверяем, если значение атрибута пустое, значит его нет
       #print("Выбрано неверное значение фильтра")
#else: print('Выбрано значение "Default sorting"')
#from selenium.webdriver.support.select import Select # импортируем класс Select из библиотеки webdriver
#Price_max_min = driver.find_element_by_class_name("orderby") # "element" это просто название переменной, можно задать и другое
#select_price_max_min = Select(Price_max_min) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
#select_price_max_min.select_by_value("price-desc") # ищем элемент с текстом "price-desc" ; в этом и предыдущем методе добавлять .click() не нужно
#Sort_window_selector_high_to_low = driver.find_element_by_css_selector(".orderby :nth-child(6)")
#Sort_window_selector_high_to_low_select = Sort_window_selector_high_to_low.get_attribute("selected") #создали переменную, в которую поместим значение атрибута
#if Sort_window_selector_high_to_low_select is None: #проверяем, если значение атрибута пустое, значит его нет
       #print("Выбрано неверное значение фильтра")
#else: print('Выбрано значение "Sort by price: high to low"')
#driver.quit()


#четвертая задача
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(20)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(10)
# Username_field = driver.find_element_by_id("username")
# Username_field.send_keys("ivanjulius@mail.com")
# Password_field = driver.find_element_by_id("password")
# Password_field.send_keys("321AbH135")
# driver.find_element_by_name("login").click()
# driver.find_element_by_css_selector("#menu-item-40  a").click()
# time.sleep(10)
# driver.find_element_by_css_selector(".post-169 .attachment-shop_catalog").click()
# time.sleep(10)
# alt_price = driver.find_element_by_css_selector("del .amount")
# alt_price_text = alt_price.text #получили текст элемента с помощью.text
# assert alt_price_text == "₹600.00", "отсутствует удаленная цена - ₹600.00 " # добавили проверку что содержимое равно ожидаемому
# time.sleep(10)
# print(alt_price_text)
# new_price = driver.find_element_by_css_selector("ins .amount")
# new_price_text = new_price.text #получили текст элемента с помощью.text
# assert new_price_text == "₹450.00"  # добавили проверку что содержимое равно ожидаемому
# time.sleep(10)
# img_book = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-main-image.zoom")) )
# img_book.click()
# img_book_close = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
# img_book_close.click()
# time.sleep(10)
#driver.quit()

#Пятая задача
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(20)
# driver.find_element_by_css_selector("#menu-item-40  a").click()
# time.sleep(10)
# Add_to_basket = driver.find_element_by_tag_name('[data-product_id="182"]')
# Add_to_basket.click()
# time.sleep(10)
# basket = driver.find_element_by_class_name("cartcontents")
# basket_text = basket.text #получили текст элемента с помощью.text
# assert basket_text == "1 Item"# добавили проверку что содержимое равно ожидаемому
# time.sleep(10)
# price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# price_text = price.text #получили текст элемента с помощью.text
# assert price_text == "₹180.00"# добавили проверку что содержимое равно ожидаемому
# time.sleep(10)
# View_Basket = driver.find_element_by_class_name("added_to_cart.wc-forward")
# View_Basket.click()
# basket_totals= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "₹180.00"))
# total= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "₹183.60"))
# driver.quit()

#Шестая задача
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(20)
# driver.find_element_by_css_selector("#menu-item-40  a").click()
# time.sleep(10)
# driver.execute_script("window.scrollBy(0, 300)")
# Add_to_basket = driver.find_element_by_tag_name('[data-product_id="182"]')
# Add_to_basket.click()
# time.sleep(10)
# Add_to_basket_book = driver.find_element_by_tag_name('[data-product_id="180"]')
# Add_to_basket_book.click()
# time.sleep(10)
# View_Basket = driver.find_element_by_class_name("added_to_cart.wc-forward")
# View_Basket.click()
# time.sleep(10)
# close_btn_1 = driver.find_element_by_tag_name('[data-product_id="182"]')
# close_btn_1.click()
# time.sleep(10)
# undo = driver.find_element_by_css_selector(".woocommerce-message a")
# undo.click()
# time.sleep(10)
# driver.find_element_by_name(name="cart[045117b0e0a11a242b9765e79cbf113f][qty]").clear()
# quantity = driver.find_element_by_name(name="cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# quantity.send_keys("3")
# update_basket = driver.find_element_by_name("update_cart")
# update_basket.click()
# quantity_books = driver.find_element_by_name(name="cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# quantity_books_val = quantity_books.get_attribute("value")
# assert quantity_books_val == "3"
# time.sleep(10)
# coupon = driver.find_element_by_name("apply_coupon")
# coupon.click()
#
# #alert = driver.switch_to.alert
# #alert_expected_text = "Please enter a coupon code."
# #alert_text = alert.text
#
# alert_script = driver.execute_script("alert('Please enter a coupon code.');") # вызываем окно alert
# alert = driver.switch_to.alert # переключаемся в область окна alert; обратите внимание, “()” после switch_to.alert не нужны
# alert_text = alert.text # получаем текст с помощью команды .text
# print(alert_text) # выводим содержимое в консоли
# alert.accept()
# driver.quit()


# Седьмая задача
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(20)
# driver.find_element_by_css_selector("#menu-item-40  a").click()
# time.sleep(10)
# driver.execute_script("window.scrollBy(0, 300)")
# Add_to_basket = driver.find_element_by_tag_name('[data-product_id="182"]')
# Add_to_basket.click()
# time.sleep(10)
# View_Basket = driver.find_element_by_class_name("added_to_cart.wc-forward")
# View_Basket.click()
# time.sleep(10)
# proceed_to_checkout_btn = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")) )
# proceed_to_checkout_btn.click()
# name = WebDriverWait(driver, 20).until( # говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
#  EC.element_to_be_clickable((By.ID, "billing_first_name")) )
# name.send_keys("Ivan")
# Last_Name = driver.find_element_by_id("billing_last_name")
# Last_Name.send_keys("Ivanov")
# Email_Address = driver.find_element_by_id("billing_email")
# Email_Address.send_keys("ivanjulius@mail.com")
# Phone = driver.find_element_by_id("billing_phone")
# Phone.send_keys("345788")
# Address = driver.find_element_by_id("billing_address_1")
# Address.send_keys("Lomona")
# Address_2 = driver.find_element_by_id("billing_address_2")
# Address_2.send_keys("53")
# Town = driver.find_element_by_id("billing_city")
# Town.send_keys("Guwahati")
# State = driver.find_element_by_id("s2id_billing_state")
# State.click()
#
# State_1 = driver.find_element_by_id("s2id_autogen2_search")
# State_1.send_keys("Assam")
# driver.find_element_by_css_selector(".select2-result-label .select2-match").click()
#
# time.sleep(10)
# Postcode_value = driver.find_element_by_id("billing_postcode") #вводим индекс почты
# Postcode_value.send_keys("400600")
# time.sleep(10)
# driver.execute_script("window.scrollBy(0, 600)") #проскролим страницу на 600 пикселей
# Check_Payments = driver.find_element_by_id("payment_method_cheque") #выбор значения радиобаттон
# Check_Payments.click()
# time.sleep(10)
#
# place_order_btn = driver.find_element_by_id("place_order") #нажмем кнопку place_order
# place_order_btn.click()
#
# driver.quit()



