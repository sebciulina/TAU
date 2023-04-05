from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class PageElements:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, id):
        return self.driver.find_element(By.ID, id)

    def find_element_by_class_name(self, class_name):
        return self.driver.find_element(By.CLASS_NAME, class_name)

class TestLoginPage(unittest.TestCase):
    def setUpBrowser(self, browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif browser == "Edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Unsupported browser: {}".format(browser))
        return self.driver

    def setUp(self):
        self.driver = self.setUpBrowser("Chrome")
        self.elements = PageElements(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_page_load(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        wait = WebDriverWait(self.driver, 10)

        try:
            element = wait.until(EC.presence_of_element_located((By.ID, "login")))
        except:
            print("Błąd: Strona nie załadowała się w oczekiwanym czasie.")

    def test_login(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        # Test 1 - Brak wprowadzenia nazwy użytkownika i hasła
        element = self.elements.find_element_by_id("submit")
        element.click()
        time.sleep(1)
        error_message = self.elements.find_element_by_id("error").text
        self.assertEqual(error_message, "Your username is invalid!")

        # Test 2 - Poprawne dane logowania
        username = "student"
        password = "Password123"
        element = self.elements.find_element_by_id("username")
        element.send_keys(username)
        element = self.elements.find_element_by_id("password")
        element.send_keys(password)
        self.elements.find_element_by_id("submit").click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "https://practicetestautomation.com/logged-in-successfully/")
        self.driver.back()

        # Test 3 - Niepoprawny login
        username = "invalid_user"
        password = "Password123"
        element = self.elements.find_element_by_id("username")
        element.send_keys(username)
        element = self.elements.find_element_by_id("password")
        element.send_keys(password)
        self.elements.find_element_by_id("submit").click()
        time.sleep(1)
        error_message = self.elements.find_element_by_id("error").text
        self.assertEqual(error_message, "Your username is invalid!")

        # Test 4 - Niepoprawne hasło
        username = "student"
        password = "invalid_password"
        element = self.elements.find_element_by_id("username")
        element.send_keys(username)
        element = self.elements.find_element_by_id("password")
        element.send_keys(password)
        self.elements.find_element_by_id("submit").click()
        time.sleep(1)
        error_message = self.elements.find_element_by_id("error").text
        self.assertEqual(error_message, "Your password is invalid!")

        # Test 5 - Brak loginu
        username = ""
        password = "Password123"
        element = self.elements.find_element_by_id("username")
        element.send_keys(username)
        element = self.elements.find_element_by_id("password")
        element.send_keys(password)
        self.elements.find_element_by_id("submit").click()
        time.sleep(1)
        error_message = self.elements.find_element_by_id("error").text
        self.assertEqual(error_message, "Your username is invalid!")

        # Test 6 - Brak hasła
        username = "student"
        password = ""
        element = self.elements.find_element_by_id("username")
        element.send_keys(username)
        element = self.elements.find_element_by_id("password")
        element.send_keys(password)
        self.elements.find_element_by_id("submit").click()
        time.sleep(1)
        error_message = self.elements.find_element_by_id("error").text
        self.assertEqual(error_message, "Your password is invalid!")

        # Test 7 - Niepoprawny login i hasło
        username = "invalid_user"
        password = "invalid_password"
        element = self.elements.find_element_by_id("username")
        element.send_keys(username)
        element = self.elements.find_element_by_id("password")
        element.send_keys(password)
        self.elements.find_element_by_id("submit").click()
        time.sleep(1)
        error_message = self.elements.find_element_by_id("error").text
        self.assertEqual(error_message, "Your username is invalid!")

        # Test 8 - Login i hasło zawierają tylko białe znaki
        username = "   "
        password = "   "
        element = self.elements.find_element_by_id("username")
        element.send_keys(username)
        element = self.elements.find_element_by_id("password")
        element.send_keys(password)
        self.elements.find_element_by_id("submit").click()
        time.sleep(1)
        error_message = self.elements.find_element_by_id("error").text
        self.assertEqual(error_message, "Your username is invalid!")


    def test_find_text(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

        username = "student"
        password = "Password123"
        element = self.elements.find_element_by_id("username")
        element.send_keys(username)
        element = self.elements.find_element_by_id("password")
        element.send_keys(password)
        self.elements.find_element_by_id("submit").click()
        time.sleep(1)
        post_title = self.elements.find_element_by_class_name("post-title").text
        self.assertEqual(post_title, "Logged In Successfully")


if __name__ == '__main__':
    unittest.main()
