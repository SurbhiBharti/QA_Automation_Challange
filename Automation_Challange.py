from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Firefox(executable_path="E:/SurbhiLearning/Automation/Python/Webdriver Installation Setup/geckodriver-v0.24.0-win64/geckodriver.exe")

driver.get("http://automationpractice.com")
driver.maximize_window()
driver.find_element_by_class_name("login").click()   # Click Signup
driver.implicitly_wait(5)
print("User should be navigated to Registration page")

# Create Random EmailID (Scenario 1)
e2 = random.randint(1, 500)
e3 = "testaccount@abc.com"
email = str(e2)+e3
print("Random EmailID generated: " + email)
driver.find_element_by_id("email_create").send_keys(email)
driver.find_element_by_css_selector("#SubmitCreate > span").click()

# Your Personal Information - Registration
driver.find_element_by_id("uniform-id_gender2").click()
driver.find_element_by_name("customer_firstname").send_keys("Surbhi")
driver.find_element_by_name("customer_lastname").send_keys("Bharti")
driver.find_element_by_name("email")
driver.find_element_by_name("passwd").send_keys("Google123")

#Your Address Section
driver.find_element_by_id("firstname").send_keys("Surbhi")
driver.find_element_by_id("lastname").send_keys("Bharti")
driver.find_element_by_id("address1").send_keys("St. Austins lane")
driver.find_element_by_id("city").send_keys("Warrington")

# Dropdown Element
elem = driver.find_element_by_id("id_state")
drop = Select(elem)
drop.select_by_visible_text("Florida")

driver.find_element_by_id("postcode").send_keys("98789")
driver.find_element_by_id("id_country").send_keys("United States")
driver.find_element_by_id("phone_mobile").send_keys("09873465556")
driver.find_element_by_id("alias").send_keys("My Address")
driver.find_element_by_css_selector("#submitAccount > span").click()
driver.find_element_by_class_name("logout").click()

#login(Scenario 2)
driver.find_element_by_class_name("login").click()
time.sleep(5)

# Sign In with the account created
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("passwd").send_keys("Google123")
driver.find_element_by_css_selector("#SubmitLogin > span").click()

# Add Item to the cart (Scenario 3)
driver.find_element_by_class_name("sf-with-ul").click() #Choose Product
driver.find_element_by_css_selector("#center_column > ul > li:nth-child(5) > div > div.left-block > div > a.product_img_link > img").click() # Click Image
driver.find_element_by_css_selector("#add_to_cart > button > span").click()   # Click Add to cart button
print("Selected Product : "+driver.find_element_by_id("product_reference").text)    # Print SKU Id of the product
time.sleep(2)

'''
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)'''

driver.get("http://automationpractice.com/index.php?controller=cart")

driver.find_element_by_xpath("//*[@id='header']/div[3]/div/div/div[3]/div/a").click() # Click on cart
print("Product in Cart: "+driver.find_element_by_class_name("cart_ref").text) # Print SKU Id of the product

driver.close()
driver.quit()

