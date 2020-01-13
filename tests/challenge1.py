import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def google(driver):
    driver.get('https://google.com')
    yield driver


def test_google_title(google):
    assert 'Google' in google.title


def test_google_search(google):
    google.find_element(By.NAME, 'q').send_keys('puppies')
    google.find_element(By.NAME, 'btnK').submit()
    assert 'puppies' in google.title
