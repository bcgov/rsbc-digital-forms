import React from "react";
import { useField } from "formik";

export const Checkbox = ({ checked, children, ...props }) => {
  const [field, meta] = useField({ ...props, type: "checkbox" });

  return (
    <div>
      <label>
        <input
          className="mr-1"
          type="checkbox"
          id={field.name}
          {...field}
          {...props}
          checked={field.value}
        />
        <span style={{ marginLeft: "5px" }}>{children}</span>
      </label>
      {meta.touched && meta.error ? (
        <div className="error-message">{meta.error}</div>
      ) : null}
    </div>
  );
};
