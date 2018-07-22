# Login into the Redmine
# Click on Project Link
# Select an existing project
# Go to Settings tab
# Go to member
# On Members tab create a new member:
# Non member user
# Role: Reporter
# Bonus Track:
# Check if User was created successfully
# Create Page Objects for each page

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

# Enter project page
projects_link = driver.find_element_by_class_name("projects")
projects_link.click()

# Select an existing project
existing_project_link=driver.find_element_by_xpath('//*[@id="projects-index"]/ul/li[1]/div/a')
existing_project_link.click()

# Go to Settings tab
settings_link=driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[12]/a')
settings_link.click()

# Go to member
tab_member_link=driver.find_element_by_id('tab-members')
tab_member_link.click()

# On Members tab create a new member:
create_member_link=driver.find_element_by_css_selector('#tab-content-members > p:nth-child(1) > a')
create_member_link.click()

# Non member user
non_member_user=driver.find_element_by_css_selector('#principals > label:nth-child(2) > input[type="checkbox"]')
non_member_user.click()

# Role: Reporter
reporter_link=driver.find_element_by_css_selector('#new_membership > fieldset:nth-child(3) > div > label:nth-child(3) > input[type="checkbox"]')
reporter_link.click()

add_new_user=driver.find_element_by_id('member-add-submit')
add_new_user.click()

# Check if User was created successfully
created_user= driver.find_element_by_xpath('//*[@id="member-4"]/td[1]').text
assert created_user == 'Non member users'

# Create Page Objects for each page... in progress

wait = WebDriverWait(driver, 10)
logout_link = driver.find_element_by_class_name("logout")
logout_link.click()
driver.close()
driver.quit()