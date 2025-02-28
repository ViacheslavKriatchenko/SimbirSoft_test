from pages.main import MainPage
import time
import pytest
from config.locators import TaskPageLocators

Locators = TaskPageLocators()
name = "Slava"
password = "12345"
email = "gotoauto@gmail.com"


def test(driver):
    main = MainPage(driver)
    main.open_the_page()
    main.input_data(Locators.NAME_FIELD, data=name)
    #main.input_data(Locators.PASSWORD_FIELD, data=password)
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
    time.sleep(5)
