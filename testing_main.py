import pytest
from selenium import webdriver
from utils import WebAutomationLibrary
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

@pytest.fixture(scope="function")
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
        "wrong_password": config['credentials']['wrong_password'],
        "wait": int(config['credentials']['wait']),
        "b_name": config['base_case']['name'],
        "b_phone": config['base_case']['phone'],
        "b_address": config['base_case']['address'],
        "b_city": config['base_case']['city'],
        "b_CRBTV": config['base_case']['CRBTV'],
        "b_valuev": config['base_case']['valuev'],
        "m_name": config['missing_case']['name'],
        "m_phone": config['missing_case']['phone'],
        "m_address": config['missing_case']['address'],
        "m_city": config['missing_case']['city'],
        "m_CRBTV": config['missing_case']['CRBTV'],
        "m_valuev": config['missing_case']['valuev'],
        "w_address": config['wrong_case']['address'],
        "w_city": config['wrong_case']['city'],
        "w_CRBTV1": config['wrong_case']['CRBTV1'],
        "w_CRBTV2": config['wrong_case']['CRBTV2'],
        "w_valuev1": config['wrong_case']['valuev1'],
        "w_valuev2": config['wrong_case']['valuev2'],
        "upload_file_c": config['upload_file']['upload_file_c'],
        "upload_file_w1": config['upload_file']['upload_file_w1'],
        "upload_file_w2": config['upload_file']['upload_file_w2'],
        "upload_file_w3": config['upload_file']['upload_file_w3'],
        "ticket-A4": int(config['ticket']['A4']),
        "ticket-100X70": int(config['ticket']['100X70']),
        "parcel_confirmed" : int(config['parcels']['parcel_confirmed']),
        "parcel_canceled" : int(config['parcels']['parcel_canceled']),
        "parcel_draft_1" : int(config['parcels']['parcel_draft_1']),
        "parcel_draft_2" : int(config['parcels']['parcel_draft_2']),
        "one" : int(config['archive']['one']),
        "many" : int(config['archive']['many']),
        "message" : config['message']['message_input'],
        
    }
    return data

@pytest.fixture(scope="function")
def setup_web_automation(driver, data):
    web_automation = WebAutomationLibrary(driver)
    web_automation.open(data["url"])
    web_automation.login(data["email"], data["password"])
    return web_automation

#TESTS:

# LOGIN TESTS:
def test_login(driver, data):
    web_automation = WebAutomationLibrary(driver)
    web_automation.open(data["url"])
    assert web_automation.login(data["email"], data["password"])
def test_login(driver, data):
    web_automation = WebAutomationLibrary(driver)
    web_automation.open(data["url"])
    assert web_automation.login(data["email"], data["wrong_password"])

# CREATE PARCEL(S) TESTS:
def test_create_parcel_base_case(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"])
def test_create_parcel_missing_name(setup_web_automation, data):
    # Missing info case: the test should pass and return errors
    assert setup_web_automation.create_parcel(data["m_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"])
def test_create_parcel_missing_address(setup_web_automation, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation.create_parcel(data["b_name"], data["b_phone"], data["w_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"])
def test_create_parcel_wrong_city(setup_web_automation, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["w_city"], data["b_CRBTV"], data["b_valuev"], data["wait"])
def test_create_parcel_wrong_crbtv_fc(setup_web_automation, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["w_CRBTV1"], data["b_valuev"], data["wait"])
def test_create_parcel_wrong_crbtv_sc(setup_web_automation, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["w_CRBTV2"], data["b_valuev"], data["wait"])
def test_create_parcel_wrong_value_fc(setup_web_automation, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev1"], data["wait"])
def test_create_parcel_wrong_value_sc(setup_web_automation, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev2"], data["wait"])
def test_create_parcels_in_mass_correct_file(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.create_parcels_in_mass(data["wait"], data["upload_file_c"])
def test_create_parcels_in_mass_incorrect_file1(setup_web_automation, data):
    # Incorrect file case (no partner barcode): the test should pass and return errors
    assert setup_web_automation.create_parcels_in_mass(data["wait"], data["upload_file_w1"])
def test_create_parcels_in_mass_incorrect_file2(setup_web_automation, data):
    # Incorrect file case(missing city): the test should pass and return errors
    assert setup_web_automation.create_parcels_in_mass(data["wait"], data["upload_file_w2"])
def test_create_parcels_in_mass_incorrect_file3(setup_web_automation, data):
    # Incorrect file case (missing COD): the test should pass and return errors
    assert setup_web_automation.create_parcels_in_mass(data["wait"], data["upload_file_w3"])

# CANCEL PARCEL TESTS:
def test_cancel_correct_parcel(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.parcel_cancellation(data["wait"], data['parcel_draft_1'])
def test_cancel_already_cancel_parcel(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.parcel_cancellation(data["wait"], data['parcel_draft_2'])
def test_cancel_already_confirmed_parcel(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.parcel_cancellation(data["wait"], data['parcel_confirmed'])

# CONFIRM PARCEL(S) TESTS:
def test_confirm_correct_parcel(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.parcel_confirmation(data["wait"], data['parcel_draft_1'])
def test_confirm_already_confirmed_parcel(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.parcel_confirmation(data["wait"], data['parcel_draft_1'])
def test_confirm_already_canceled_parcel(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.parcel_confirmation(data["wait"], data['parcel_draft_2'])

def test_confirm_in_mass_parcel(setup_web_automation, data):
    #Confirm mass parcels: the list of parcels is mixed between confirmed canceled drafted parcels test should pass
    assert setup_web_automation.parcel_mass_confirmation(data["wait"])

# PRINT TICKET(S) TESTS:
def test_print_parcel_ticket(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.parcel_ticket_print(data["wait"], data['ticket-100X70'])
def test_print_parcels_tickets_in_mass(setup_web_automation, data):    
    # Base case: the test should pass and return no errors
    assert setup_web_automation.parcel_ticket_mass_print(data["wait"], data['ticket-A4'])

# UPDATE PARCEL (S) DETAILS TESTS:
def test_update_parcel(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.update_parcel_details(data["wait"])

# ARCHIVE PARCEL(S)
def test_archive_parcel_confirmed_draft(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.archive_parcel(data["wait"], data["parcel_draft_1"], data["one"])
def test_archive_parcel_cancelled(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.archive_parcel(data["wait"], data["parcel_draft_2"], data["one"])
def test_archive_parcel_mixed_parcels(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.archive_parcel(data["wait"], data["parcel_draft_1"], data["many"])

#SEND MESSAGE
def test_send_message(setup_web_automation, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation.send_message(data["wait"], data["parcel_draft_1"], data["message"])
