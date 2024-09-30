import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://kodilla.com/pl/test/store")
    yield driver
    driver.quit()

def assert_amount(driver, search_term, expected_count):
    search_box = driver.find_element(By.XPATH, "//*[@id='searchField']")
    
    search_box.clear()
    
    search_box.send_keys(search_term)
    
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(2)

    results = driver.find_elements(By.XPATH, "//div[@class='element']")

    assert len(results) == int(expected_count), f"Błąd: Oczekiwano {expected_count} wyników, ale znaleziono {len(results)}."

def test_store(setup):
    driver = setup

    assert_amount(driver, "Laptop", "3")
    assert_amount(driver, "NoteBook", "2")
    assert_amount(driver, "Gaming", "1")
