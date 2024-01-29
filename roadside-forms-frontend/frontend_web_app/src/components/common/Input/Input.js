import { useField } from "formik";

export const Input = ({ label, required, onChange, onBlur, ...props }) => {
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
      <input
        id={field.name}
        {...field}
        {...props}
        className="form-control"
        onChange={handleInputChange}
        onBlur={onBlur}
        autoComplete="off"
      />
      {meta.touched && meta.error ? (
        <div className="error-message">{meta.error}</div>
      ) : null}
    </div>
  );
};
