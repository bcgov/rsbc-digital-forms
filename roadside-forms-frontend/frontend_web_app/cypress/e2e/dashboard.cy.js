describe('Dashboard', () => {
  it('successfully loads', () => {
    cy.visit('/')

    cy.login('test', '1234')

    cy.contains('Events in Progress').should('be.visible')
    cy.contains('Waiting for Transmission to Server').should('be.visible')
    cy.contains('Completed').should('be.visible')
  })
})
