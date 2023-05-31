import React from 'react';
import { useField, Field } from 'formik';
import Table from 'react-bootstrap/Table';

export const MultiSelectWidget = ({ name, options }) => {
  const [field, , helpers] = useField({ name });

  const handleCheckboxChange = (option) => {
    const selectedValues = [...field.value];
    const optionIndex = selectedValues.indexOf(option.value);

    if (optionIndex === -1) {
      selectedValues.push(option.value);
    } else {
      selectedValues.splice(optionIndex, 1);
    }

    helpers.setValue(selectedValues);
  };

  return (
    <>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Code</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {options.map((option) => (
            <tr key={option.value}>
              <td>
                <div>
                  <label htmlFor={option.value}>
                    <Field
                      className="mr-1"
                      type="checkbox"
                      name={name}
                      id={option.value}
                      value={option.value}
                      checked={field.value.includes(option.value)}
                      onChange={() => handleCheckboxChange(option)}
                    />
                    <span style={{ marginLeft: "5px" }}>{option.value}</span>
                  </label>
                </div>
              </td>
              <td>{option.label}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      <div>Selected: {field.value && field.value.length > 0 ? field.value.join(', ') : 'None'}</div>
    </>
  );
};
