# File to hold global pytest fixtures
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # before each test
    web_driver = webdriver.Chrome()
    yield web_driver
    # after each test
    web_driver.quit()
