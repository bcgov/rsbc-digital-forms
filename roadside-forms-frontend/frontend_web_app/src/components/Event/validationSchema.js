import * as Yup from 'yup';
import moment from 'moment-timezone';


const vehicleImpoundedValidation = (selectedValue) => {
  return Yup.string().test('vehicleImpounded', 'This field is required', function(value) {
    const { createError, path, options } = this;
    const vehicleImpoundedValue = this.resolve(selectedValue);
    if (vehicleImpoundedValue === 'YES' && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const prescribedDeviceValidation = (selectedValue) => {
  return Yup.string().test('prescribedDevice', 'This field is required', function(value) {
    const { createError, path, options } = this;
    const checkValue = this.resolve(selectedValue);
    if (checkValue === 'YES' && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const releasedToDriverValidation = (selectedValue) => {
  return Yup.string().test('releasedToDriver', 'This field is required', function(value) {
    const { createError, path, options } = this;
    const checkValue = this.resolve(selectedValue)

    if (checkValue === 'released' && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const prohibitionValidation = (yesSeleted) => {
  return Yup.mixed().test('prohibition', 'This field is required', function(value) {
    const { createError, path, options } = this;

    if (yesSeleted && !value) {
      return createError({ path, message: options.message });
    }

    return true;
  });
};

const validateRequiredDateWithMax = (selectedValue, errorPath, maxDate) => {
  return function(value) {
    if (selectedValue && !value) {
      return this.createError({
        path: errorPath,
        message: 'Date is required',
      });
    }

    if (selectedValue && value) {
      // Adjust the current date and yesterday's date to Pacific Timezone
      const today = new Date();
      const yesterdayPST = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1);
      const todayPST = new Date(today.getFullYear(), today.getMonth(), today.getDate());

      if (
        (value.getTime() !== yesterdayPST.getTime()) &&
        (value.getTime() !== todayPST.getTime())
      ) {
        return this.createError({
          path: errorPath,
          message: 'Date must be yesterday or today',
        });
      }
    }

    if (value && maxDate && value > maxDate) {
      return this.createError({
        path: errorPath,
        message: `Date cannot be a future date or later than ${maxDate.toDateString()}`,
      });
    }

    return true;
  };
};


export const validationSchema = Yup.object().shape({
  //common form fields validation
  "last-name": Yup.string().required('Last Name is required'),
  "address": Yup.string().required('Address is required'),
  "city": Yup.string().required('City is required'),
  "prov-state": Yup.object().required('Prov / State is required'),
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

    const currentDate = moment();
    const inputDate = moment(dob).utcOffset('+07:00');;
  
    const currentYear = currentDate.year();
    const inputYear = inputDate.year();

    const ageInYears = currentYear - inputYear;

    // Check if the input date is valid and within the desired age range
    if (isNaN(ageInYears) || ageInYears < 10 || ageInYears > 120) {
      return this.createError({ message: 'Driver must be between 10 to 120 years old' });
    }

    const currentMonth = currentDate.month();
    const currentDay = currentDate.date();

    // Get the month and day from the adjusted input date
    const inputMonth = inputDate.month();
    const inputDay = inputDate.date();

    // Check if the user is exactly 10 years old
    if (ageInYears === 10 && (inputMonth > currentMonth || (inputMonth === currentMonth && inputDay > currentDay))) {
      // If the input month is greater than the current month,
      // or if the input month is equal to the current month but the input day is greater,
      // return an error message
        return this.createError({ message: 'Driver must be at least 10 years old' });
    }

    if (ageInYears >= 120 && (inputMonth < currentMonth || (inputMonth === currentMonth && inputDay < currentDay))) {
        return this.createError({ message: 'Driver cannot be older than 120 years' });
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
  "reason-for-not-impounding": Yup.string()
  .test('not-impounded', 'Reason for not Impounding is required', function(value) {
    const vehicleImpoundedValue = this.resolve(Yup.ref('vehicle-impounded'));

    if (vehicleImpoundedValue === 'NO' && !value) {
      return this.createError({
        path: 'reason-for-not-impounding',
        message: 'Reason for not Impounding is required',
      });
    }

    return true;
  }),
  "type-of-prohibition": prohibitionValidation(Yup.ref('24Hour')),
  "offence-address": prohibitionValidation(Yup.ref('24Hour')),
  "offence-city": prohibitionValidation(Yup.ref('24Hour')),
  "offence-agency-file": prohibitionValidation(Yup.ref('24Hour')),
  'date-of-driving': Yup.date()
  .max(new Date(), 'Date of driving cannot be a future date')
  .nullable()
  .test('prohibition', 'Date of driving is required when 24-hour is selected', validateRequiredDateWithMax(Yup.ref('24Hour'), 'date-of-driving', new Date())),
  "time-of-driving": Yup.string()
  .matches(/^([01]\d|2[0-3])[0-5]\d$/, 'Invalid time format')
  .test('required', 'Time of driving is required when 24-hour is selected', function(value) {
    const twentyFourHourValue = this.parent['24Hour'];

    if (twentyFourHourValue && !value) {
      return this.createError({
        path: 'time-of-driving',
        message: 'Time of driving is required',
      });
    }

    return true;
  }),
  "vehicle-released-to": releasedToDriverValidation(Yup.ref('reason-for-not-impounding')),
  "date-released": Yup.date()
   .max(new Date(), 'Date of release cannot be a future date')
   .nullable()
   .test('released', 'Date of release is required when release is selected', validateRequiredDateWithMax(Yup.ref('reason-for-not-impounding'), 'date-released', new Date())),
  "time-released": releasedToDriverValidation(Yup.ref('reason-for-not-impounding'))
  .matches(/^([01]\d|2[0-3])[0-5]\d$/, 'Invalid time format'),
  "test-used-alcohol": prescribedDeviceValidation(Yup.ref('prescribed-device')),
  "BAC-result": Yup.number()
  .nullable()
  .positive('BAC result must be a positive number')
  .integer('BAC result must be an integer')
  .min(2, 'BAC result must be greater than 1')
  .max(998, 'BAC result must be less than 999')
  .test('BAC-result', 'BAC-result is required when instrument is selected', function (value) {
    const selectedValue = this.parent['test-used-alcohol'];

    if (selectedValue === 'instrument' && !value) {
      return this.createError({
        path: 'BAC-result',
        message: 'This field is required',
      });
    }

    return true;
  }),
  'ASD-expiry-date': Yup.date()
  .nullable()
  .test('ASD', 'ASD expiry date is required when ASD is selected', function (value) {
    const selectedValue = this.parent['test-used-alcohol'];

    if (selectedValue === 'alco-sensor' && !value) {
      return this.createError({
        path: 'ASD-expiry-date',
        message: 'This field is required',
      });
    }

    if (value && value < new Date()) {
      return this.createError({
        path: 'ASD-expiry-date',
        message: 'Expired!',
      });
    }

    return true;
  }),
  'alcohol-test-result': Yup.string()
  .nullable()
  .test('alcohol-test-result', 'Test result is required when alco-sensor is selected', function(value) {
    const selectedValue = this.parent['test-used-alcohol'];

    if (selectedValue === 'alco-sensor' && !value) {
      return this.createError({
        path: 'alcohol-test-result',
        message: 'This field is required',
      });
    }

    return true;
  }),
  "test-used-drug": prescribedDeviceValidation(Yup.ref('prescribed-device')),
});
