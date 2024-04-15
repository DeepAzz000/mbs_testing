import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv

class WebAutomationLibrary:
    def __init__(self, driver=None):
        self.driver = driver or webdriver.Chrome()
        self.log = logging.getLogger(__name__)

    def open(self, url):
        self.driver.get(url)
        self.log.info("Opened URL: %s", url)

    def login(self, email, password):
        try:
            email_input = self.driver.find_element(By.ID, "login")
            email_input.send_keys(email)
            self.log.info("Email entered")

            password_input = self.driver.find_element(By.ID, "password")
            password_input.send_keys(password)
            self.log.info("Password entered")

            login_button = self.driver.find_element(By.XPATH, "//*[@id='wrapwrap']/main/div/div/div/form/div[3]/button")
            login_button.click()
            self.log.info("Login button clicked")

            login_successful = self.driver.current_url != "https://dev.mobipreshipement.link/web/login"

            if login_successful:
                self.log.info("Login successful")
                return True
            else:
                self.log.error("Login failed: Invalid credentials")
                return False

        except Exception as e:
            self.log.error("Error logging in: %s", str(e))
            return False

    def create_parcel(self, name, phone, address, city, CRBTV, valuev, wait):
        try:
            parent_element = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'o_menu_sections')))
            self.log.info("Parent element found")

            link = parent_element.find_elements(By.TAG_NAME, 'a')[1]
            href_create_parcel = link.get_attribute('href')
            self.driver.get(href_create_parcel)
            main_info = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
            self.log.info("Creation page found")

            delivery_type_button = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Livraison à domicile']")))
            delivery_type_button.click()
            self.log.info("Delivery type selected")

            next_button = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-value='next']")))
            next_button.click()
            self.log.info("Next button clicked")

            name_input = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='child_name' and contains(@class, 'o_address_street')])[1]")))
            name_input.send_keys(name)
            self.log.info("Name input filled")

            phone_input = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='child_phone' and contains(@class, 'o_address_street')])[1]")))
            phone_input.send_keys(phone)
            self.log.info("Phone input filled")

            address_input = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "(//input[@name='child_street' and contains(@class, 'o_address_street')])[1]")))
            address_input.send_keys(address)
            self.log.info("Address input filled")

            city_input = WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, "//div[@name='destination_city']//input[contains(@class, 'o_input')]")))
            city_input.send_keys(city)
            dropdown_option = WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable((By.XPATH, "//ul[contains(@class, 'ui-autocomplete')]//li/a")))
            dropdown_option.click()

            next_button = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-value='next']")))
            next_button.click()
            self.log.info("Next button clicked")

            CRBT = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "//div[@name='cod']//input[contains(@class, 'o_input')]")))
            CRBT.clear()
            CRBT.send_keys(CRBTV)
            self.log.info("CRBT input filled")

            value = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "//div[@name='colis_value']//input[contains(@class, 'o_input')]")))
            value.click()
            value.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
            value.send_keys(valuev)
            self.log.info("Value input filled")

            save_button = WebDriverWait(main_info, wait).until(EC.element_to_be_clickable((By.XPATH, "//button[@special='save']")))
            save_button.click()
            self.log.info("Save button clicked")            
            try:
                error_modal = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'o_dialog_warning')))
                error_message = error_modal.find_element(By.TAG_NAME, 'p').text
                self.log.error("Validation error occurred: %s", error_message)
                return False, error_message
                
            except TimeoutException:
                self.log.info("No error appeared after clicking save button")
                
                try:
                    notification = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'o_notification_manager')))
                    notification_text = notification.text
                    self.log.info("Parcel creation failed due to %s", notification_text)
                    return False, notification_text
                
                except TimeoutException:
                    self.log.info("Parcel created successfully")
                    self.driver.refresh()
                    return True, ""

        except Exception as e:
            self.log.error("Error creating parcel: %s", str(e))
            return False, str(e)

    def create_parcels_in_mass(self, wait):
        action = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[3]/button/span")))
        action.click()
        self.log.info("1")
        import_parcels_file = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[3]/ul/li[6]/button"))) 
        import_parcels_file.click()
        self.log.info("2")
        file_input= WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div/button[4]")))
        file_path = "C:\\Users\\Public\\Testing_cases\\cpcolisminimal(DATA FOR TESTING).xlsx"
        file_input.send_keys(file_path)
        time.sleep(wait)

    def save_to_csv(self, test_time, name, phone, address, city, CRBTV, valuev, status, error_message, output_file_path):
        try:
            logging.info(f'Writing to csv file: {output_file_path} started')
            data_file = open(output_file_path, mode='a', newline='', encoding='utf-8')
            writer = csv.writer(data_file)
            writer.writerow([test_time, name, phone, address, city, CRBTV, valuev, status, error_message])
        except Exception as e:
            logging.error(f'Error writing to csv file: {str(e)}')

    def parcel_confirmation(self, wait):
        try: 
            main_element = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'o_action_manager')))            
            parcels_list = WebDriverWait(main_element, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ui-sortable')))
            parcel_to_confirm = WebDriverWait(parcels_list, wait).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-id="cp.coli_2"]')))
            parcel_to_confirm.click()
            confirm = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.NAME, 'action_confirm_coli')))
            confirm.click()
            self.log.info("Parcel confirmed")
            return True
        except Exception as e:
            self.log.error("Error confirming parcel: %s", str(e))
            return False

    def parcel_cancellation(self, wait):
        try: 
            main_element = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'o_action_manager')))            
            parcels_list = WebDriverWait(main_element, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ui-sortable')))
            parcel_to_cancel = WebDriverWait(parcels_list, wait).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-id="cp.coli_7"]')))
            parcel_to_cancel.click()
            cancel = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.NAME, 'action_cancel_colis')))
            cancel.click()
            self.log.info("Parcel cancelled")
            return True
        except Exception as e:
            self.log.error("Error canceling parcel: %s", str(e))
            return False

    def parcel_mass_confirmation(self, wait):
        try: 
            select_all = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/table/thead/tr/th[1]")))
            
            select_all.click()
            action = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/button/span")))
            action.click()
            action_dropdown_option_confirm = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[4]/a")
            action_dropdown_option_confirm.click()
            
            ok = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/footer/button/span")))
            ok.click()
            return True
        except Exception as e:
            self.log.error("Error confirming parcels: %s", str(e))
            return False

    def parcel_mass_print(self, wait):
        try: 
            select_all = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/table/thead/tr/th[1]")))
            
            select_all.click()
            print = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]/button/span")))
            print.click()
            # print_dropdown_option_100x70 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]/ul/li[1]/a")
            # print_dropdown_option_100x70.click()
            print_dropdown_option_A4 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[1]/ul/li[2]/a")
            print_dropdown_option_A4.click()
            time.sleep(int(wait))
            self.log.info("printed all parcels tickets")
            return True
        except Exception as e:
            self.log.error("Error printing parcels: %s", str(e))
            return False

    def update_parcel_details(self, wait):
        try: 
            select = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]")))
            select.click()
            action = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/button/span")))
            action.click()
            action_dropdown_edit_address = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[3]/a")
            action_dropdown_edit_address.click()
            
            main_info = WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
            self.log.info("Updating parcel details")
            full_name = WebDriverWait(main_info, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/main/div/div/div/div/table/tbody/tr[1]/td[2]/input")))
            full_name.send_keys("ABDOU")
            phone_number = WebDriverWait(main_info, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/main/div/div/div/div/table/tbody/tr[2]/td[2]/input")))
            phone_number.send_keys("ABDOU")
            new_address = WebDriverWait(main_info, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/main/div/div/div/div/table/tbody/tr[3]/td[2]/input")))
            new_address.send_keys("ABDOU")
            update = WebDriverWait(main_info, wait).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/footer/div/footer/button[1]/span")))
            update.click()
            try:
                error_modal = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'o_dialog_warning')))
                error_message = error_modal.find_element(By.TAG_NAME, 'p').text
                self.log.error("Validation error occurred: %s", error_message)
                return False, error_message
            except TimeoutException:
                self.log.info("No error appeared after updating parcel details")
                return True
        except Exception as e:
            self.log.error("Error printing parcels: %s", str(e))
            return False
