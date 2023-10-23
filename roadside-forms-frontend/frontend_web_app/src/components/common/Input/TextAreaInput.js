import { useField } from "formik";

export const TextAreaInput = ({ label, required, onChange, ...props }) => {
  const [field, meta, helpers] = useField(props);

  const handleInputChange = (event) => {
    const value = event.target.value.toUpperCase();
    helpers.setValue(value);

    // Call the onChange method from the parent component if provided
    if (onChange) {
      onChange(event);
    }
  };
  return (
    <div>
      <label htmlFor={props.id || props.name}>
        {label}
        {required && <span className="required-asterisk"> *</span>}
      </label>
      <textarea
        id={field.name}
        {...field}
        {...props}
        onChange={handleInputChange}
      />
      {meta.touched && meta.error ? (
        <div className="error-message">{meta.error}</div>
      ) : null}
    </div>
  );
};
