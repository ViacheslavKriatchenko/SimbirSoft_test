from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from config.locators import TaskPageLocators
from config.ConfigProvider import ConfigProvider


class MainPage:

    data = ConfigProvider()
    Locators = TaskPageLocators()
    PAGE_URL = data.get(section='test_data', prop='URL')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        self.action = ActionChains(driver)

    def find_textarea(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to(self, locator):
        element = self.driver.find_element(*locator)
        self.action.scroll_to_element(element).perform()

    def checkbox_checker(self, locator):
        check = self.wait.until(EC.element_to_be_clickable(locator))
        if check.is_selected() is True:
            return check
        else:
            return check.click()

    def open_the_page(self):
        self.driver.get(self.PAGE_URL)

    def page_is_opened(self):
        self.wait.until(EC.url_to_be((self.PAGE_URL)))

    def input_data(self, locator, data):
        self.find_textarea(locator).send_keys(data)

    def radio_box_select(self, locator):
        self.checkbox_checker(locator)

    def dropdown(self, locator):
        DROPDOWN = Select(self.driver.find_element(*locator))
        DROPDOWN.select_by_value('yes')

    def count_tools(self, locator):
        ul_el = self.driver.find_element(*locator)
        li_els = ul_el.find_elements(*self.Locators.TOOLS_ELEMENTS)
        return f"Количество инструментов = {len(li_els)}\n"

    def big(self, locator):
        li_els = self.driver.find_elements(*self.Locators.TOOLS_ELEMENTS)
        tools = (el.text for el in li_els)
        longest = max(tools, key=len)
        return f'Наибольшее кол-во символов в - {longest}'
