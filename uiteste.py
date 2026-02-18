from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/Bookstore/index2.html")

    driver.find_element(By.NAME, 'username').send_keys("testuser")
    driver.find_element(By.NAME, 'password').send_keys("testpass")
    driver.find_element(By.ID, "login-button").click()

    # Wait up to 10 seconds for welcome-message to appear
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.presence_of_element_located((By.ID, "welcome-message")))

    assert message is not None
    driver.quit()
