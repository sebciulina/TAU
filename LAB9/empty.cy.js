describe('Test 1 - Brak wprowadzenia nazwy użytkownika i hasła', () => {
  it('Wyświetla błąd "Your username is invalid!"', () => {
    cy.visit('https://practicetestautomation.com/practice-test-login/')
    cy.get('#submit').click()
    cy.get('#error').should('contain', 'Your username is invalid!')
  })
})
