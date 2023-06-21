describe('Test 3 - Niepoprawny login', () => {
    it('Wyświetla błąd "Your username is invalid!"', () => {
      cy.visit('https://practicetestautomation.com/practice-test-login/')
      cy.get('#username').type('invalid_user')
      cy.get('#password').type('Password123')
      cy.get('#submit').click()
      cy.get('#error').should('contain', 'Your username is invalid!')
    })
  })
  