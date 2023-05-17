import React from 'react';
import { useField } from 'formik';
import PropTypes from 'prop-types';

export const PhoneField = ({ label, required, ...props }) => {
    const [field, meta] = useField(props);

    const handlePhoneChange = (event) => {
        const phone = event.target.value;
        const formattedPhone = formatPhoneNumber(phone); // Function to format phone number
    
        field.onChange(event.target.name)(formattedPhone);
      };
    
      const formatPhoneNumber = (phone) => {
        // Example: Format as ###-###-####
        const cleaned = phone.replace(/[^0-9]/g, '');
        const match = cleaned.match(/^(\d{0,3})(\d{0,3})(\d{0,4})$/);
        return !match ? '' : [match[1], match[2], match[3]].filter((group) => !!group).join('-');
      };
  
    return (
      <div>
        <label htmlFor={props.id || props.name}>{label}{required && <span className="required-asterisk">*</span>}</label>
        <input
          type="tel"
          {...field} {...props}
          name={field.name}
          value={field.value}
          id={field.name}
          onChange={handlePhoneChange}
          maxLength={12}
          pattern="\d{3}-\d{3}-\d{4}"
          placeholder="###-###-####"
          onBlur={field.onBlur}
        />
        {meta.touched && meta.error ? (
          <div className="error-message">{meta.error}</div>
        ) : null}
      </div>
    );
  };
  
  PhoneField.propTypes = {
    label: PropTypes.string.isRequired,
  };
  