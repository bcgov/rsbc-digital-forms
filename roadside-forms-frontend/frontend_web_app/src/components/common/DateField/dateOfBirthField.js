import React from 'react';
import { useField } from 'formik';

export const DateOfBirthField = ({ label, required, ...props }) => {
  const [field, meta] = useField(props);

  const handleChange = (event) => {
    const { value } = event.target;
    const formattedValue = value.replace(/[^0-9]/g, '');

    if (formattedValue.length <= 8) {
      field.onChange(event);
    }
  };

  const calculateAge = (dateOfBirth) => {
    if (!dateOfBirth) return '';
  
    const year = Number(dateOfBirth.substring(0, 4));
    const month = Number(dateOfBirth.substring(4, 6));
    const day = Number(dateOfBirth.substring(6, 8));
  
    const today = new Date();
    const birthDate = new Date(year, month - 1, day);
  
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
  
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
  
    return age;
  };

  const formatAge =(value) =>{
    const age = calculateAge(value);
    if (age) {
      return ' (' +age +' yrs)'
    }
    return '( 0 yrs )'
  }

  return (
    <div>
      <label htmlFor={props.id || props.name}>{label +  formatAge(field.value)}{required && <span className="required-asterisk">*</span>}</label>
      <input
        type="text"
        name={field.name}
        id={field.name}
        value={field.value}
        onChange={handleChange}
        onBlur={field.onBlur}
        placeholder="YYYYMMDD"
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
