'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.headless = True

driver = webdriver.Chrome(options=options)

driver.get("https://google.com/")
print(driver.title)
driver.quit()
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

options = Options()
user_data_dir = tempfile.mkdtemp() #Creates a temporary directory.
options.add_argument(f"--user-data-dir={user_data_dir}")

service = Service(ChromeDriverManager().install())
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://google.com/")
print(driver.title)

driver.quit()
import shutil
shutil.rmtree(user_data_dir) #removes the temp directory.
