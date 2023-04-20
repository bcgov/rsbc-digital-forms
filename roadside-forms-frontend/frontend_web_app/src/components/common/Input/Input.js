import { useField } from "formik";

export const Input = ({ label, ...props }) => {
  const [field, meta, helpers] = useField(props);

  const handleInputChange = (event) => {
    const value = event.target.value.toUpperCase();
    helpers.setValue(value);
  };

  return (
    <div>
      <label htmlFor={props.id || props.name}>{label}</label>
      <input {...field} {...props} onChange={handleInputChange} />
      {meta.touched && meta.error ? <div className="error-message">{meta.error}</div> : null}
    </div>
  );
}
