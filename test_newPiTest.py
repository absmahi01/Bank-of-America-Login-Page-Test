from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest
import pytest_html
''''
Test case is step by step instructions for a tester to verify a software or web appliccation

step-01: Open chrome browser
step-02: Navigate to https://bankofamerica.com
step-03: Enter incorrect user name/online id
step-04: Enter incorrect password
step-05: Click on sign in button
step-06: print title
step-07: print current URL
step-08: close the browser


'''

class Test_BOALoginTest:
    @pytest.fixture()
    @pytest.mark.regression
    def test_setup(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://bankofamerica.com")
        self.driver.maximize_window()


        yield

        self.driver.close()
        self.driver.quit()
        print("Test Successful")

    @pytest.mark.regression
    def test_BoALoginFunction(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)

    @pytest.mark.regression
    def test_BoALoginFunction02(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
        print("Current URL: ",self.driver.current_url)

    @pytest.mark.regression
    def test_BoALoginFunction04(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
        print("Current URL: ", self.driver.current_url)

    @pytest.mark.regression
    def test_BoALoginFunction05(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
        print("Current URL: ", self.driver.current_url)


    @pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.smoke
    def test_BoALoginFunction03(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)

    #@pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.smoke
    def test_BoALoginFunction06(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)

    #@pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.smoke
    def test_BoALoginFunction07(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
        print("Current URL: ", self.driver.current_url)

    @pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.regression
    def test_BoALoginFunction08(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
        print("Current URL: ", self.driver.current_url)

    @pytest.mark.regression
    def test_BoALoginFunction09(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
        print("Current URL: ", self.driver.current_url)

    #@pytest.mark.skip(reason="All smoke test under skip")
    @pytest.mark.smoke
    def test_BoALoginFunction10(self, test_setup):
        self.driver.find_element(By.XPATH, "//*[@id='onlineId1']").send_keys("absmahi17500@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "#passcode1").send_keys("mahi valo chele")
        self.driver.find_element(By.ID, "signIn").click()
        time.sleep(10)
        print("Mahi")
        print("The title is: ", self.driver.title)
