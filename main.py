from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import compiler_strategy

# Set up Chrome options to run in headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Comment this line if you want to see the browser window
# chrome_options.add_argument("--disable-gpu")

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the website

file = 'test1.rs'
file_content = ""

def read_exnt(file_name):
    return file_name.split('.')[-1]

strategy = compiler_strategy.Programize()


url = strategy.generate_url(read_exnt(file))

driver.get(url)



while True:
    with open(file , 'r') as f:
        content = f.read()
        if content != file_content:
            file_content = content
            js_code = strategy.js_code(file_content)
            driver.execute_script(js_code)
    time.sleep(1)



prompt = input("Press enter to close");

driver.quit()
