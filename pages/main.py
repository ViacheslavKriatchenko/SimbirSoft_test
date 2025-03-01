from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from config.locators import TaskPageLocators
from config.ConfigProvider import ConfigProvider
import allure


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
        with allure.step(f"Скролим до элемента {locator}"):
            element = self.driver.find_element(*locator)
            self.action.scroll_to_element(element).perform()

    def checkbox_checker(self, locator):
        with allure.step("Проверяем что элемент не выбран"):
            check = self.wait.until(EC.element_to_be_clickable(locator))
            if check.is_selected() is True:
                return check
            else:
                return check.click()

    def open_the_page(self):
        with allure.step(f'Открываем страницу {self.PAGE_URL}'):
            self.driver.get(self.PAGE_URL)

    def page_is_opened(self):
        self.wait.until(EC.url_to_be((self.PAGE_URL)))

    def input_data(self, locator, data):
        with allure.step(f'Вводим данные {data} в поле'):
            self.find_textarea(locator).send_keys(data)

    def radio_box_select(self, locator):
        with allure.step('Делаем выбор'):
            self.checkbox_checker(locator)

    def dropdown(self, locator):
        with allure.step('Выбираем "yes" из выпадающего списка'):
            DROPDOWN = Select(self.driver.find_element(*locator))
            DROPDOWN.select_by_value('yes')

    def count_tools(self, locator):
        with allure.step('Считаем количество элементов'):
            ul_el = self.driver.find_element(*locator)
            li_els = ul_el.find_elements(*self.Locators.TOOLS_ELEMENTS)
            return f"Количество инструментов = {len(li_els)}\n"

    def big(self, locator):
        with allure.step('Выводим самое длинное слово'):
            li_els = self.driver.find_elements(*self.Locators.TOOLS_ELEMENTS)
            tools = (el.text for el in li_els)
            longest = max(tools, key=len)
            return f'Наибольшее кол-во символов в - {longest}'

    def click(self, locator):
        with allure.step('Нажимаем на кнопку'):
            self.wait.until(EC.element_to_be_clickable(locator), message="Кнопка не найдена").click()

    def take_alert(self):
        with allure.step('Сравниваем текст alertа с шаблоном'):
            alert = self.wait.until(EC.alert_is_present())
            self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
