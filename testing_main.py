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
    
        "url": config['credentials_shop']['url'],
        "email_shop": config['credentials_shop']['email'],
        "password_shop": config['credentials_shop']['password'],
        "email_delivery": config['credentials_delivery_person']['email'],
        "password_delivery": config['credentials_delivery_person']['password'],
        "wrong_password": config['credentials_shop']['wrong_password'],
        "wait": int(config['credentials_shop']['wait']),
        "b_name": config['base_case']['name'],
        "b_phone": config['base_case']['phone'],
        "b_address": config['base_case']['address'],
        "b_city": config['base_case']['city'],
        "b_CRBTV": config['base_case']['CRBTV'],
        "b_valuev": config['base_case']['valuev'],
        "CIN": config['base_case']['CIN'],
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
        "w_valuev3": config['wrong_case']['valuev3'],
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
        "parcel_draft_3" : config['parcels']['parcel_draft_3'],
        "parcel_different_status" : config['parcels']['parcel_different_status'],
        "parcel_picked" : config['parcels']['parcel_picked_up'],
        "parcel_wrong_barcode": config['parcels']['parcel_wrong_barcode'],
        "parcel_delivered": config['parcels']['parcel_delivered'],
        "parcel_returned": config['parcels']['parcel_returned'],
        "parcel_return": config['parcels']['parcel_return'],
        "parcel_neg_CRBTV": config['parcels']['parcel_neg_CRBTV'],
        "parcels_draft" : config['parcels']['parcels_draft'],
        "parcels_different_status" : config['parcels']['parcels_different_status'],
        "parcels_wrong_barcode": config['parcels']['parcels_wrong_barcode'],
        "parcels_delivered": config['parcels']['parcels_delivered'],
        "parcels_returned": config['parcels']['parcels_returned'],
        "parcels_return": config['parcels']['parcels_return'],
        "parcels_neg_CRBTV": config['parcels']['parcels_neg_CRBTV'],
        "one" : int(config['archive']['one']),
        "many" : int(config['archive']['many']),
        "message" : config['message']['message_input'],
        "LAD" : config['delivery_types']['LAD'],
        "LPR" : config['delivery_types']['LPR'],
        "REA" : config['delivery_types']['REA'],
        
        "LPR_N_N_VD_HD_P_P": config['Cities']['LPR_N_N_VD_HD_P_P'],
        "LPR_N_N_VD_HD_P_C": config['Cities']['LPR_N_N_VD_HD_P_C'],
        "LPR_N_N_VD_HD_C_P": config['Cities']['LPR_N_N_VD_HD_C_P'],
        "LPR_N_N_VD_HD_C_C": config['Cities']['LPR_N_N_VD_HD_C_C'],
        
        "LPR_N_N_VD_MH_P_P": config['Cities']['LPR_N_N_VD_MH_P_P'],
        "LPR_N_N_VD_MH_P_C": config['Cities']['LPR_N_N_VD_MH_P_C'],
        "LPR_N_N_VD_MH_C_P": config['Cities']['LPR_N_N_VD_MH_C_P'],
        "LPR_N_N_VD_MH_C_C": config['Cities']['LPR_N_N_VD_MH_C_C'],
        
        "LPR_N_N_MV_MH_P_P": config['Cities']['LPR_N_N_MV_MH_P_P'],
        "LPR_N_N_MV_MH_C_C": config['Cities']['LPR_N_N_MV_MH_C_C'],
        
        "LPR_N_S_VD_HD_P_P": config['Cities']['LPR_N_S_VD_HD_P_P'],
        "LPR_N_S_VD_HD_P_C": config['Cities']['LPR_N_S_VD_HD_P_C'],
        "LPR_N_S_VD_HD_C_P": config['Cities']['LPR_N_S_VD_HD_C_P'],
        "LPR_N_S_VD_HD_C_C": config['Cities']['LPR_N_S_VD_HD_C_C'],
        
        "LPR_N_S_VD_MH_P_P": config['Cities']['LPR_N_S_VD_MH_P_P'],
        "LPR_N_S_VD_MH_P_C": config['Cities']['LPR_N_S_VD_MH_P_C'],
        "LPR_N_S_VD_MH_C_P": config['Cities']['LPR_N_S_VD_MH_C_P'],
        "LPR_N_S_VD_MH_C_C": config['Cities']['LPR_N_S_VD_MH_C_C'],
        
        "LPR_S_N_VD_HD_P_P": config['Cities']['LPR_S_N_VD_HD_P_P'],
        "LPR_S_N_VD_HD_P_C": config['Cities']['LPR_S_N_VD_HD_P_C'],
        "LPR_S_N_VD_HD_C_P": config['Cities']['LPR_S_N_VD_HD_C_P'],
        "LPR_S_N_VD_HD_C_C": config['Cities']['LPR_S_N_VD_HD_C_C'],
        
        "LPR_S_N_VD_MH_P_P": config['Cities']['LPR_S_N_VD_MH_P_P'],
        "LPR_S_N_VD_MH_P_C": config['Cities']['LPR_S_N_VD_MH_P_C'],
        "LPR_S_N_VD_MH_P_P": config['Cities']['LPR_S_N_VD_MH_P_P'],
        "LPR_S_N_VD_MH_C_C": config['Cities']['LPR_S_N_VD_MH_C_C'],
        
        "LPR_S_S_MV_MH_C_C": config['Cities']['LPR_S_S_MV_MH_C_C'],
        
        "LAD_N_N_VD_HD_P_P": config['Cities']['LAD_N_N_VD_HD_P_P'],
        "LAD_N_N_VD_HD_P_C": config['Cities']['LAD_N_N_VD_HD_P_C'],
        "LAD_N_N_VD_HD_C_P": config['Cities']['LAD_N_N_VD_HD_C_P'],
        "LAD_N_N_VD_HD_C_C": config['Cities']['LAD_N_N_VD_HD_C_C'],
        
        "LAD_N_N_VD_MH_P_P": config['Cities']['LAD_N_N_VD_MH_P_P'],
        "LAD_N_N_VD_MH_P_C": config['Cities']['LAD_N_N_VD_MH_P_C'],
        "LAD_N_N_VD_MH_C_P": config['Cities']['LAD_N_N_VD_MH_C_P'],
        "LAD_N_N_VD_MH_C_C": config['Cities']['LAD_N_N_VD_MH_C_C'],
        
        "LAD_N_N_MV_MH_P_P": config['Cities']['LAD_N_N_MV_MH_P_P'],
        "LAD_N_N_MV_MH_C_C": config['Cities']['LAD_N_N_MV_MH_C_C'],
        
        "LAD_N_S_VD_HD_P_P": config['Cities']['LAD_N_S_VD_HD_P_P'],
        "LAD_N_S_VD_HD_P_C": config['Cities']['LAD_N_S_VD_HD_P_C'],
        "LAD_N_S_VD_HD_C_P": config['Cities']['LAD_N_S_VD_HD_C_P'],
        "LAD_N_S_VD_HD_C_C": config['Cities']['LAD_N_S_VD_HD_C_C'],
        
        "LAD_N_S_VD_MH_P_P": config['Cities']['LAD_N_S_VD_MH_P_P'],
        "LAD_N_S_VD_MH_P_C": config['Cities']['LAD_N_S_VD_MH_P_C'],
        "LAD_N_S_VD_MH_C_P": config['Cities']['LAD_N_S_VD_MH_C_P'],
        "LAD_N_S_VD_MH_C_C": config['Cities']['LAD_N_S_VD_MH_C_C'],
        
        "LAD_S_N_VD_HD_P_P": config['Cities']['LAD_S_N_VD_HD_P_P'],
        "LAD_S_N_VD_HD_P_C": config['Cities']['LAD_S_N_VD_HD_P_C'],
        "LAD_S_N_VD_HD_C_P": config['Cities']['LAD_S_N_VD_HD_C_P'],
        "LAD_S_N_VD_HD_C_C": config['Cities']['LAD_S_N_VD_HD_C_C'],
        
        "LAD_S_N_VD_MH_P_P": config['Cities']['LAD_S_N_VD_MH_P_P'],
        "LAD_S_N_VD_MH_P_C": config['Cities']['LAD_S_N_VD_MH_P_C'],
        "LAD_S_N_VD_MH_P_P": config['Cities']['LAD_S_N_VD_MH_P_P'],
        "LAD_S_N_VD_MH_C_C": config['Cities']['LAD_S_N_VD_MH_C_C'],
        
        "LAD_S_S_MV_MH_C_C": config['Cities']['LAD_S_S_MV_MH_C_C'],
        
        "REA_": config['Cities']['REA_'],
        
        "city1": config['Cities']['city1'],
        "city2": config['Cities']['city2'],
        "city3": config['Cities']['city3'],
        "city4": config['Cities']['city4'],
        "city5": config['Cities']['city5'],
        "city6": config['Cities']['city6'],
    }
    return data

