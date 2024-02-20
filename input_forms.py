from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df = pd.read_excel('challenge.xlsx')

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)


def fill_form(driver, key, value):
    """Заполняет поле формы, идентифицированное заданным ключом
    и соотвествующим значением."""
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         f"//label[contains(text(), '{key}')]/following-sibling::input")
        ))
    element.clear()
    element.send_keys(str(value))


def submit_form(driver):
    """Отправка формы, нажатием на кнопку отправить."""
    element = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'input[type="submit"]')
        ))
    element.click()


driver.get("https://rpachallenge.com/")

input(
    'После нажатия кнопки Start в браузере нажмите Enter для запуска программы'
    )

for _, row in df.iterrows():
    row_dict = row.to_dict()
    for key, value in row_dict.items():
        fill_form(driver, key, value)
    submit_form(driver)

driver.quit()
