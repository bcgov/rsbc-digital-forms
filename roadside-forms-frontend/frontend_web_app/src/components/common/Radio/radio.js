import React from 'react';
import { useField } from 'formik';

export const Radio = ({ name, options, required, label }) => {
  const [field, meta] = useField(name);

  return (
    <div>
      {label && (
        <label htmlFor={name}>
          {label}{required && (<span className="required-asterisk"> *</span>)}
        </label>
      )}
      {options.map((option) => (
        <div key={option.value}>
          <input
          className="mr-1"
            type="radio"
            {...field}
            id={`${name}-${option.value}`}
            value={option.value}
            checked={field.value === option.value}
            required={required}
          />
          <label style={{ marginLeft: "5px" }} htmlFor={`${name}-${option.value}`}>{option.label}</label>
        </div>
      ))}
      {meta.touched && meta.error && <div className="error-message">{meta.error}</div>}
    </div>
  );
};

