from selenium import webdriver
import pytest
import json
import platform


CONFIG_PATH = "./configs/config.json"


@pytest.fixture()
def browser():
    browser = None
    if platform.system() == "Darwin":
        browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
    elif platform.system() == "Windows":
        browser = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
    else:
        raise pytest.UsageError("You should have Mac or Win PC with installed Chrome browser to run tests")
    yield browser
    browser.quit()


@pytest.fixture()
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
        return data

