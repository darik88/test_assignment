import pytest
from pages.main_page import MainPage

# correct_values = [0, 1, -1, 100, -100, 99, -99, 60, -44]


# @pytest.mark.parametrize('value', correct_values)
# @pytest.mark.parametrize('another_value', correct_values)
# def test_sum(browser, config, value, another_value):
#     page = MainPage(browser)
#     page.open_page(config["link"])
#     page.make_sum(value, another_value)


def test_sum_out_of_range_values(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(-101, 152)


def test_sum_correct_and_out_of_range_values(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(5, 152)


def test_sum_0_and_0(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(0, 0)


def test_sum_0_and_1(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(0, 1)


def test_sum_1_and_0(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(1, 0)


def test_sum_limit_negatives(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(-100, -100)


def test_sum_limit_negative_and_limit_positive(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(-100, 100)


def test_sum_0_and_limit_positive(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(0, 100)


def test_sum_limit_positive_and_0(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(100, 0)


def test_sum_negative_and_positive(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_sum(-10, 40)


# and so on
