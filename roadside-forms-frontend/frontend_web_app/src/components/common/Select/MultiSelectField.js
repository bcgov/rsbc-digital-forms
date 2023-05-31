import React, { useState } from 'react';
import { useField } from 'formik';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Select from 'react-select';
import { MultiSelectWidget } from '../Widget/MultiSelectWidget'; 

export const MultiSelectField = ({ label, name, options }) => {
  const [field, , helpers] = useField(name);
  const [showModal, setShowModal] = useState(false);

  const handleToggleModal = () => {
    setShowModal(!showModal);
  };

  const handleSelect = (selectedOptions) => {
    const selectedValues = selectedOptions.map((option) => option.value);
    helpers.setValue(selectedValues);
    setShowModal(false);
  };

  return (
    <>
      <label>{label}</label>{' '}<Button variant="primary" className="slim-button" onClick={handleToggleModal}>
            Edit
          </Button>
      <Select
        isMulti
        options={options}
        id={name}
        value={options.filter((option) => field.value.includes(option.value))}
        onChange={(selectedOptions) => {
          const selectedValues = selectedOptions.map((option) => option.value);
          helpers.setValue(selectedValues);
        }}
        onBlur={helpers.setTouched}
        onMouseDown={handleToggleModal}
      />
      <Modal show={showModal} onHide={handleToggleModal}>
        <Modal.Header closeButton>
          <Modal.Title>Select Options</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <MultiSelectWidget name={name} options={options} onSelect={handleSelect} />
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleToggleModal}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};
