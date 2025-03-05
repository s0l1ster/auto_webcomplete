from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

# Set up WebDriver
chrome_driver_path = r"C:\Users\Vasya\Desktop\win32\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("http://localhost:8000/index.html")
#mail_field = driver.find_element(By.NAME, "email")  # Locate by the "name" attribute
#mail_field.send_keys("levosyykillya@gmail.com")  # Enter the email

# Fill in the password field
#password_field = driver.find_element(By.NAME, "password")  # Locate by the "name" attribute
#password_field.send_keys("456123mnB)")  # Enter the password

#time.sleep(10)

#submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")  # Locate button by class
#submit_button.click()


time.sleep(10)


#button = driver.find_element(By.CLASS_NAME, "btn-primary")  # Locate button by class
#button.click()

try:
    while True:
        with open(r"C:\Users\Vasya\PycharmProjects\pythonProject5\script_things\scripts.txt", "r") as file:
            # Read the latest content from the file
            file_content = file.read()
        
        # Execute the script
        driver.execute_script(file_content)
        
        # Wait for a while before reading the file again (e.g., 5 seconds)
        time.sleep(10)
        submit_button = driver.find_element(By.NAME, "savebutton")  # Locate button by class
        submit_button.click()
        time.sleep(10)
        submit_button_back = driver.find_element(By.NAME, "goback")  # Locate button by class
        submit_button_back.click()

except KeyboardInterrupt:
    print("Program stopped manually.")

# Clean up
