import { useField } from "formik";

export const TextAreaInput = ({ label, required, ...props }) => {
  const [field, meta, helpers] = useField(props);

  return (
    <div>
      <label htmlFor={props.id || props.name}>
        {label}
        {required && <span className="required-asterisk"> *</span>}
        </label>
      <textarea id={field.name} {...field} {...props} />
      {meta.touched && meta.error ? <div className="error-message">{meta.error}</div> : null}
    </div>
  );
}
