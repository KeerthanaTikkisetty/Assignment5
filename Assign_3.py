# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()


# Navigating to the Amazon.ca homepage
driver.get("https://www.youtube.com/")
time.sleep(3)

# all_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[1]/yt-icon-button[2]/button/yt-icon/yt-icon-shape/icon-shape/div")
# all_button.click()


trending = driver.find_element("xpath","/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item/yt-formatted-string")
trending.click()

time.sleep(3)


movies_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[4]/div/div[1]")
movies_button.click()

time.sleep(5)


select_vid= driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img")
select_vid.click()
time.sleep(2)

# Clicking on Pause button
pause_button= driver.find_element("xpath","//*[@id='movie_player']/div[27]/div[2]/div[1]/button")
pause_button.click()
time.sleep(2)

# Clicking on Play button
play_button= driver.find_element("xpath","//*[@id='movie_player']/div[27]/div[2]/div[1]/button")
play_button.click()
time.sleep(5)


driver.close()
