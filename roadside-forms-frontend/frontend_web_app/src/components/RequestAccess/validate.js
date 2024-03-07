export const validate = (values) => {
  const errors = {};

  if (!values.first_name) {
    errors.first_name = "Given Name is required";
  } else if (values.first_name && values.first_name.length < 2) {
    errors.first_name = "Given Name must be at least 2 characters";
  } else if (values.first_name && values.first_name.length > 30) {
    errors.first_name = "Given Name cannot be longer than 30 characters";
  }

  if (!values.last_name) {
    errors.last_name = "Surname is required";
  } else if (values.last_name && values.last_name.length < 2) {
    errors.last_name = "Surname must be at least 2 characters";
  } else if (values.last_name && values.last_name.length > 30) {
    errors.last_name = "Surname cannot be longer than 30 characters";
  }

  if (!values.agency) {
    errors.agency = "Agency Name is required";
  } else if (values.agency && values.agency.length < 5) {
    errors.agency = "Agency Name must be at least 5 characters";
  } else if (values.agency && values.agency.length > 30) {
    errors.agency = "Agency Name cannot be longer than 30 characters";
  }
  if (!values.badge_number) {
    errors.badge_number = "PRIME ID is required";
  } else if (
    values.badge_number &&
    !/^([A-Z]{2}\d{2,4})|(\d{6})$/.test(values.badge_number)
  ) {
    errors.badge_number = "must be 2 letters + 2-4 digits OR 6 digits (HRMIS)";
  }

  return errors;
};
