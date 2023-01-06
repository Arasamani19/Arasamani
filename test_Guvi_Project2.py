from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

class Arasu():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Firefox
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_Login_TC_PIM_01(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        self.driver.find_element(By.NAME, "Username").send_keys("Admin")
        self.driver.find_element(By.NAME, "Password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        