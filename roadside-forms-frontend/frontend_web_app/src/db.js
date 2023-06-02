import Dexie from 'dexie';

export const db = new Dexie('digitalForms');

db.version(1).stores({
  user: 'user_guid, business_guid, username, agency, badge_number, last_name, first_name, display_name, login',
  userRoles:'[user_guid+role_name], user_guid, role_name, submitted_dt, approved_dt',
  vehicles: 'id, mk, search, md',
  vehicleStyles: 'code, name',
  vehicleColours: 'code, display_name, colour_class',
  provinces: 'id, objectCd, objectDsc',
  jurisdictions: 'id, objectCd, objectDsc',
  impoundLotOperators: 'id, name, lot_address, city, phone',
  countries: 'id, objectCd, objectDsc',
  cities: 'id, objectCd, objectDsc',
  agencies: 'id, vjur, agency_name',
});

db.open().catch(function (e) {
    console.error("Open failed: " + e);
});






 
 

