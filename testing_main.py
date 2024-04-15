import pytest
from selenium import webdriver
from utils import WebAutomationLibrary
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

@pytest.fixture(scope="class")
def driver():
    wd = webdriver.Chrome()
    yield wd
    wd.quit()

@pytest.fixture(scope="class")
def data():
    data = {
        "url": config['credentials']['url'],
        "email": config['credentials']['email'],
        "password": config['credentials']['password'],
        "name": config['input_data']['name'],
        "phone": config['input_data']['phone'],
        "address": config['input_data']['address'],
        "city": config['input_data']['city'],
        "CRBTV": config['input_data']['CRBTV'],
        "valuev": config['input_data']['valuev'],
        "wait": config['input_data']['wait']
    }
    
    print("Data from config file:", data)
    return data

class Test:
    def test_login(self, driver, data):
        web_automation = WebAutomationLibrary(driver)
        web_automation.open(data["url"])
        assert web_automation.login(data["email"], data["password"])


    def test_create_parcel(self, driver, data):
        web_automation = WebAutomationLibrary(driver)
        web_automation.open(data["url"])
        web_automation.login(data["email"], data["password"])

        parcel_created, error_message = web_automation.create_parcel(data["name"], data["phone"], data["address"], data["city"], data["CRBTV"], data["valuev"], data["wait"])
        test_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_file_path = "tests_records.csv"
        status = "Passed" if parcel_created else "Error"
        web_automation.save_to_csv(test_time, data["name"], data["phone"], data["address"], data["city"], data["CRBTV"], data["valuev"], status, error_message, output_file_path)
        assert parcel_created, f"Parcel creation failed: {error_message}"

        assert web_automation.create_parcels_in_mass(data["wait"])



    def test_confirm_cancel_print_update_parcel(self, driver, data):
        web_automation = WebAutomationLibrary(driver)
        web_automation.open(data["url"])
        web_automation.login(data["email"], data["password"])

        assert web_automation.parcel_confirmation(data["wait"])

        assert web_automation.parcel_cancellation(data["wait"])

        assert web_automation.parcel_mass_confirmation(data["wait"])

        assert web_automation.parcel_mass_print(data["wait"])

        assert web_automation.update_parcel_details(data["wait"])