@pytest.fixture(scope="function")
def setup_web_automation_shop(driver, data):
    web_automation = WebAutomationLibrary(driver)
    web_automation.open(data["url"])
    web_automation.login(data["email_shop"], data["password_shop"])
    return web_automation

@pytest.fixture(scope="function")
def setup_web_automation_delivery(driver, data):
    web_automation = WebAutomationLibrary(driver)
    web_automation.open(data["url"])
    web_automation.login(data["email_delivery"], data["password_delivery"])
    return web_automation

#TESTS:

# LOGIN TESTS:
def test_login(driver, data):
    web_automation = WebAutomationLibrary(driver)
    web_automation.open(data["url"])
    assert web_automation.login(data["email_shop"], data["password_shop"])
def test_login(driver, data):
    web_automation = WebAutomationLibrary(driver)
    web_automation.open(data["url"])
    assert web_automation.login(data["email_shop"], data["wrong_password"])

# CREATE PARCEL(S) TESTS:
def test_create_parcel_base_case_LAD(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["LAD"], data["CIN"])
def test_create_parcel_missing_name_LAD(setup_web_automation_shop, data):
    # Missing info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["m_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["LAD"], data["CIN"])
def test_create_parcel_missing_address_LAD(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["w_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["LAD"], data["CIN"])
def test_create_parcel_wrong_city_LAD(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["w_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["LAD"], data["CIN"])
def test_create_parcel_wrong_crbtv_fc_LAD(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return 
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["w_CRBTV1"], data["b_valuev"], data["wait"], data["LAD"], data["CIN"])
    # Expected (that the CRBTV should not be negative) #reality: the parcel is created with a negative crbtv
def test_create_parcel_wrong_crbtv_sc_LAD(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["w_CRBTV2"], data["b_valuev"], data["wait"], data["LAD"], data["CIN"])
def test_create_parcel_wrong_value_fc_LAD(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev1"], data["wait"], data["LAD"], data["CIN"])
def test_create_parcel_wrong_value_sc_LAD(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev2"], data["wait"], data["LAD"], data["CIN"])
def test_create_parcel_wrong_value_tc_LAD(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev3"], data["wait"], data["LAD"], data["CIN"])

def test_create_parcel_base_case_LPR(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["LPR"], data["CIN"])
def test_create_parcel_missing_name_LPR(setup_web_automation_shop, data):
    # Missing info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["m_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["LPR"], data["CIN"])
def test_create_parcel_missing_address_LPR(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["w_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["LPR"], data["CIN"])
def test_create_parcel_wrong_city_LPR(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["w_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["LPR"], data["CIN"])
def test_create_parcel_wrong_crbtv_fc_LPR(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return 
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["w_CRBTV1"], data["b_valuev"], data["wait"], data["LPR"], data["CIN"])
    # Expected (that the CRBTV should not be negative) #reality: the parcel is created with a negative crbtv
def test_create_parcel_wrong_crbtv_sc_LPR(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["w_CRBTV2"], data["b_valuev"], data["wait"], data["LPR"], data["CIN"])
def test_create_parcel_wrong_value_fc_LPR(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev1"], data["wait"], data["LPR"], data["CIN"])
def test_create_parcel_wrong_value_sc_LPR(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev2"], data["wait"], data["LPR"], data["CIN"])

def test_create_parcel_base_case_REA(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["REA"], data["CIN"])
def test_create_parcel_missing_name_REA(setup_web_automation_shop, data):
    # Missing info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["m_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["REA"], data["CIN"])
def test_create_parcel_missing_address_REA(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["w_address"], data["b_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["REA"], data["CIN"])
def test_create_parcel_wrong_city_REA(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["w_city"], data["b_CRBTV"], data["b_valuev"], data["wait"], data["REA"], data["CIN"])
def test_create_parcel_wrong_crbtv_fc_REA(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return 
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["w_CRBTV1"], data["b_valuev"], data["wait"], data["REA"], data["CIN"])
    # Expected (that the CRBTV should not be negative) #reality: the parcel is created with a negative crbtv
def test_create_parcel_wrong_crbtv_sc_REA(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["w_CRBTV2"], data["b_valuev"], data["wait"], data["REA"], data["CIN"])
def test_create_parcel_wrong_value_fc_REA(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev1"], data["wait"], data["REA"], data["CIN"])
def test_create_parcel_wrong_value_sc_REA(setup_web_automation_shop, data):
    # wrong info case: the test should pass and return errors
    assert setup_web_automation_shop.create_parcel(data["b_name"], data["b_phone"], data["b_address"], data["b_city"], data["b_CRBTV"], data["w_valuev2"], data["wait"], data["REA"], data["CIN"])

def test_create_parcels_in_mass_correct_file(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.create_parcels_in_mass(data["wait"], data["upload_file_c"])
def test_create_parcels_in_mass_incorrect_file1(setup_web_automation_shop, data):
    # Incorrect file case (no partner barcode): the test should pass and return errors
    assert setup_web_automation_shop.create_parcels_in_mass(data["wait"], data["upload_file_w1"])
def test_create_parcels_in_mass_incorrect_file2(setup_web_automation_shop, data):
    # Incorrect file case(missing city): the test should pass and return errors
    assert setup_web_automation_shop.create_parcels_in_mass(data["wait"], data["upload_file_w2"])
def test_create_parcels_in_mass_incorrect_file3(setup_web_automation_shop, data):
    # Incorrect file case (missing COD): the test should pass and return errors
    assert setup_web_automation_shop.create_parcels_in_mass(data["wait"], data["upload_file_w3"])

# CANCEL PARCEL TESTS:
def test_cancel_correct_parcel(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_cancellation(data["wait"], data['parcel_draft_1'])
def test_cancel_already_cancel_parcel(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_cancellation(data["wait"], data['parcel_draft_2'])
def test_cancel_already_confirmed_parcel(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_cancellation(data["wait"], data['parcel_confirmed'])

# CONFIRM PARCEL(S) TESTS:
def test_confirm_correct_parcel(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_confirmation(data["wait"], data['parcel_draft_1'])
def test_confirm_already_confirmed_parcel(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_confirmation(data["wait"], data['parcel_draft_1'])
def test_confirm_already_canceled_parcel(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_confirmation(data["wait"], data['parcel_draft_2'])

def test_confirm_in_mass_parcel(setup_web_automation_shop, data):
    #Confirm mass parcels: the list of parcels is mixed between confirmed canceled drafted parcels test should pass
    assert setup_web_automation_shop.parcel_mass_confirmation(data["wait"])

# PRINT TICKET(S) TESTS:
def test_print_parcel_ticket_100x70(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_ticket_print(data["wait"], data['ticket-100X70'])
def test_print_parcel_ticket_A4(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_ticket_print(data["wait"], data['ticket-A4'])
def test_print_parcels_tickets_in_mass_100x70(setup_web_automation_shop, data):    
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_ticket_mass_print(data["wait"], data['ticket-100X70'])
def test_print_parcels_tickets_in_mass_A4(setup_web_automation_shop, data):    
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.parcel_ticket_mass_print(data["wait"], data['ticket-A4'])

# UPDATE PARCEL (S) DETAILS TESTS:
def test_update_parcel(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.update_parcel_details(data["wait"])

# ARCHIVE PARCEL(S)
def test_archive_parcel_confirmed_draft(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.archive_parcel(data["wait"], data["parcel_draft_1"], data["one"])
def test_archive_parcel_cancelled(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.archive_parcel(data["wait"], data["parcel_draft_2"], data["one"])
def test_archive_parcel_mixed_parcels(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.archive_parcel(data["wait"], data["parcel_draft_1"], data["many"])

#SEND MESSAGE
def test_send_message(setup_web_automation_shop, data):
    # Base case: the test should pass and return no errors
    assert setup_web_automation_shop.send_message(data["wait"], data["parcel_draft_1"], data["message"])


#DELIVERY PERSON

# PICKUP PARCEL:
def test_pickup_parcel_base_case(setup_web_automation_delivery, data):
    # Base case (pickup a parcel draft or confirmed): the test should pass and return no errors 
    assert setup_web_automation_delivery.pickup_parcel(data["wait"], data["parcel_draft_3"])
    # Expected: the parcel status changes to picked up
def test_pickup_parcel_different_status_case(setup_web_automation_delivery, data):
    # Base case (pickup a parcel already loaded or picked up): the test should pass and return no errors 
    assert setup_web_automation_delivery.pickup_parcel(data["wait"], data["parcel_different_status"])
    # Expected: the parcel status changes to picked
def test_pickup_parcel_wrong_barcode(setup_web_automation_delivery, data):
    # wrong case (pickup a draft with wrong_barcode): the test should pass and return an errors
    assert setup_web_automation_delivery.pickup_parcel(data["wait"], data["parcel_wrong_barcode"])
    # Expected: return a notification with a message stating that the barcode is wrong
def test_pickup_parcel_already_delivered(setup_web_automation_delivery, data):
    # Already delivered case (pickup a draft with wrong_barcode): the test should pass and return no errors
    assert setup_web_automation_delivery.pickup_parcel(data["wait"], data["parcel_delivered"])
    # Expected: return a notification with a message stating that the parcel is already delivered
#PICKUP PARCELS:
def test_pickup_parcels_base_case(setup_web_automation_delivery, data):
    # Base case (pickup parcels draft or confirmed): the test should pass and return no errors 
    assert setup_web_automation_delivery.pickup_parcel(data["wait"], data["parcels_draft"])
    # Expected: the parcels status changes to picked up
def test_pickup_parcels_different_status_case(setup_web_automation_delivery, data):
    # Base case (pickup parcels already loaded or picked up): the test should pass and return no errors 
    assert setup_web_automation_delivery.pickup_parcel(data["wait"], data["parcels_different_status"])
    # Expected: the parcels status changes to picked
def test_pickup_parcels_wrong_barcode(setup_web_automation_delivery, data):
    # wrong case (pickup draft parcels with wrong_barcode): the test should pass and return an errors
    assert setup_web_automation_delivery.pickup_parcel(data["wait"], data["parcels_wrong_barcode"])
    # Expected: return a notification with a message stating that the barcode is wrong
def test_pickup_parcels_already_delivered(setup_web_automation_delivery, data):
    # Already delivered case (pickup draft parcels with wrong_barcode): the test should pass and return no errors
    assert setup_web_automation_delivery.pickup_parcel(data["wait"], data["parcels_delivered"])
    # Expected: return a notification with a message stating that the parcel is already delivered

#LOAD PARCEL:
def test_load_parcel_base_case(setup_web_automation_delivery, data):
    # Base case (load a parcel picked): the test should pass and return no errors
    assert setup_web_automation_delivery.load_parcel(data["wait"], data["parcel_picked"])
    # Expected: the parcel status changes to loaded
def test_load_parcel_different_status_case(setup_web_automation_delivery, data):
    # Base case (pickup a parcel already loaded or picked up): the test should pass and return no errors 
    assert setup_web_automation_delivery.load_parcel(data["wait"], data["parcel_different_status"]) 
    # Expected: the parcel status changes to loaded
def test_load_parcel_wrong_barcode(setup_web_automation_delivery, data):
    # Wrong case (load a parcel with wrong barcode): the test should fail and return errors
    assert setup_web_automation_delivery.load_parcel(data["wait"], data["parcel_wrong_barcode"])
    # Expected: return a notification with a message stating that the barcode is wrong
def test_load_parcel_already_delivered(setup_web_automation_delivery, data):
    # Already delivered case (try to load a parcel that has already been delivered): the test should fail and return errors
    assert setup_web_automation_delivery.load_parcel(data["wait"], data["parcel_delivered"])
    # Expected: return a notification with a message stating that the parcel is already delivered
#LOAD PARCELS:
def test_load_parcels_base_case(setup_web_automation_delivery, data):
    # Base case (load a parcel picked): the test should pass and return no errors
    assert setup_web_automation_delivery.load_parcel(data["wait"], data["parcels_picked"])
    # Expected: the parcel status changes to loaded
def test_load_parcels_different_status_case(setup_web_automation_delivery, data):
    # Base case (pickup a parcel already loaded or picked up): the test should pass and return no errors 
    assert setup_web_automation_delivery.load_parcel(data["wait"], data["parcels_different_status"]) 
    # Expected: the parcel status changes to loaded
def test_load_parcels_wrong_barcode(setup_web_automation_delivery, data):
    # Wrong case (load a parcel with wrong barcode): the test should fail and return errors
    assert setup_web_automation_delivery.load_parcel(data["wait"], data["parcels_wrong_barcode"])
    # Expected: return a notification with a message stating that the barcode is wrong
def test_load_parcels_already_delivered(setup_web_automation_delivery, data):
    # Already delivered case (try to load a parcel that has already been delivered): the test should fail and return errors
    assert setup_web_automation_delivery.load_parcel(data["wait"], data["parcels_delivered"])
    # Expected: return a notification with a message stating that the parcel is already delivered

#DELIVER PARCEL:
def test_deliver_parcel_base_case(setup_web_automation_delivery, data):
    # Base case (deliver a parcel draft or confirmed): the test should pass and return no errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcel_draft_3"])
    assert success
    # Expected: the parcel status changes to delivered
def test_deliver_parcel_different_status_case(setup_web_automation_delivery, data):
    # Base case (deliver a parcel picked): the test should pass and return no errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcel_different_status"])
    assert success
    # Expected: the parcel status changes to delivered
def test_deliver_parcel_wrong_barcode(setup_web_automation_delivery, data):
    # Wrong case (deliver a parcel with wrong barcode): the test should fail and return errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcel_wrong_barcode"])
    assert success
    # Expected: return a notification with a message stating that the barcode is wrong
def test_deliver_parcel_already_delivered(setup_web_automation_delivery, data):
    # Already delivered case (try to deliver a parcel that has already been delivered): the test should fail and return errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcel_delivered"])
    assert success
    # Expected: return a notification with a message stating that the parcel is already delivered
def test_deliver_parcel_with_negative_CRBTV(setup_web_automation_delivery, data):
    # Parcel with negative CRBTV case: the test should pass and return no errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcel_neg_CRBTV"])
    assert success
    # Expected: return a notification with a message stating that the parcel has a negative and cannot be delivered
#DELIVER PARCELS:
def test_deliver_parcels_base_case(setup_web_automation_delivery, data):
    # Base case (deliver a parcel draft or confirmed): the test should pass and return no errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcels_draft"])
    assert success
    # Expected: the parcel status changes to delivered
def test_deliver_parcels_different_status_case(setup_web_automation_delivery, data):
    # Base case (deliver a parcel picked): the test should pass and return no errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcels_different_status"])
    assert success
    # Expected: the parcel status changes to delivered
def test_deliver_parcels_wrong_barcode(setup_web_automation_delivery, data):
    # Wrong case (deliver a parcel with wrong barcode): the test should fail and return errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcels_wrong_barcode"])
    assert success
    # Expected: return a notification with a message stating that the barcode is wrong
def test_deliver_parcels_already_delivered(setup_web_automation_delivery, data):
    # Already delivered case (try to deliver a parcel that has already been delivered): the test should fail and return errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcels_delivered"])
    assert success
    # Expected: return a notification with a message stating that the parcel is already delivered
def test_deliver_parcels_with_negative_CRBTV(setup_web_automation_delivery, data):
    # Parcel with negative CRBTV case: the test should pass and return no errors
    success, _ = setup_web_automation_delivery.deliver_parcel(data["wait"], data["parcels_neg_CRBTV"])
    assert success
    # Expected: return a notification with a message stating that the parcel has a negative and cannot be delivered

#RETURN PARCEL:
def test_return_parcel_and_check_status_base_case(setup_web_automation_delivery, setup_web_automation_shop, data):
    # Base case (return a parcel draft or confirmed or any): the test should pass and return no errors
    setup_web_automation_delivery.open(data["url"])
    setup_web_automation_delivery.login(data["email_delivery"], data["password_delivery"])
    parcel_number = setup_web_automation_delivery.return_parcel(data["wait"], data["parcel_return"])
    setup_web_automation_shop.open(data["url"])
    setup_web_automation_shop.login(data["email_shop"], data["password_shop"])
    assert setup_web_automation_shop.check_status(data["wait"], parcel_number)
    # Expected: the parcel status changes to returned
def test_return_parcel_and_check_status_returned(setup_web_automation_delivery, setup_web_automation_shop, data):
    # Already returned case (return a parcel already returned): the test should pass and return no errors
    setup_web_automation_delivery.open(data["url"])
    setup_web_automation_delivery.login(data["email_delivery"], data["password_delivery"])
    parcel_number = setup_web_automation_delivery.return_parcel(data["wait"], data["parcel_returned"])
    setup_web_automation_shop.open(data["url"])
    setup_web_automation_shop.login(data["email_shop"], data["password_shop"])
    assert setup_web_automation_shop.check_status(data["wait"], parcel_number)
    # Expected: return a notification with a message stating that the parcel is already returned
def test_return_parcel_and_check_status_delivered(setup_web_automation_delivery, setup_web_automation_shop, data):
    # Delivered case (return a parcel already returned): the test should pass and return no errors
    setup_web_automation_delivery.open(data["url"])
    setup_web_automation_delivery.login(data["email_delivery"], data["password_delivery"])
    parcel_number = setup_web_automation_delivery.return_parcel(data["wait"], data["parcel_return"])
    setup_web_automation_shop.open(data["url"])
    setup_web_automation_shop.login(data["email_shop"], data["password_shop"])
    assert setup_web_automation_shop.check_status(data["wait"], parcel_number)
    # Expected: return a notification with a message stating that the parcel is already delivered and cannot ba returned
#RETURN PARCELS:
def test_return_parcels_and_check_status_base_case(setup_web_automation_delivery, setup_web_automation_shop, data):
    # Base case (return a parcel draft or confirmed or any): the test should pass and return no errors
    setup_web_automation_delivery.open(data["url"])
    setup_web_automation_delivery.login(data["email_delivery"], data["password_delivery"])
    parcel_number = setup_web_automation_delivery.return_parcel(data["wait"], data["parcels_return"])
    setup_web_automation_shop.open(data["url"])
    setup_web_automation_shop.login(data["email_shop"], data["password_shop"])
    assert setup_web_automation_shop.check_status(data["wait"], parcel_number)
    # Expected: the parcel status changes to returned
def test_return_parcels_and_check_status_returned(setup_web_automation_delivery, setup_web_automation_shop, data):
    # Already returned case (return a parcel already returned): the test should pass and return no errors
    setup_web_automation_delivery.open(data["url"])
    setup_web_automation_delivery.login(data["email_delivery"], data["password_delivery"])
    parcel_number = setup_web_automation_delivery.return_parcel(data["wait"], data["parcels_returned"])
    setup_web_automation_shop.open(data["url"])
    setup_web_automation_shop.login(data["email_shop"], data["password_shop"])
    assert setup_web_automation_shop.check_status(data["wait"], parcel_number)
    # Expected: return a notification with a message stating that the parcel is already returned
def test_return_parcels_and_check_status_delivered(setup_web_automation_delivery, setup_web_automation_shop, data):
    # Delivered case (return a parcel already Delivered): the test should pass and return no errors
    setup_web_automation_delivery.open(data["url"])
    setup_web_automation_delivery.login(data["email_delivery"], data["password_delivery"])
    parcel_number = setup_web_automation_delivery.return_parcel(data["wait"], data["parcels_return"])
    setup_web_automation_shop.open(data["url"])
    setup_web_automation_shop.login(data["email_shop"], data["password_shop"])
    assert setup_web_automation_shop.check_status(data["wait"], parcel_number)
    # Expected: return a notification with a message stating that the parcel is already delivered and cannot ba returned

# COD TESTS:
def test_cod_base_case(setup_web_automation_delivery, data):
    # Base case (deliver a parcel that is not already delivered): the test should pass and return no errors 
    assert setup_web_automation_delivery.cod(data["wait"], data["parcel_draft_3"])
    # Expected: the CRBT after adding COD matches the displayed CRBT total
def test_cod_already_delivered_case(setup_web_automation_delivery, data):
    # Already delivered case (deliver a parcel that is delivered): the test should pass and return no errors 
    assert setup_web_automation_delivery.cod(data["wait"], data["parcel_draft_3"])
    # Expected: No matching or checking because parcel already delivered

# FEES TESTs:

def test_fees_LPR_N_N_VD_HD_P_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city4"], data["city2"], data["LPR_N_N_VD_HD_P_C"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_N_N_VD_HD_C_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city2"], data["city3"], data["LPR_N_N_VD_HD_C_P"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_N_N_VD_HD_C_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city3"], data["city1"], data["LPR_N_N_VD_HD_C_C"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_N_N_VD_MH_P_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city5"], data["city2"], data["LPR_N_N_VD_MH_P_P"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_N_N_VD_MH_P_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city1"], data["city2"], data["LPR_N_N_VD_MH_P_C"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_N_N_VD_MH_C_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city2"], data["city1"], data["LPR_N_N_VD_MH_C_P"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_N_N_MV_MH_P_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city2"], data["city2"], data["LPR_N_N_MV_MH_P_P"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_N_S_VD_HD_P_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city6"], data["city2"], data["LPR_N_S_VD_HD_P_C"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_S_N_VD_HD_C_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city2"], data["city6"], data["LPR_S_N_VD_HD_C_P"], data["wait"], data["LPR"], data["CIN"])
def test_fees_LPR_S_S_MV_MH_C_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city6"], data["city6"], data["LPR_S_S_MV_MH_C_C"], data["wait"], data["LPR"], data["CIN"])

def test_fees_LAD_N_N_VD_HD_P_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city4"], data["city2"], data["LAD_N_N_VD_HD_P_C"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_N_N_VD_HD_C_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city2"], data["city3"], data["LAD_N_N_VD_HD_C_P"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_N_N_VD_HD_C_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city3"], data["city1"], data["LAD_N_N_VD_HD_C_C"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_N_N_VD_MH_P_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city5"], data["city2"], data["LAD_N_N_VD_MH_P_P"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_N_N_VD_MH_P_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city1"], data["city2"], data["LAD_N_N_VD_MH_P_C"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_N_N_VD_MH_C_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city2"], data["city1"], data["LAD_N_N_VD_MH_C_P"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_N_N_MV_MH_P_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city2"], data["city2"], data["LAD_N_N_MV_MH_P_P"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_N_S_VD_HD_P_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city6"], data["city2"], data["LAD_N_S_VD_HD_P_C"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_S_N_VD_HD_C_P(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city2"], data["city6"], data["LAD_S_N_VD_HD_C_P"], data["wait"], data["LAD"], data["CIN"])
def test_fees_LAD_S_S_MV_MH_C_C(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city6"], data["city6"], data["LAD_S_S_MV_MH_C_C"], data["wait"], data["LAD"], data["CIN"])

def test_fees_REA(setup_web_automation_shop, data):
    assert setup_web_automation_shop.fees_check(data["b_name"], data["b_phone"], data["b_address"], data["city6"], data["city6"], data["REA_"], data["wait"], data["REA"], data["CIN"])