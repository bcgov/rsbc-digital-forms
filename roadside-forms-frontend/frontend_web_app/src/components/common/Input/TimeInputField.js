import React from 'react';
import { useField } from 'formik';

export const TimeInputField = ({ required, label, ...props }) => {
  const [field, meta, helpers] = useField(props.name);

  const handleInputChange = (event) => {
    const { value } = event.target;
    const formattedValue = formatTime(value); // Format the input value as HH:MM

    helpers.setValue(formattedValue);
  };

  const formatTime = (value) => {
    // Remove any non-digit characters
    const digitsOnly = value.replace(/\D/g, '');

     // Ensure the value has at most 4 digits
    const formattedValue = digitsOnly.slice(0, 4);


    return formattedValue;
  };

  return (
    <div>
      <label htmlFor={props.name}>{label}{required && <span className="required-asterisk"> *</span>}
        <span style={{color: "gray"}}>Time in 24-hour clock</span>
        </label>
      <input
        type="text"
        {...field}
        {...props}
        id={props.name}
        value={field.value}
        onChange={handleInputChange}
        required={required}
        className={`form-control ${meta.touched && meta.error && 'is-invalid'}`}
      />
      {meta.touched && meta.error ? <div className="error-message">{meta.error}</div> : null}
    </div>
  );
};
