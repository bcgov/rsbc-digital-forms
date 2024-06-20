import React from "react";
import { useField } from "formik";
import Select from "react-select";

export const SearchableSelect = ({
  onChange,
  label,
  required,
  options,
  ...props
}) => {
  const [field, meta, helpers] = useField(props.name);

  const { disabled } = props;

  const handleChange = (selectedOption) => {
    helpers.setValue(selectedOption);
    if (onChange) {
      onChange(selectedOption);
    }
  };

  const value = field.value
    ? options.find((option) => option.value === field.value.value) ||
      field.value
    : null;

  return (
    <div>
      <label htmlFor={field.name}>
        {label}
        {required && <span className="required-asterisk">*</span>}
      </label>
      <Select
        {...field}
        {...props}
        value={value}
        inputId={`${field.name}-select`}
        onChange={handleChange}
        options={options}
        isDisabled={disabled}
        isSearchable
        styles={{
          option: (baseStyles) => ({
            ...baseStyles,
            minHeight: 40,
          }),
        }}
      />
      <input
        name={field.name}
        id={field.name}
        type="hidden"
        value={field.value ? JSON.stringify(field.value) : ""} // Assuming field.value is an object with a value property
      />
      {meta.touched && meta.error ? (
        <div className="error-message">{meta.error}</div>
      ) : null}
    </div>
  );
};
