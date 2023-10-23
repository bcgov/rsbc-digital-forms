import React from "react";
import { useField } from "formik";

export const NumericInput = ({ required, label, name, ...props }) => {
  const [field, meta] = useField(name);

  const handleChange = (e) => {
    const { value } = e.target;

    // Limit the input value to 999
    const sanitizedValue = value.replace(/[^0-9]/g, "").slice(0, 3);

    // Update the field value
    field.onChange({ target: { name, value: sanitizedValue } });
  };

  return (
    <div>
      <label htmlFor={name}>
        {label}
        {required && <span className="required-asterisk"> *</span>}
      </label>
      <input
        type="text"
        id={name}
        {...field}
        {...props}
        onChange={handleChange}
        required={required}
        className={`form-control ${meta.touched && meta.error && "is-invalid"}`}
      />
      {meta.touched && meta.error && (
        <div className="invalid-feedback">{meta.error}</div>
      )}
    </div>
  );
};
