from selenium import webdriver
from selenium.webdriver.support import expected_conditions
import time

com = []
site = webdriver.Firefox()
site.get('ytlink')

time.sleep(2)
site.find_element_by_xpath("/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a").click()
scroll_pause_time = 1
site.execute_script("window.scrollTo(0, 200);")
screen_height = site.execute_script("return window.screen.height;")
time.sleep(5)
site.execute_script("window.scrollTo(0, 1000);")
i = 1

# while True:
#     # scroll one screen height each time
#     site.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
#     i += 1
#     time.sleep(scroll_pause_time)
#     # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
#     scroll_height = site.execute_script("return document.body.scrollHeight;")
#     # Break the loop when the height we need to scroll to is larger than the total scroll height
#     if (screen_height) < scroll_height:
#         break

for com in site.find_elements_by_xpath('//*[@id="comments"]'):
    file = open("output.txt", "w")
    file.write(com.text)
    file.close()



