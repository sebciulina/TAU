Feature: Testowanie logowania

Scenario: Testuj logowanie bez podania danych
  Given Otwieram przeglądarkę
  When Wchodzę na stronę "https://practicetestautomation.com/practice-test-login/"
  Then Powinienem zobaczyć pole "login"
  When Klikam przycisk "Submit" bez podania nazwy użytkownika i hasła
  Then Powinienem zobaczyć komunikat o nieprawidłowej nazwie użytkownika

Scenario: Testuj logowanie z poprawnymi danymi
  Given Otwieram przeglądarkę
  When Wchodzę na stronę "https://practicetestautomation.com/practice-test-login/"
  Then Powinienem zobaczyć pole "login"
  When Wpisuję poprawną nazwę użytkownika i hasło
  And Klikam przycisk "Submit"
  Then Powinienem zostać przekierowany na stronę "https://practicetestautomation.com/logged-in-successfully/"
  And Powinienem móc wrócić na poprzednią stronę

Scenario: Testuj logowanie z niepoprawną nazwą użytkownika
  Given Otwieram przeglądarkę
  When Wchodzę na stronę "https://practicetestautomation.com/practice-test-login/"
  Then Powinienem zobaczyć pole "login"
  When Wpisuję niepoprawną nazwę użytkownika i poprawne hasło
  And Klikam przycisk "Submit"
  Then Powinienem zobaczyć komunikat o nieprawidłowej nazwie użytkownika

Scenario: Testuj logowanie z nieprawidłowym hasłem
  Given Otwieram przeglądarkę
  When Wchodzę na stronę "https://practicetestautomation.com/practice-test-login/"
  Then Powinienem zobaczyć pole "login"
  When Wpisuję poprawną nazwę użytkownika i nieprawidłowe hasło
  And Klikam przycisk "Submit"
  Then Powinienem zobaczyć komunikat o nieprawidłowym haśle