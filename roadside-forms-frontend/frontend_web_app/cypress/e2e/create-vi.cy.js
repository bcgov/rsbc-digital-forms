// import { cy } from 'cypress';

describe('Create VI event', () => {
  beforeEach(() => {
    cy.visit('/');
  
    cy.login('test', '1234');
  
    cy.intercept('**/api/v1/forms', (req) => {
      req.continue((res) => {
        res.body = {
          'forms': [
            {
              "form_type": "VI",
              "id": "12345679",
              "lease_expiry": "Thu, 15 Aug 2034 12:54:23 GMT",
              "printed_timestamp": null,
              "spoiled_timestamp": null,
              "user_guid": "e865ec95-82bc-4fa7-a1b0-e822219ffa15"
            },
            {
              "form_type": "24Hour",
              "id": "VZ123456",
              "lease_expiry": "Thu, 15 Aug 2024 12:54:23 GMT",
              "printed_timestamp": null,
              "spoiled_timestamp": null,
              "user_guid": "e865ec95-82bc-4fa7-a1b0-e822219ffa15"
            },
            {
              "form_type": "12Hour",
              "id": "JZ123456",
              "lease_expiry": "Thu, 15 Aug 2024 12:54:23 GMT",
              "printed_timestamp": null,
              "spoiled_timestamp": null,
              "user_guid": "e865ec95-82bc-4fa7-a1b0-e822219ffa15",
            }
          ]
        }
      })
    }).as('getForms');
    cy.wait('@getForms', {timeout: 10000});
    cy.get('button').contains('New Event').should('be.enabled').click();
  })

  it('successfully fills the form', () => {
    const now = new Date(2024, 6, 17);
    cy.clock(now).then(clock => {
      clock.setSystemTime(now);
    });
    cy.intercept('**/api/v1/icbc/drivers/01234567').as('getDL');
    cy.intercept('**/api/v1/icbc/vehicles/RH5234').as('getVehicle');
    
    cy.get('#VI').check();
    
    cy.get('#event-container').toMatchSnapshot({
      name: 'empty-form'
    });

    cy.get('#driver_licence_no').type('01234567');
    cy.get('button').contains('ICBC Prefill').first().click();
    cy.wait('@getDL');
    
    cy.get('#vehicle_plate_no').type('RH5234');
    cy.get('.vehicle-info').find('button').contains('ICBC Prefill').last().click();
    cy.wait('@getVehicle');
    cy.get('#vehicle_mk_md-select').type('AUDI-{enter}{enter}');
    cy.get('#vehicle_style-select').type('2dr{enter}{enter}');
    
    cy.get('.registered-owner-info')
      .find('button')
      .contains('Fill from driver')
      .click();
    
      cy.get('#date_of_impound').type('20240716{enter}');
    cy.get('#ILO-options-select').type('A J{enter}{enter}');
    
    cy.get('#intersection_or_address_of_offence').type('900 blk hw1');
    cy.get('#offence_city-select').type('Victoria{enter}{enter}');
    cy.get('#agency_file_no').type('123');
    cy.get('#date_of_driving').type('20240716{enter}');
    cy.get('#time_of_driving').type('0600');
    
    cy.get('#irp_impound-YES').check();
    cy.get('#irp_impound_duration-BACWARN3').check();
    cy.get('#IRP_number').type('4321');
    
    cy.get('#excessive_speed').check();
    cy.get('#prohibited').check();
    cy.get('#suspended').check();
    cy.get('#street_racing').check();
    cy.get('#stunt_driving').check();
    cy.get('#motorcycle_seating').check();
    cy.get('#excessive_speed').check();
    cy.get('#motorcycle_restrictions').should('be.disabled');
    cy.get('#unlicensed').check();

    cy.get('#speed_limit').type('50');
    cy.get('#vehicle_speed').type('160');
    cy.get('#speed_estimation_technique-VISUAL').check();
    cy.get('#speed_confirmation_technique-LASER').check();

    cy.get('#unlicenced_prohibition_number').type('UL8976');
    cy.get('#belief_driver_bc_resident-YES').check();
    cy.get('#out_of_province_dl-NO').check();

    cy.get('#linkage_location_of_keys').check();
    cy.get('#linkage_driver_principal').check();
    cy.get('#linkage_owner_in_vehicle').check();
    cy.get('#linkage_owner_aware_possesion').check();
    cy.get('#linkage_vehicle_transfer_notice').check();
    cy.get('#linkage_other').check();
    cy.get('#linkage_location_of_keys_explanation').type('test')

    cy.get('#incident_details').type('no details');
    
    cy.get('#event-container').toMatchSnapshot({
      name: 'filled-form'
    });

    cy.get('button').contains('Next').click()

    cy.get('#event-container').toMatchSnapshot({
      name: 'form-to-print'
    });
  });
})
