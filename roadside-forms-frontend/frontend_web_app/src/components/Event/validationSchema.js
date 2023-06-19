import * as Yup from 'yup';

const vehicleNotImpoundedValidation = (selectedValue) => {
  return Yup.string().test('vehicleNotImpounded', 'This field is required', function(value) {
    const { createError, path, options } = this;

    if (selectedValue === 'Yes' && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const vehicleImpoundedValidation = (selectedValue) => {
  return Yup.string().test('vehicleImpounded', 'This field is required', function(value) {
    const { createError, path, options } = this;

    if (selectedValue === 'Yes' && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const typeOfProhibitionAlcoholValidation = (selectedValue) => {
  return Yup.string().test('typeOfProhibitionAlcohol', 'This field is required', function(value) {
    const { createError, path, options } = this;

    if (selectedValue === 'alcohol' && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const typeOfProhibitionDrugsValidation = (selectedValue) => {
  return Yup.string().test('typeOfProhibitionDrugs', 'This field is required', function(value) {
    const { createError, path, options } = this;

    if (selectedValue === 'drugs' && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const releasedToDriverValidation = (selectedValue) => {
  return Yup.string().test('releasedToDriver', 'This field is required', function(value) {
    const { createError, path, options } = this;

    if (selectedValue === 'released' && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const prohibitionValidation = (yesSeleted) => {
  return Yup.string().test('prohibition', 'This field is required', function(value) {
    const { createError, path, options } = this;

    if (yesSeleted && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

export const validationSchema = Yup.object().shape({
  //common form fields validation
  "last-name": Yup.string().required('Last Name is required'),
  "address": Yup.string().required('Address is required'),
  "city": Yup.string().required('City is required'),
  "prov-state": Yup.string().required('Prov / State is required'),
  "officer-lastname": Yup.string().required('Last Name is required'),
  "officer-prime-id": Yup.string().required('PRIME ID is required'),
  "officer-agency": Yup.string().required('Agency is required'),
  "phone": Yup.string().matches(/^\d{3}-\d{3}-\d{4}$/, 'Phone number format ###-###-####'),
  "dob": Yup.string()
  .nullable()
  .test('dob-validation', 'Invalid Date of Birth', function (dob) {
    if (!dob) {
      // Return true if the field is empty
      return true;
    }
    const currentDate = new Date();
    const inputDate = new Date(dob);

    // Check if the input date is valid and within the desired age range
    if (
      isNaN(inputDate) ||
      inputDate > currentDate ||
      inputDate.getFullYear() < 1900 ||
      inputDate.getFullYear() > currentDate.getFullYear() - 10 ||
      inputDate.getFullYear() < currentDate.getFullYear() - 120
    ) {
      return this.createError({ message: 'Driver must be between 10 to 120 years old' });
    }

    return true;
  }),
  "vin-number": Yup.string().max(20, 'VIN must be 20 characters or less'),
  "nsc-number": Yup.string().max(14, 'NSC no. must be 14 characters or less'),
  //24 Hour Fields validation
  'vehicle-impounded': Yup.string().test('vehicleImpoundment', 'Vehicle impoundment is required when 24-hour is selected', function (value) {
    const twentyFourHourValue = this.parent['24Hour'];
    
    if (twentyFourHourValue && !value) {
      return this.createError({
        path: 'vehicle-impounded',
        message: 'Vehicle impoundment is required',
      });
    }

    return true;
  }),
  'key-location': vehicleImpoundedValidation(Yup.ref('vehicle-impounded')),
  'ILO-name': vehicleImpoundedValidation(Yup.ref('vehicle-impounded')),
  'ILO-address': vehicleImpoundedValidation(Yup.ref('vehicle-impounded')),
  'ILO-city': vehicleImpoundedValidation(Yup.ref('vehicle-impounded')),
  'ILO-phone': vehicleImpoundedValidation(Yup.ref('vehicle-impounded')),
  'reason-for-not-impounding': vehicleNotImpoundedValidation(Yup.ref('vehicle-impounded')),
  "type-of-prohibition": prohibitionValidation(Yup.ref('24Hour')),
  "offence-address": prohibitionValidation(Yup.ref('24Hour')),
  "offence-city": prohibitionValidation(Yup.ref('24Hour')),
  "offence-agency-file": prohibitionValidation(Yup.ref('24Hour')),
  'date-of-driving': Yup.date()
  .max(new Date(), 'Date of driving cannot be a future date')
  .nullable()
  .test('prohibition', 'Date of driving is required when 24-hour is selected', function(value) {
    const twentyFourHourValue = this.parent['24Hour'];

    if (twentyFourHourValue && !value) {
      return this.createError({
        path: 'date-of-driving',
        message: 'Date of driving is required',
      });
    }
    if (twentyFourHourValue && value) {
      const today = new Date();
      const oneYearAgo = new Date(today.getFullYear() - 1, today.getMonth(), today.getDate());

      if (value < oneYearAgo) {
        return this.createError({
          path: 'date-of-driving',
          message: 'Date of driving cannot be older than a year',
        });
      }
    }

    return true;
  }),
  "time-of-driving": Yup.string()
     .matches(/^([01]\d|2[0-3])[0-5]\d$/, 'Invalid time format')
  .test('pacific-time', 'Invalid Pacific Time', (value) => {
    if (!value) return true;

    const currentTime = new Date();
    const currentUtcHour = currentTime.getUTCHours();
    const currentUtcMinute = currentTime.getUTCMinutes();

    let currentPacificHour = (currentUtcHour - 7 + 24) % 24; // Convert UTC to Pacific Time (UTC-7)
    const currentPacificMinute = currentUtcMinute;

    const enteredHour = parseInt(value.substr(0, 2));
    const enteredMinute = parseInt(value.substr(2, 2));

    if (enteredHour < currentPacificHour ||
      (enteredHour === currentPacificHour && enteredMinute < currentPacificMinute) ||
      enteredHour > currentPacificHour ||
      enteredMinute < 0 || enteredMinute > 59) {
      return false; // Invalid entered hour or minute
  }

    return true;
  }),
  "vehicle-released-to": releasedToDriverValidation(Yup.ref('reason-for-not-impounding')),
  "date-released": Yup.date()
  .max(new Date(), 'Date of release cannot be a future date')
  .nullable()
  .test('released', 'Date of release is required when release is selected', function(value) {
    const selectedValue = this.parent['reason-for-not-impounding'];

    if (selectedValue === 'released' && !value) {
      return this.createError({
        path: 'date-released',
        message: 'Date of release is required',
      });
    }

    if (selectedValue === 'released' && value) {
      const today = new Date();
      const oneYearAgo = new Date(today.getFullYear() - 1, today.getMonth(), today.getDate());

      if (value < oneYearAgo) {
        return this.createError({
          path: 'date-released',
          message: 'Date of release cannot be older than a year',
        });
      }
    }

    return true;
  }),
  "time-released": releasedToDriverValidation(Yup.ref('reason-for-not-impounding'))
  .matches(/^([01]\d|2[0-3])[0-5]\d$/, 'Invalid time format')
  .test('pacific-time', 'Invalid Pacific Time', (value) => {
    if (!value) return true;

    const currentTime = new Date();
    const currentUtcHour = currentTime.getUTCHours();
    const currentUtcMinute = currentTime.getUTCMinutes();

    let currentPacificHour = (currentUtcHour - 7 + 24) % 24; // Convert UTC to Pacific Time (UTC-7)
    const currentPacificMinute = currentUtcMinute;

    const enteredHour = parseInt(value.substr(0, 2));
    const enteredMinute = parseInt(value.substr(2, 2));

    if (enteredHour < currentPacificHour ||
      (enteredHour === currentPacificHour && enteredMinute < currentPacificMinute) ||
      enteredHour > currentPacificHour ||
      enteredMinute < 0 || enteredMinute > 59) {
    return false; // Invalid entered hour or minute
  }

    return true;
  }),
  "test-used-alcohol": typeOfProhibitionAlcoholValidation(Yup.ref('type-of-prohibition')),
  "BAC-result": typeOfProhibitionAlcoholValidation(Yup.ref('type-of-prohibition')),
  'ASD-expiry-date': Yup.date()
  .nullable()
  .test('ASD', 'ASD expiry date is required when ASD is is selected', function(value) {
    const selectedValue = this.parent['test-used-alcohol'];

    if (selectedValue === 'alco-sensor' && !value) {
      return this.createError({
        path: 'ASD-expiry-date',
        message: 'This field is required',
      });
    }

    return true;
  }),
  'alcohol-test-result': Yup.date()
  .nullable()
  .test('Instrument', 'Test result is required when Instrument is is selected', function(value) {
    const selectedValue = this.parent['test-used-alcohol'];

    if (selectedValue === 'instrument' && !value) {
      return this.createError({
        path: 'instrument',
        message: 'This field is required',
      });
    }

    return true;
  }),
  "test-used-drug": typeOfProhibitionDrugsValidation(Yup.ref('type-of-prohibition')),
});
