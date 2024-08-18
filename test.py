from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


# Configure ChromeDriver
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_service = Service('/usr/local/bin/chromedriver')


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    driver.quit()


def test_valid_sign_up(driver):
    driver.get('https://app-moccona.letsweel.com/app/business-signup')
    driver.find_element('name', 'email').send_keys('test1436@company.com')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]').click()
    driver.find_element('id', 'password').send_keys('ValidPassword@123')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="registration-terms"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-testid="email-sign-up"]').click()
    time.sleep(5)  # Wait for navigation
    assert driver.current_url == 'https://app-moccona.letsweel.com/app/personal-info'



def test_already_sign_up(driver):
    driver.get('https://app-moccona.letsweel.com/app/business-signup')
    driver.find_element('name', 'email').send_keys('test3@company.com')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]').click()
    driver.find_element('id', 'password').send_keys('ValidPassword@123')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="registration-terms"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-testid="email-sign-up"]').click()
    time.sleep(4)  # Wait for navigation
    already_error = driver.find_element(By.CSS_SELECTOR, '[data-testid="login-to-continue-link"]').text
    assert already_error == 'Login to continue'

def test_error_message_for_unpopulated_fields_signup(driver):
    driver.get('https://app-moccona.letsweel.com/app/business-signup')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]').click()
    time.sleep(2)
    email_error = driver.find_element(By.CSS_SELECTOR, '[data-testid="form-input-wrapper-error-text"]').text
    assert email_error == 'Please enter an email address.'


def test_error_message_for_unpopulated_fields_signin(driver):
    driver.get('https://app-moccona.letsweel.com/app/business-signup')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="login-link"]').click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]').click()
    time.sleep(2)
    email_error = driver.find_element(By.CSS_SELECTOR, '[data-testid="form-input-wrapper-error-text"]').text
    assert email_error == 'Please enter your email address'


def test_valid_work_email(driver):
    driver.get('https://app-moccona.letsweel.com/app/business-signup')
    driver.find_element('name', 'email').send_keys('test@gmail.com')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]').click()
    driver.find_element('id', 'password').send_keys('ValidPassword@123')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="registration-terms"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-testid="email-sign-up"]').click()
    time.sleep(2)  # Wait for navigation
    email_error = driver.find_element(By.CSS_SELECTOR, '[data-testid="form-input-wrapper-error-text"]').text
    assert email_error == 'Please try again with your work email address'


def test_invalid_password(driver):
    driver.get('https://app-moccona.letsweel.com/app/business-signup')
    driver.find_element('name', 'email').send_keys('test@company.com')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]').click()
    driver.find_element('id', 'password').send_keys('ValidPassword123')
    driver.find_element(By.CSS_SELECTOR, '[data-testid="registration-terms"]').click()
    button = driver.find_element(By.CSS_SELECTOR, '[data-testid="email-sign-up"]')
    assert button.is_enabled() == False

if __name__ == '__main__':
    pytest.main()