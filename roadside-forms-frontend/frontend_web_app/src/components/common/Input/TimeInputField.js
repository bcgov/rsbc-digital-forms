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
      <label>{label}{required && <span className="required-asterisk"> *</span>}
        <span style={{color: "gray"}}>HHMM in Pacific Time</span>
        </label>
      <input
        type="text"
        {...field}
        {...props}
        value={field.value}
        onChange={handleInputChange}
        required={required}
        className={`form-control ${meta.touched && meta.error && 'is-invalid'}`}
      />
      {meta.touched && meta.error && (
        <div className="invalid-feedback">{meta.error}</div>
      )}
    </div>
  );
};
