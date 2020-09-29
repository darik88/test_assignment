from .base_page import BasePage
from locators.main_page import MainPageLocators
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):

    def fill_first_input(self, value):
        self.find_element(MainPageLocators.FIRST_INPUT_FIELD).send_keys(value)

    def fill_second_input(self, value):
        self.find_element(MainPageLocators.SECOND_INPUT_FIELD).send_keys(value)

    def press_calculate(self):
        calculate_button = self.find_element(MainPageLocators.CALCULATE_BUTTON)
        calculate_button.click()

    def select_operation_add(self):
        select = Select(self.find_element(MainPageLocators.OPERATION_SELECT))
        select.select_by_visible_text("Add")

    def select_operation_subtract(self):
        select = Select(self.find_element(MainPageLocators.OPERATION_SELECT))
        select.select_by_visible_text("Subtract")

    def select_operation_multiply(self):
        select = Select(self.find_element(MainPageLocators.OPERATION_SELECT))
        select.select_by_visible_text("Multiply")

    def select_operation_divide(self):
        select = Select(self.find_element(MainPageLocators.OPERATION_SELECT))
        select.select_by_visible_text("Divide")

    def get_result(self):
        result = self.find_element(MainPageLocators.RESULT).text
        return result

    def make_sum(self, value, another_value):
        self.fill_first_input(value)
        self.select_operation_add()
        self.fill_second_input(another_value)
        self.press_calculate()
        result = self.get_result()
        assert result == str(value + another_value), \
            f"Correct result of {value} + {another_value} is {value + another_value}"

    def make_subtraction(self, value, another_value):
        self.fill_first_input(value)
        self.select_operation_subtract()
        self.fill_second_input(another_value)
        self.press_calculate()
        result = self.get_result()
        assert result == str(value - another_value), \
            f"Correct result of {value} - {another_value} is {value - another_value}"

    def make_multiplication(self, value, another_value):
        self.fill_first_input(value)
        self.select_operation_multiply()
        self.fill_second_input(another_value)
        self.press_calculate()
        result = self.get_result()
        assert result == str(value * another_value), \
            f"Correct result of {value} * {another_value} is {value * another_value}"

    def make_division(self, value, another_value):
        self.fill_first_input(value)
        self.select_operation_divide()
        self.fill_second_input(another_value)
        self.press_calculate()
        result = self.get_result()
        assert result == str(value / another_value), \
            f"Correct result of {value} / {another_value} is {value / another_value}"
