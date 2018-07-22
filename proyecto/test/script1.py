# Download Chrome driver from: http://chromedriver.chromium.org/downloads
# Create a Python Project with its corresponding virtual environment
# What kind of libraries do you think we might need? List them
# Install libraries
# Create a script with the following steps:
# Open Chrome browser
# Go to Redmine
# Login into the application
# Capture each web element locator and assign them into a variable
# Instantiate Webelements
# Interact with the system through weblements.
# Bonus track:
# Check you are logged in (try to use assertion)




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Open Chrome browser
driver = webdriver.Chrome(executable_path ="C:\\Users\\cguzman\\Documents\\GitHub\\python\\proyecto\\binarios\\chromedriver.exe")
driver.set_page_load_timeout(20)
wait = WebDriverWait(driver, 10)

driver.get("http://127.0.0.1:81/redmine/")
driver.maximize_window()
driver.implicitly_wait(20)
# Login into the application
login = driver.find_element_by_link_text("Sign in")
login.click()

username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")
submit_button = driver.find_element_by_id("login-submit")

username_field.send_keys("user")
password_field.send_keys("password")
submit_button.click()

# Check you are logged in (try to use assertion)
loggeduser = driver.find_element_by_xpath('//*[@id="loggedas"]/a').text
assert loggeduser == 'user'

projects_link = driver.find_element_by_class_name("projects")
projects_link.click()

# Capture each web element locator and assign them into a variable
home_link = driver.find_element_by_class_name("home")
home_link.click()
page_link = driver.find_element_by_class_name("my-page")
page_link.click()
administration_link = driver.find_element_by_class_name("administration")
administration_link.click()
help_link = driver.find_element_by_class_name("help")
account_link = driver.find_element_by_class_name("my-account")
search_link = driver.find_element_by_xpath('//*[@id="q"]')
logout_link = driver.find_element_by_class_name("logout")
logout_link.click()






driver.close()
driver.quit()