#next is to import keyboard inputs such as enter and stuff
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #delay programme by x time to prevent driver from closing immediately
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#error handling by including exceptions and user interface by inputting actions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.myanimelist.net/')

# search = driver.find_element_by_id("topSearchText")

# search.click()

# search = driver.find_element_by_id("topSearchText")
# search.send_keys("demon slayer")
# search.send_keys(Keys.ENTER)

#Navigation to Top Anime from myanimelist

actions = ActionChains(driver)
anime = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]/a")
topanime = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]/ul/li[2]/a")
actions.move_to_element(anime).click(topanime).perform()



# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]/a"))
#     )

#     actions.move_to_element(topanime).click()

# except NoSuchElementException:
# 	pass

# finally:
# 	driver.quit()

    
#     topanime = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]/a")
#     topanime.click()
    







