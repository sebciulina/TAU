from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

@given('Otwieram przeglądarkę')
def step_given_otwieram_przegladarke(context):
    pass

@when('Wchodzę na stronę "{url}"')
def step_when_wchodze_na_strone(context, url):
    driver.get(url)

@then('Powinienem zobaczyć pole "{element_id}"')
def step_then_powinienem_zobaczyc_pole(context, element_id):
    element = driver.find_element(By.ID, element_id)
    assert element.is_displayed()

@when('Klikam przycisk "{button_text}" bez podania nazwy użytkownika i hasła')
def step_when_klikam_przycisk_bez_podania_danych(context, button_text):
    element = driver.find_element(By.ID, "submit")
    element.click()
    time.sleep(1)

@then('Powinienem zobaczyć komunikat o nieprawidłowej nazwie użytkownika')
def step_then_powinienem_zobaczyc_komunikat_o_nieprawidlowej_nazwie_uzytkownika(context):
    error_message = driver.find_element(By.ID, "error").text
    assert "Your username is invalid!" in error_message

@when('Wpisuję poprawną nazwę użytkownika i hasło')
def step_when_wpisuje_poprawna_nazwe_uzytkownika_i_haslo(context):
    username = "student"
    password = "Password123"
    element = driver.find_element(By.ID, "username")
    element.send_keys(username)
    element = driver.find_element(By.ID, "password")
    element.send_keys(password)

@then('Powinienem zostać przekierowany na stronę "{expected_url}"')
def step_then_powinienem_zostac_przekierowany(context, expected_url):
    assert driver.current_url == expected_url

@then('Powinienem móc wrócić na poprzednią stronę')
def step_then_powinienem_moc_wrocic_na_poprzednia_strone(context):
    driver.back()
    time.sleep(1)

@when('Wpisuję nieprawidłową nazwę użytkownika i poprawne hasło')
def step_when_wpisuje_nieprawidlowa_nazwe_uzytkownika_i_poprawne_haslo(context):
    username = "invalid_user"
    password = "Password123"
    element = driver.find_element(By.ID, "username")
    element.send_keys(username)
    element = driver.find_element(By.ID, "password")
    element.send_keys(password)

@then('Powinienem zobaczyć komunikat o nieprawidłowej nazwie użytkownika')
def step_then_powinienem_zobaczyc_komunikat_o_nieprawidlowej_nazwie_uzytkownika(context):
    error_message = driver.find_element(By.ID, "error").text
    assert error_message == "Your username is invalid!"

@when('Wpisuję poprawną nazwę użytkownika i nieprawidłowe hasło')
def step_when_wpisuje_poprawna_nazwe_uzytkownika_i_nieprawidlowe_haslo(context):
    username = "student"
    password = "invalid_password"
    element = driver.find_element(By.ID, "username")
    element.send_keys(username)
    element = driver.find_element(By.ID, "password")
    element.send_keys(password)

@then('Powinienem zobaczyć komunikat o nieprawidłowym haśle')
def step_then_powinienem_zobaczyc_komunikat_o_nieprawidlowym_hasle(context):
    error_message = driver.find_element(By.ID, "error").text
    assert error_message == "Your password is invalid!"

@when('Wpisuję poprawną nazwę użytkownika i hasło')
def step_when_wpisuje_poprawna_nazwe_uzytkownika_i_haslo(context):
    username = "student"
    password = "Password123"
    element = driver.find_element(By.ID, "username")
    element.send_keys(username)
    element = driver.find_element(By.ID, "password")
    element.send_keys(password)

@when('Klikam przycisk "Submit"')
def step_when_klikam_przycisk_submit(context):
    element = driver.find_element(By.ID, "submit")
    element.click()
    time.sleep(1)

@when('Wpisuję poprawną nazwę użytkownika i hasło')
def step_when_wpisuje_poprawna_nazwe_uzytkownika_i_haslo(context):
    username = "student"
    password = "Password123"
    element = driver.find_element(By.ID, "username")
    element.send_keys(username)
    element = driver.find_element(By.ID, "password")
    element.send_keys(password)

@when('Klikam przycisk "Submit"')
def step_when_klikam_przycisk_submit(context):
    element = driver.find_element(By.ID, "submit")
    element.click()
    time.sleep(1)

@when('Wpisuję niepoprawną nazwę użytkownika i niepoprawne hasło')
def step_when_wpisuje_niepoprawna_nazwe_uzytkownika_i_niepoprawne_haslo(context):
    username = "invalid_user"
    password = "invalid_password"
    element = driver.find_element(By.ID, "username")
    element.send_keys(username)
    element = driver.find_element(By.ID, "password")
    element.send_keys(password)

@then('Powinienem zobaczyć komunikat o nieprawidłowej nazwie użytkownika')
def step_then_powinienem_zobaczyc_komunikat_o_nieprawidlowej_nazwie_uzytkownika(context):
    error_message = driver.find_element(By.ID, "error").text
    assert error_message == "Your username is invalid!"

@when('Wpisuję login zawierający tylko białe znaki')
def step_when_wpisuje_login_zawierajacy_tylko_biale_znaki(context):
    username = "   "
    password = "Password123"
    element = driver.find_element(By.ID, "username")
    element.send_keys(username)
    element = driver.find_element(By.ID, "password")
    element.send_keys(password)

@when('Wpisuję hasło zawierające tylko białe znaki')
def step_when_wpisuje_haslo_zawierajace_tylko_biale_znaki(context):
    username = "student"
    password = "   "
    element = driver.find_element(By.ID, "username")
    element.send_keys(username)
    element = driver.find_element(By.ID, "password")
    element.send_keys(password)

@then('Powinienem zobaczyć komunikat o nieprawidłowej nazwie użytkownika')
def step_then_powinienem_zobaczyc_komunikat_o_nieprawidlowej_nazwie_uzytkownika(context):
    error_message = driver.find_element(By.ID, "error").text
    assert error_message == "Your username is invalid!"

driver.close()
