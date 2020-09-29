from pages.main_page import MainPage


def test_subtraction(browser, config):
    page = MainPage(browser)
    page.open_page(config["link"])
    page.make_subtraction(10, 100)


# TODO: complete tests for subtraction operations
