import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito --no-sandbox")   
driver = webdriver.Chrome(executable_path='C:/Users/josea/AppData/Roaming/Python/Python37/site-packages/selenium/webdriver/chrome/chromedriver', chrome_options=chrome_options)
driver.get('https://www.surveymonkey.com/r/K8GRR6N')
time.sleep(3) 
vote_check = driver.find_element_by_xpath("//label[@for='255734041_1733326514']")
vote_check.click()
time.sleep(3) 
nxt_btn = driver.find_element_by_xpath("//button[contains(text(), ' LISTO')]")
nxt_btn.click() 
driver.quit()

id="settingsMenuBtn"
id="managePersonalStorage"
# <span ng-bind="viewModel.tryItFreeText">Try Pro for free</span>
# <input type="button" value="Start trial" class="undefined primary">
# <input type="button" value="Close" class="undefined primary">