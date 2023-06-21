describe('Test 2 - Poprawne dane logowania', () => {
    it('Loguje się pomyślnie', () => {
      cy.visit('https://practicetestautomation.com/practice-test-login/')
      cy.get('#username').type('student')
      cy.get('#password').type('Password123')
      cy.get('#submit').click()
      cy.url().should('eq', 'https://practicetestautomation.com/logged-in-successfully/')
    })
  })
  