from pages.main import MainPage
from config.locators import TaskPageLocators
import allure

Locators = TaskPageLocators()
name = "Slava"
password = "12345"
email = "gotoauto@gmail.com"


@allure.title('Работа с полями и формами')
@allure.description('Заполняем форму, нажимаем кнопку, проверяем окно алерт')
@allure.severity(severity_level="Critical")
def test(driver):
    main = MainPage(driver)
    main.open_the_page()
    main.input_data(Locators.NAME_FIELD, data=name)
    main.input_data(Locators.PASSWORD_FIELD, data=password)
    main.radio_box_select(Locators.MILK_CHECKBOX)
    main.radio_box_select(Locators.COFFEE_CHECKBOX)
    main.scroll_to(Locators.YELLOW_BUTTON)
    main.radio_box_select(Locators.YELLOW_BUTTON)
    main.scroll_to(Locators.DROPDOWN_ELEMENT)
    main.dropdown(Locators.DROPDOWN_ELEMENT)
    main.scroll_to(Locators.EMAIL_FIELD)
    main.input_data(Locators.EMAIL_FIELD, data=email)
    main.scroll_to(Locators.MESSAGE_FIELD)
    main.input_data(Locators.MESSAGE_FIELD, data=main.count_tools(Locators.TOOLS_LIST))
    main.input_data(Locators.MESSAGE_FIELD, data=main.big(Locators.TOOLS_ELEMENTS))
    main.scroll_to(Locators.SUBMIT_BUTTON)
    main.click(Locators.SUBMIT_BUTTON)
    text = main.take_alert()
    with allure.step('Сверяем текст алерт окна с шаблоном'):
        assert text == "Message received!", "Ошибка"
