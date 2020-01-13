import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def copart(driver):
    driver.get('https://copart.com')
    yield driver


def test_porsche_in_exotic_search(copart, wait):
    copart.find_element(By.XPATH, "//input[@id='input-search']").send_keys('exotics' + Keys.ENTER)
    makes = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//span[@data-uname='lotsearchLotmake' and text()='PORSCHE']")))
    assert len(makes) > 0
