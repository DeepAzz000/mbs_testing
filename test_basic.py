import pytest
from selenium import webdriver
from utils import WebAutomationLibrary


@pytest.fixture
def data():
    return {"url": "https://dev.mobipreshipement.link/web/login", "email": "shop99@example.com", "password": "0pxghEO2gYyQ7@U", "name": "AHMED", "phone": "+2126102030405060", "address": "Dar Ahmed", "city": "Casablanca", "CRBTV": "100", "valuev": "1000"}

@pytest.fixture(scope="class")
def driver():
    wd = webdriver.Chrome()
    yield wd
    wd.quit()

class Test:
    def test_login_and_create_parcel(self, driver, data):
            web_automation = WebAutomationLibrary(driver)
            web_automation.open(data["url"])
            assert web_automation.login(data["email"], data["password"])
            assert web_automation.create_parcel(data["name"], data["phone"], data["address"], data["city"], data["CRBTV"], data["valuev"])