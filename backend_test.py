import logging
import requests
from bs4 import BeautifulSoup

class WebAutomationLibrary:
    def __init__(self, driver=None):
        self.driver = driver
        self.log = logging.getLogger(__name__)
        self.session = requests.Session()

    def login(self, email, password):
        try:
            login_url = "https://dev.mobipreshipement.link/web/login"
            
            login_data = {
                "login": email,
                "password": password
            }

            response = self.session.post(login_url, data=login_data)

            if response.status_code == 200:
                self.log.info("Login successful")
                return True
            else:
                self.log.error("Login failed. Status code: %d", response.status_code)
                self.log.error("Response content: %s", response.content)
                return False
        except Exception as e:
            self.log.error("Error logging in: %s", str(e))
            return False

    def create_parcel(self, name, phone, address, city, CRBTV, valuev, wait):
        self.log.info("Create parcel test started:")
        try:
            if not self.login("shop99@example.com", "#dDf7NPptnTHI60"):
                self.log.error("Failed to login")
                return False

            parcel_data = {
                "name": name,
                "phone": phone,
                "address": address,
                "city": city,
                "CRBTV": CRBTV,
                "valuev": valuev
            }

            endpoint_url = "https://dev.mobipreshipement.link/web/dataset/call_kw/cp.coli/create"

            response = self.session.post(endpoint_url, json=parcel_data)

            if response.status_code == 200:
                response_data = response.json()
                if response_data.get("result"):
                    self.log.info("Parcel created successfully")
                    return True
                else:
                    self.log.error("Failed to create parcel. Error message: %s", response_data.get("error"))
                    return False
            else:
                self.log.error("Failed to create parcel. Status code: %d", response.status_code)
                return False

        except Exception as e:
            self.log.error("Error creating parcel: %s", str(e))
            return False

# Example usage:
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    web_automation = WebAutomationLibrary()

    name = "Saad"
    phone = "+2126010203040506"
    address = "Dar Saad"
    city = "Casablanca"
    CRBTV = 9999991
    valuev = 99
    wait = 7

    web_automation.create_parcel(name, phone, address, city, CRBTV, valuev, wait)
