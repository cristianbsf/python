# Login into the Redmine
# Click on Project Link
# Click on “New Project”
# Complete the following fields:
# Name
# Description
# Identifier
# Uncheck “public”
# Select a Default Assignee
# Go to Modules tab
# On Modules tab, leave checked only “Issue Tracking” and “Time Tracking”
# Click on Create button and Save
# Bonus Track:

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

# Click on “New Project”
new_project_link = driver.find_element_by_xpath('//*[@id="content"]/div[1]/a')
new_project_link.click()

# Click on “New Project”
project_name = driver.find_element_by_id('project_name')
project_description= driver.find_element_by_id("project_description")
project_identifier = driver.find_element_by_id("project_identifier")
project_is_public = driver.find_element_by_id("project_is_public")

project_name.send_keys("test")
project_description.send_keys("test")
project_is_public.click()

# On Modules tab, leave checked only “Issue Tracking” and “Time Tracking”
news_checkbox = driver.find_element_by_id("project_enabled_module_names_news")
docs_checkbox = driver.find_element_by_id("project_enabled_module_names_documents")
file_checkbox = driver.find_element_by_id("project_enabled_module_names_files")
wiki_checkbox = driver.find_element_by_id("project_enabled_module_names_wiki")
repo_checkbox = driver.find_element_by_id("project_enabled_module_names_repository")
boar_checkbox = driver.find_element_by_id("project_enabled_module_names_boards")
cale_checkbox = driver.find_element_by_id("project_enabled_module_names_calendar")
gant_checkbox = driver.find_element_by_id("project_enabled_module_names_gantt")

news_checkbox.click()
docs_checkbox.click()
file_checkbox.click()
wiki_checkbox.click()
repo_checkbox.click()
boar_checkbox.click()
cale_checkbox.click()
gant_checkbox.click()

# Click on Create button and Save
create_button = driver.find_element_by_name('commit')
create_button.click()

logout_link = driver.find_element_by_class_name("logout")
logout_link.click()

wait = WebDriverWait(driver, 10)

driver.close()
driver.quit()