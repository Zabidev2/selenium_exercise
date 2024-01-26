from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.insightly.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "nav-login"))
)

button = driver.find_element(By.ID, "nav-login")
button.click()


username = driver.find_element(By.ID, "emailaddress").send_keys("zabih9224@gmail.com")
password = driver.find_element(By.NAME, "password").send_keys("Zabi12345")
login_button = driver.find_element(By.ID, "login-button").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "navlink_task"))
)

driver.find_element(By.ID, "navlink_task").click()
time.sleep(3)
driver.find_element(By.ID, "AddNewButton").click()
time.sleep(3)
driver.find_element(By.ID, "TITLE").send_keys("Meeting")
driver.find_element(By.ID, "Task_DUE_DATE").send_keys("04-Mar-2022")
driver.find_element(By.ID, "btn-save").click()

time.sleep(5)

task_name = driver.find_element(By.ID, "entityname").text
task_id = driver.find_element(By.ID,"metadata-row-viewer-TASK_ID").text
assigned_to = driver.find_element(By.ID,"field-render-AssignedTo").text
category = driver.find_element(By.ID,"field-render-Category").text
due_date = driver.find_element(By.ID,"field-render-DateDue").text
start_date = driver.find_element(By.ID,"field-render-StartDate").text
reminder = driver.find_element(By.ID,"field-render-Reminder").text
repeat = driver.find_element(By.ID,"field-render-Repeat").text
progress = driver.find_element(By.ID,"field-render-Progress").text
priority = driver.find_element(By.ID,"field-render-Priority").text
status = driver.find_element(By.ID,"field-render-Status").text
last_updated = driver.find_element(By.ID,"field-render-LastUpdated").text
created = driver.find_element(By.ID,"field-render-TaskCreated").text
created_by = driver.find_element(By.ID,"field-render-CreatedBy").text
task_owner = driver.find_element(By.ID,"field-render-TaskOwner").text

print("-----------------------------------------")
print("Task Report")
print("----------------------------------------")
print(f"Name: {task_name}\n")
print(f"Task ID: {task_id}\n")
print(f"{assigned_to}\n")
print(f"{category}\n")
print(f"{created}\n")
print(f"{created_by}\n")
print(f"{start_date}\n")
print(f"{due_date}\n")
print(f"{reminder}\n")
print(f"{repeat}\n")
print(f"{progress}\n")
print(f"{priority}\n")
print(f"{status}\n")
print(f"{last_updated}\n")
print(f"{created_by}\n")
print(f"{task_owner}\n")
print("__________________________________________")


driver.quit()