class TaskPageLocators:
    "Класс локаторов страницы"

    NAME_FIELD = ("id", "name-input")
    PASSWORD_FIELD = ("xpath", '//input[@type="password"]')
    CHECHBOXEX = ("xpath", '//input[@type="checkbox"]')
    MILK_CHECKBOX = ("xpath", '//input[@type="checkbox" and @value="Milk"]')
    COFFEE_CHECKBOX = ("xpath", '//input[@type="checkbox" and @value="Coffee"]')
    RADIOBUTTONS = ("xpath", '//input[@type="radio"]')
    YELLOW_BUTTON = ("xpath", '//input[@type="radio" and @value="Yellow"]')
    SELECTS = ("xpath", '//select[@name="automation"]')
    EMAIL_FIELD = ("xpath", '//input[@id="email"]')
    DROPDOWN_ELEMENT = ("xpath", '//select[@id="automation"]')
    MESSAGE_FIELD = ("css selector", 'textarea[name=message]')
    TOOLS_LIST = ("xpath", "//label/following-sibling::ul")
    TOOLS_ELEMENTS = ("xpath", "//label/following-sibling::ul/li")
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit-btn"]')
