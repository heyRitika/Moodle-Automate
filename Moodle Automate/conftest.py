from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import pytest

@pytest.fixture(scope='class')
def activatebrowser(request):
        services_obj=Service(r"C:\\Users\\lenovo\\Downloads\\chromedriver-win64\\chromedriver.exe")
        driver=webdriver.Chrome(service=services_obj)
        driver.maximize_window()
        #request.cls points to the test class where the fixture is being used.
        request.cls.driver=driver
        yield
        driver.quit()

        