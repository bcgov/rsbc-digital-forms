import React from 'react';
import { useField } from 'formik';
import Select from 'react-select';

export const SearchableSelect = ({ label, required, options, ...props }) => {
  const [field, meta, helpers] = useField(props.name);

  const handleChange = (selectedOption) => {
    helpers.setValue(selectedOption.value);
  };

  const value = options.find((option) => option.value === field.value.value);

  return (
    <div>
      <label htmlFor={props.id || props.name}>{label}{required && <span className="required-asterisk">*</span>}</label>
      <Select
        {...field}
        {...props}
        value={value}
        id={field.name}
        onChange={handleChange}
        options={options}
        isSearchable
      />
      {meta.touched && meta.error ? <div className="error-message">{meta.error}</div> : null}
    </div>
  );
};
