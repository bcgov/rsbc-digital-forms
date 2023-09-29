import React from 'react';
import { useField } from 'formik';
import { DatePickerField } from './DatePicker';

export const DateOfBirthField = ({ label, required, ...props }) => {
  const [field, meta] = useField(props);
  const calculateAge = (dateOfBirth) => {
    if (!dateOfBirth ) return '';
  
    const date = new Date(dateOfBirth);

    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
  
    if (isNaN(year) || isNaN(month) || isNaN(day)) return '';
  
    const today = new Date();
    const birthDate = new Date(year, month - 1, day);
  
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
  
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
  
    return age;
  };

  const formatAge = (value) => {
    const age = calculateAge(value);
    if (value && age !== '') {
      return ' (' + age + ' yrs)';
    }
    return '( 0 yrs )';
  };


  return (
    <div>
      <DatePickerField
        {...field}
        {...props}
        label={label + formatAge(field.value)}
        className={`form-control ${
          meta.touched && meta.error ? 'is-invalid' : ''
        }`}
      />
      {meta.touched && meta.error ? (
        <div className="invalid-feedback">{meta.error}</div>
      ) : null}
    </div>
  );
};
