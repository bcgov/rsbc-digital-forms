import React, { useState } from 'react';
import { useField } from 'formik';

export const MultiSelectField = ({ label, options, ...props }) => {
  const [field, meta, helpers] = useField(props.name);
  const [expanded, setExpanded] = useState(false);

  const handleChange = event => {
    const selectedOptions = Array.from(event.target.selectedOptions, option => option.value);
    helpers.setValue(selectedOptions);
  };

  const toggleExpand = () => {
    setExpanded(!expanded);
  };

  const containerClassName = `multi-select-container ${expanded ? 'expanded' : ''}`;

  return (
    <div className={containerClassName}>
      <label htmlFor={props.name}>{label}</label>
      <select
        id={props.name}
        onChange={handleChange}
        value={field.value}
        onFocus={toggleExpand}
        onBlur={toggleExpand}
        multiple
        {...props}
      >
        {options.map(option => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      {meta.touched && meta.error && <div>{meta.error}</div>}
    </div>
  );
};
