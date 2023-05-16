import * as Yup from 'yup';

export const validationSchema = Yup.object().shape({
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
  .test('dob-validation', 'Invalid Date of Birth', (dob) => {
    if (!dob) return true;

    const dateRegex = /^(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$/;
    if (!dateRegex.test(dob)) return false;

    const year = Number(dob.substring(0, 4));
    const month = Number(dob.substring(4, 6));
    const day = Number(dob.substring(6, 8));

    const currentDate = new Date();
    const inputDate = new Date(year, month - 1, day);

    // Check if the input date is valid and within the desired range
    return (
      inputDate.getFullYear() === year &&
      inputDate.getMonth() === month - 1 &&
      inputDate.getDate() === day &&
      inputDate <= currentDate &&
      year >= 1900
    );
  }),
  "vin-number": Yup.string().max(20, 'VIN must be 20 characters or less'),
  "nsc-number": Yup.string().max(14, 'NSC no. must be 14 characters or less'),
});
