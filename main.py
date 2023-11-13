from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options to run in headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Comment this line if you want to see the browser window
# chrome_options.add_argument("--disable-gpu")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the website
url = "https://onecompiler.com/cpp"
driver.get(url)

file = 'test.cpp'
file_content = ""

while True:
    with open(file , 'r') as f:
        content = f.read()
        if content != file_content:
            file_content = content
            js_code = f"let editor = ace.edit('oc_ace'); editor.setValue(`{file_content}`)"
            driver.execute_script(js_code)
    time.sleep(1)

# Inject JavaScript




prompt = input("Press enter to close");

# Wait for a while to see the changes (you may need to adjust the time based on your page load time)
# driver.implicitly_wait(5)

# Take a screenshot (optional)
# driver.save_screenshot("screenshot.png")

# Close the browser
# driver.quit()
