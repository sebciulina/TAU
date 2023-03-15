from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

# Test 1 - Brak wprowadzenia nazwy użytkownika i hasła
element = driver.find_element(By.ID, "submit")
element.click()
time.sleep(1)
error_message = driver.find_element(By.ID, "error").text
assert "Your username is invalid!" in error_message

# Test 2 - Poprawne dane logowania
username = "student"
password = "Password123"
element = driver.find_element(By.ID, "username")
element.send_keys(username)
element = driver.find_element(By.ID, "password")
element.send_keys(password)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"
driver.back()

# Test 3 - Niepoprawny login
username = "invalid_user"
password = "Password123"
element = driver.find_element(By.ID, "username")
element.send_keys(username)
element = driver.find_element(By.ID, "password")
element.send_keys(password)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
error_message = driver.find_element(By.ID, "error").text
assert error_message == "Your username is invalid!"

# Test 4 - Niepoprawne hasło
username = "student"
password = "invalid_password"
element = driver.find_element(By.ID, "username")
element.send_keys(username)
element = driver.find_element(By.ID, "password")
element.send_keys(password)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
error_message = driver.find_element(By.ID, "error").text
assert error_message == "Your password is invalid!"

# Test 5 - Brak loginu
username = ""
password = "Password123"
element = driver.find_element(By.ID, "username")
element.send_keys(username)
element = driver.find_element(By.ID, "password")
element.send_keys(password)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
error_message = driver.find_element(By.ID, "error").text
assert error_message == "Your username is invalid!"

# Test 6 - Brak hasła
username = "student"
password = ""
element = driver.find_element(By.ID, "username")
element.send_keys(username)
element = driver.find_element(By.ID, "password")
element.send_keys(password)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
error_message = driver.find_element(By.ID, "error").text
assert error_message == "Your password is invalid!"

# Test 7 - Niepoprawny login i hasło
username = "invalid_user"
password = "invalid_password"
element = driver.find_element(By.ID, "username")
element.send_keys(username)
element = driver.find_element(By.ID, "password")
element.send_keys(password)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
error_message = driver.find_element(By.ID, "error").text
assert error_message == "Your username is invalid!"

# Test 8 - Login i hasło zawierają tylko białe znaki
username = "   "
password = "   "
element = driver.find_element(By.ID, "username")
element.send_keys(username)
element = driver.find_element(By.ID, "password")
element.send_keys(password)
driver.find_element(By.ID, "submit").click()
time.sleep(1)
error_message = driver.find_element(By.ID, "error").text
assert error_message == "Your username is invalid!"

driver.close()