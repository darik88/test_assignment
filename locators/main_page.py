from selenium.webdriver.common.by import By


class MainPageLocators:

    FIRST_INPUT_FIELD = (By.ID, "input1")
    OPERATION_SELECT = (By.ID, "operation")
    SECOND_INPUT_FIELD = (By.ID, "input2")
    CALCULATE_BUTTON = (By.ID, "submit")
    RESULT = (By.ID, "result")
