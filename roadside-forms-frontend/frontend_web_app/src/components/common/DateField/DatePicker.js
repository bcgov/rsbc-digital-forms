import React from 'react';
import { useField } from 'formik';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { CalendarToday } from '@mui/icons-material';

export const DatePickerField = ({ required, label, ...props }) => {
  const [field, meta, helpers] = useField(props.name);

  const handleDateChange = (date) => {
    helpers.setValue(date);
  };

  return (
    <div>
      <label htmlFor={props.id || props.name}>{label}{required && <span className="required-asterisk"> * </span>}
        <span style={{color: "gray"}}>YYYYMMDD</span>
        </label>
      <div className="d-flex align-items-center">
        <DatePicker
          {...field}
          {...props}
          selected={field.value}
          id={props.name}
          onChange={handleDateChange}
          dateFormat="yyyyMMdd"
          className={`form-control ${meta.touched && meta.error && 'is-invalid'}`}
        />
        <CalendarToday />
      </div>
      {meta.touched && meta.error ? <div className="error-message">{meta.error}</div> : null}  
    </div>
  );
};
