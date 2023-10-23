import React, { useRef, useEffect } from "react";
import { useField } from "formik";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { CalendarToday } from "@mui/icons-material";

export const DatePickerField = ({ required, label, ...props }) => {
  const [field, meta, helpers] = useField(props.name);
  const datepickerRef = useRef(null);

  const handleDateChange = (date) => {
    helpers.setValue(date);
  };

  const openDatePicker = () => {
    datepickerRef.current.setOpen(true);
  };

  useEffect(() => {
    if (meta.value) {
      helpers.setTouched(true);
    }
  }, [meta.value, helpers]);

  return (
    <div>
      <label htmlFor={props.name}>
        {label}
        {required && <span className="required-asterisk"> *</span>}
      </label>
      <div className="d-flex align-items-center">
        <DatePicker
          {...field}
          {...props}
          id={props.name}
          selected={field.value}
          onChange={handleDateChange}
          dateFormat="yyyyMMdd"
          todayButton="Today"
          showMonthDropdown
          showYearDropdown
          placeholderText="YYYYMMDD"
          minDate={new Date(1900, 0, 1)}
          className={`form-control ${
            meta.touched && meta.error && "is-invalid"
          }`}
          ref={datepickerRef}
        />
        <div onClick={openDatePicker}>
          <CalendarToday />
        </div>
      </div>
      {meta.touched && meta.error ? (
        <div className="error-message">{meta.error}</div>
      ) : null}
    </div>
  );
};
