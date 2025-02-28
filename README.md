# SimbirSoft_test

## Практикум SDET: Тестовое задание
Создать проект UI-автотестов по тест-кейсам

### Шаги:
1. Склонировать репозитой "git clone https://github.com/ViacheslavKriatchenko/Sky_final_Auto.git"
2. Запустить виртуальное окружение "python -m venv venv"
3. Установить окружение "python -m pip install -r requirements.txt"
4. Запустить тесты "pytest -s -v --alluredir allure_results"
5. Просмотреть отчет "allure serve allure_results"

### Стэк:
- Selenium
- Webdriver-manager
- Requests
- PyTest
- Allure

### Структура:
- ./config - настройка конфигурации
    - locators.py - класс локаторов
    - ConfigProvider.py - глобальные настройки
- ./pages - описание страниц сайта
- ./tests - тесты
    - test_UI.py - UI тесты
- conftest.py - фикстуры
- global_options.ini - глобальные переменные
- pytest.ini - настройка тестов
- requirements.txt - настройка окружения
- user_data.json - пользовательские данные

### Полезные ссылки:
[Гайд по Markdown](https://www.markdownguide.org/basic-syntax/)  
[Сайт генератор .gitignore](https://www.toptal.com/developers/gitignore)  
[Перенос окружения](https://pip.pypa.io/en/stable/cli/pip_freeze/)  
[Вызов PyTest инструкция](https://pytest-docs-ru.readthedocs.io/ru/latest/usage.html)

### Библиотеки:
- pip install selenium
- pip install webdriver-manager
- pip install pytest
- pip install requests
- pip install allure-pytest
