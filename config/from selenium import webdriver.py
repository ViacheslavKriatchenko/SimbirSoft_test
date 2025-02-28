from selenium import webdriver
import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


driver = webdriver.Chrome()
driver.get("https://practice-automation.com/form-fields/")
TOOLS_LIST = ('xpath', '//label/following-sibling::ul')
TOOLS_ELEMENTS = ('xpath', '//label/following-sibling::ul/li')
el = driver.find_element(*TOOLS_LIST)
els = el.find_elements(*TOOLS_ELEMENTS)
lst = (el.text for el in els)
longest = max(lst, key=len)
print(longest)
# for i in range(len(els)):
#     print(els[i].text)
