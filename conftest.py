import pytest
from selenium import webdriver
from data import Site


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Site.main_site)

    yield driver
    driver.quit()