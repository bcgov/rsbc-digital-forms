import {atom} from 'recoil'

export const vehicles = atom({
    key:"allVehicles",
    default: [],
  });

export const vehicleStyles = atom({
    key:"allVehicleStyles",
    default: [],
  });

  export const vehicleColours = atom({
    key:"allVehicleColours",
    default: [],
  });

export const provinces = atom({
    key:"allProvinces",
    default: [],
  });

export const permissions = atom({
    key:"allPermissions",
    default: [],
  });

export const jurisdictions = atom({
    key:"allJurisdictions",
    default: [],
  });

export const impoundLotOperators = atom({
    key:"allImpoundLotOperators",
    default: [],
  });

export const countries = atom({
    key:"allCountries",
    default: [],
  });

export const cities = atom({
    key:"allCities",
    default: [],
  });

export const agencies = atom({
    key:"allAgencies",
    default: [],
  });
