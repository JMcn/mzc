# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

browser = webdriver.Firefox()
browser.get("https://meadjohnson-us.tmall.hk/campaign-3746-16.htm")
#browser.maximize_window()
#browser.set_window_size(2560, 1600)
now_handle = browser.current_window_handle
print now_handle
time.sleep(5)
element_map = browser.find_element_by_xpath("//map[@name='ttbva']")
element = element_map.find_elements_by_xpath("area")
img = browser.find_element_by_xpath("//img[@usemap='#ttbva']")
browser.execute_script("document.documentElement.scrollTop = 10000")
time.sleep(20)
browser.save_screenshot("mzc1.png")
try:

    browser.execute_script("arguments[0].scrollIntoView();", element_map)
    time.sleep(5)
    for b in element:
        browser.execute_script("arguments[0].scrollIntoView();", b)
        coord = b.get_attribute("coords")
        local = coord.split(',')
        browser.save_screenshot("mzc2.png")
        print coord

        # 利用计算出的x,y坐标并点击
        x = (int(local[0])+int(local[2]))/2
        y = (int(local[1])+int(local[3]))/2
        print local, x, y
        ActionChains(browser).move_by_offset(x, y).click().perform()
        print browser.title
        browser.save_screenshot("mzc3.png")
        # 只点击了第一个
        break
except:
    raise

time.sleep(5)

all_handles = browser.window_handles
for handle in all_handles:
    if handle != now_handle:
        browser.switch_to.window(handle)
        print browser.title
        time.sleep(2)
        browser.save_screenshot("mzc4.png")
        browser.close()

browser.quit()
