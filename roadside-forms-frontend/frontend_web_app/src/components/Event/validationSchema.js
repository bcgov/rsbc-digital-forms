import * as Yup from "yup";
import moment from "moment-timezone";

const vehicleImpoundedValidation = (selectedValue) => {
  return Yup.string().test(
    "vehicleImpounded",
    "This field is required",
    function (value) {
      const { createError, path, options } = this;
      const vehicleImpoundedValue = this.resolve(selectedValue);
      if (vehicleImpoundedValue === "YES" && !value) {
        return createError({ path, message: options.message });
      }

      return true;
    }
  );
};

const prescribedDeviceValidation = (selectedValue) => {
  return Yup.string().test(
    "prescribedDevice",
    "This field is required",
    function (value) {
      const { createError, path, options } = this;
      const checkValue = this.resolve(selectedValue);
      if (checkValue === "YES" && !value) {
        return createError({ path, message: options.message });
      }

      return true;
    }
  );
};

const releasedToDriverValidation = (selectedValue) => {
  return Yup.string().test(
    "releasedToDriver",
    "This field is required",
    function (value) {
      const { createError, path, options } = this;
      const checkValue = this.resolve(selectedValue);

      if (checkValue === "released" && !value) {
        return createError({ path, message: options.message });
      }

      return true;
    }
  );
};

const prohibitionValidation = (yesSeleted) => {
  return Yup.mixed().test(
    "prohibition",
    "This field is required",
    function (value) {
      const { createError, path, options } = this;

      if (yesSeleted && !value) {
        return createError({ path, message: options.message });
      }

      return true;
    }
  );
};

const validateRequiredDateWithMax = (selectedValue, errorPath, maxDate) => {
  return function (value) {
    if (selectedValue && !value) {
      return this.createError({
        path: errorPath,
        message: "Date is required",
      });
    }

    if (selectedValue && value) {
      // Adjust the current date and yesterday's date to Pacific Timezone
      const today = new Date();
      const yesterdayPST = new Date(
        today.getFullYear(),
        today.getMonth(),
        today.getDate() - 1
      );
      const todayPST = new Date(
        today.getFullYear(),
        today.getMonth(),
        today.getDate()
      );

      if (
        value.getTime() !== yesterdayPST.getTime() &&
        value.getTime() !== todayPST.getTime()
      ) {
        return this.createError({
          path: errorPath,
          message: "Date must be yesterday or today",
        });
      }
    }

    if (value && maxDate && value > maxDate) {
      return this.createError({
        path: errorPath,
        message: `Date cannot be a future date or later than ${maxDate.toDateString()}`,
      });
    }

    return true;
  };
};

export const validationSchema = Yup.object().shape({
  /** Form Types */
  VI: Yup.boolean(),
  TwelveHour: Yup.boolean(),
  TwentyFourHour: Yup.boolean(),
  IRP: Yup.boolean(),

  /** Driver's Information */
  driver_licence_no: Yup.string(),
  drivers_licence_jurisdiction: Yup.object(), // Only for 24h / VI
  driver_last_name: Yup.string().required("Last Name is required"),
  driver_given_name: Yup.string().required("Given Name is required"),
  driver_dob: Yup.string()
    .nullable()
    .test("dob-validation", "Invalid Date of Birth", function (dob) {
      if (!dob) {
        // Return true if the field is empty
        return true;
      }

      const currentDate = moment();
      const inputDate = moment(dob).utcOffset("+07:00");

      const currentYear = currentDate.year();
      const inputYear = inputDate.year();

      const ageInYears = currentYear - inputYear;

      // Check if the input date is valid and within the desired age range
      if (isNaN(ageInYears) || ageInYears < 10 || ageInYears > 120) {
        return this.createError({
          message: "Driver must be between 10 to 120 years old",
        });
      }

      const currentMonth = currentDate.month();
      const currentDay = currentDate.date();

      // Get the month and day from the adjusted input date
      const inputMonth = inputDate.month();
      const inputDay = inputDate.date();

      // Check if the user is exactly 10 years old
      if (
        ageInYears === 10 &&
        (inputMonth > currentMonth ||
          (inputMonth === currentMonth && inputDay > currentDay))
      ) {
        // If the input month is greater than the current month,
        // or if the input month is equal to the current month but the input day is greater,
        // return an error message
        return this.createError({
          message: "Driver must be at least 10 years old",
        });
      }

      if (
        ageInYears >= 120 &&
        (inputMonth < currentMonth ||
          (inputMonth === currentMonth && inputDay < currentDay))
      ) {
        return this.createError({
          message: "Driver cannot be older than 120 years",
        });
      }

      return true;
    }),
  driver_address: Yup.string(),
  driver_phone: Yup.string().matches(
    /^\d{3}-\d{3}-\d{4}$/,
    "Phone Number format ###-###-####"
  ),
  driver_city: Yup.string(),
  driver_prov_state: Yup.object(),
  driver_postal: Yup.string(),
  gender: Yup.string(),
  driver_licence_expiry: Yup.date(), // Cannot be less than 1980
  driver_licence_class: Yup.string(), // Up to three digits, separated by commas

  /** Vehicle Information */
  vehicle_jurisdiction: Yup.object(), // Select one
  vehicle_plate_no: Yup.string(),
  vehicle_registration_no: Yup.string(), // Max 20 characters, only for 24h / VI
  vehicle_year: Yup.string().required("Vehicle Year is required"), // Select one
  vehicle_mk_md: Yup.string().required("Make / Model is required"), // Select one
  vehicle_style: Yup.string().required("Style is required"), // Select one
  vehicle_color: Yup.string().required("Color is required"), // Select up 1-2
  vehicle_vin_no: Yup.string()
    .required("VIN is required")
    .max(20, "VIN must be 20 characters or less"), // Validation from pilot app, 13-18 characters, only for 24h / VI
  nsc_prov_state: Yup.object(),
  nsc_no: Yup.string().max(14, "NSC no. must be 14 characters or less"),

  /** Registered Owner */
  owned_by_corp: Yup.boolean(), // Only for 24h / VI
  driver_is_regist_owner: Yup.boolean(), // Only for VI
  regist_owner_last_name: Yup.string(), // Only for 24h / VI
  regist_owner_first_name: Yup.string(), // Only for 24h / VI
  regist_owner_dob: Yup.string()
    .nullable()
    .test("dob-validation", "Invalid Date of Birth", function (dob) {
      if (!dob) {
        // Return true if the field is empty
        return true;
      }

      const currentDate = moment();
      const inputDate = moment(dob).utcOffset("+07:00");

      const currentYear = currentDate.year();
      const inputYear = inputDate.year();

      const ageInYears = currentYear - inputYear;

      // Check if the input date is valid and within the desired age range
      if (isNaN(ageInYears) || ageInYears < 10 || ageInYears > 120) {
        return this.createError({
          message: "Driver must be between 10 to 120 years old",
        });
      }

      const currentMonth = currentDate.month();
      const currentDay = currentDate.date();

      // Get the month and day from the adjusted input date
      const inputMonth = inputDate.month();
      const inputDay = inputDate.date();

      // Check if the user is exactly 10 years old
      if (
        ageInYears === 10 &&
        (inputMonth > currentMonth ||
          (inputMonth === currentMonth && inputDay > currentDay))
      ) {
        // If the input month is greater than the current month,
        // or if the input month is equal to the current month but the input day is greater,
        // return an error message
        return this.createError({
          message: "Driver must be at least 10 years old",
        });
      }

      if (
        ageInYears >= 120 &&
        (inputMonth < currentMonth ||
          (inputMonth === currentMonth && inputDay < currentDay))
      ) {
        return this.createError({
          message: "Driver cannot be older than 120 years",
        });
      }

      return true;
    }), // Only for 24h / VI
  corporation_name: Yup.string(), // Only for 24h / VI
  regist_owner_address: Yup.string(), // Only for 24h / VI
  regist_owner_phone: Yup.string().matches(
    /^\d{3}-\d{3}-\d{4}$/,
    "Phone Number format ###-###-####"
  ), // Only for 24h / VI
  regist_owner_email: Yup.string().email(), // Only for 24h / VI
  regist_owner_city: Yup.string(), // Only for 24h / VI
  regist_owner_prov_state: Yup.object(), // Only for 24h / VI
  regist_owner_postal: Yup.string(), // Only for 24h / VI

  /** Vehicle Impoundment or Disposition (24h/VI Only) */
  date_of_impound: Yup.date().required(), // Only for VI, required if VI is selected
  vehicle_impounded: Yup.string().test(
    "vehicleImpoundment",
    "Vehicle impoundment is required when 24-hour is selected",
    function (value) {
      const twentyFourHourValue = this.parent["TwentyFourHour"];

      if (twentyFourHourValue && !value) {
        return this.createError({
          path: "vehicle_impounded",
          message: "Vehicle impoundment is required",
        });
      }

      return true;
    }
  ), // Only for 24h / VI
  reason_for_not_impounding: Yup.string().test(
    "not_impounded",
    "Reason for not Impounding is required",
    function (value) {
      const vehicleImpoundedValue = this.resolve(Yup.ref("vehicle_impounded"));
      if (vehicleImpoundedValue === "NO" && !value) {
        return this.createError({
          path: "reason_for_not_impounding",
          message: "Reason for not Impounding is required",
        });
      }

      return true;
    }
  ), // Only for 24h / VI, required if vehicle_impounded = "No"
  vehicle_released_to: releasedToDriverValidation(
    Yup.ref("reason-for-not-impounding")
  ), // Only for 24h / VI, required if vehicle_impounded = "No" and reason_for_not_impounding = "released"
  date_released: Yup.date()
    .max(new Date(), "Date of release cannot be a future date")
    .nullable()
    .when("TwentyFourHour", {
      is: true,
      then: () =>
        Yup.date().test(
          "released",
          "Date of release is required when release is selected",
          validateRequiredDateWithMax(
            Yup.ref("reason-for-not-impounding"),
            "date_released",
            new Date()
          )
        ),
    }), // Only for 24h / VI, required if vehicle_impounded = "No" and reason_for_not_impounding = "released"
  time_released: releasedToDriverValidation(
    Yup.ref("reason_for_not_impounding")
  ).matches(/^([01]\d|2[0-3])[0-5]\d$/, "Invalid time format"), // Only for 24h / VI, required if vehicle_impounded = "No" and reason_for_not_impounding = "released"
  location_of_keys: Yup.string().when("TwentyFourHour", {
    is: true,
    then: () => vehicleImpoundedValidation(Yup.ref("vehicle_impounded")),
  }), // Only for 24h / VI, required if vehicle_impounded = "No"
  "ILO-name": vehicleImpoundedValidation(Yup.ref("vehicle_impounded")), // Only for 24h / VI, required if vehicle_impounded = "Yes"
  "ILO-address": vehicleImpoundedValidation(Yup.ref("vehicle_impounded")), // Only for 24h / VI, required if vehicle_impounded = "Yes"
  "ILO-city": vehicleImpoundedValidation(Yup.ref("vehicle_impounded")), // Only for 24h / VI, required if vehicle_impounded = "Yes"
  "ILO-phone": vehicleImpoundedValidation(Yup.ref("vehicle_impounded")), // Only for 24h / VI, required if vehicle_impounded = "Yes"

  /** Prohibition */
  type_of_prohibition: Yup.mixed().when("TwentyFourHour", {
    is: true,
    then: () => prohibitionValidation(Yup.ref("TwentyFourHour")),
  }), // Required
  intersection_or_address_of_offence: prohibitionValidation(
    Yup.ref("TwentyFourHour")
  ), // Required, max 30 characters
  offence_city: prohibitionValidation(Yup.ref("TwentyFourHour")), // Required, dropdown, pick one, BC municipalities only
  agency_file_no: prohibitionValidation(Yup.ref("TwentyFourHour")),
  date_of_driving: Yup.date()
    .max(new Date(), "Date of driving cannot be a future date")
    .nullable()
    .test(
      "prohibition",
      "Date of driving is required when 24-hour is selected",
      validateRequiredDateWithMax(
        Yup.ref("TwentyFourHour"),
        "date_of_driving",
        new Date()
      )
    ), // Required, must be today or yesterday
  time_of_driving: Yup.string()
    .matches(/^([01]\d|2[0-3])[0-5]\d$/, "Invalid time format")
    .test(
      "required",
      "Time of driving is required when 24-hour is selected",
      function (value) {
        const twentyFourHourValue = this.parent["TwentyFourHour"];

        if (twentyFourHourValue && !value) {
          return this.createError({
            path: "time_of_driving",
            message: "Time of driving is required",
          });
        }

        return true;
      }
    ), // Required, cannot be in the future
  /** Impoundment for Immediate Roadside Prohibition */
  irp_impound: Yup.string(), // Only for VI, required, should auto-select "Yes" when irp_impound_duration is not blank
  irp_impound_duration: Yup.string(), // Only for VI
  IRP_number: Yup.string(), // Only for VI, required
  VI_number: Yup.string(), // Only for VI, required

  /** Impoundment for Driving Behaviour */
  excessive_speed: Yup.boolean(), // Only for VI
  prohibited: Yup.boolean(), // Only for VI
  suspended: Yup.boolean(), // Only for VI
  street_racing: Yup.boolean(), // Only for VI
  stunt_driving: Yup.boolean(), // Only for VI
  motorcycle_seating: Yup.boolean(), // Only for VI
  motorcycle_restrictions: Yup.boolean(), // Only for VI
  unlicensed: Yup.boolean(), // Only for VI

  /** Excessive Speed */
  speed_limit: Yup.number(), // Only for VI, required if excessive_speed is true, max 3 digits long
  vehicle_speed: Yup.number(), // Only for VI, required if excessive_speed is true, max 3 digits long
  speed_estimation_technique: Yup.string(), // Only for VI, required if excessive_speed is true, checkbox multi-select
  speed_confirmation_technique: Yup.string(), // Only for VI, required if excessive_speed is true, checkbox multi-select

  /** Unlicenced Driver */
  unlicenced_prohibition_number: Yup.string(), // Only for VI, required if unlicensed is true
  belief_driver_bc_resident: Yup.string(), // Only for VI, required if unlicensed is true
  out_of_province_dl: Yup.string(), // Only for VI, required if unlicensed is true and belief_driver_bc_resident is "Yes"
  out_of_province_dl_number: Yup.string(), // Only for VI, required if unlicensed is true and belief_driver_bc_resident is "Yes"
  out_of_province_dl_jurisdiction: Yup.object(), // Only for VI, required if unlicensed is true and belief_driver_bc_resident is "Yes"
  out_of_province_dl_expiry: Yup.date(), // Only for VI, required if unlicensed is true and belief_driver_bc_resident is "Yes"

  /** Linkage Factors */
  linkage_location_of_keys: Yup.boolean(), // Only for VI
  linkage_location_of_keys_explanation: Yup.string(), // Only for VI, requried if linkage_location_of_keys is true
  linkage_driver_principal: Yup.boolean(), // Only for VI
  linkage_owner_in_vehicle: Yup.boolean(), // Only for VI
  linkage_owner_aware_possesion: Yup.boolean(), // TODO: Fix typo  // Only for VI
  linkage_vehicle_transfer_notice: Yup.boolean(), // Only for VI
  linkage_other: Yup.boolean(), // Only for VI

  /** Incident Details */
  incident_details_extra_page: Yup.boolean(), // Only for VI
  incident_details: Yup.string(), // Only for VI, max 6000 characters

  /** Reasonable Grounds */
  witnessed_by_officer: Yup.boolean(), // Only for 24h / VI
  admission_by_driver: Yup.boolean(), // Only for 24h / VI
  independent_witness: Yup.boolean(), // Only for 24h / VI
  reasonable_ground_other: Yup.boolean(), // Only for 24h / VI
  reasonable_ground_other_reason: Yup.string(), // Only for 24h / VI, required if reasonable_ground_other is true
  prescribed_test_used: Yup.string(), // Only for 24h / VI, required
  reasonable_date_of_test: Yup.date(), // Only for 24h / VI, required if prescribed_test_used is "Yes"
  reasonable_time_of_test: Yup.string(), // Only for 24h / VI, required if prescribed_test_used is "Yes"
  reason_for_not_using_prescribed_test: Yup.string(), // Only for 24h / VI, required if prescribed_test_used is "No"

  /** Test Administred */
  reasonable_test_used_alcohol: prescribedDeviceValidation(
    Yup.ref("prescribed_test_used")
  ), // Only for 24h / VI, required if type_of_prohibition = "alcohol"
  reasonable_test_used_drugs: Yup.string(), // Only for 24h / VI, required if type_of_prohibition = "drugs"
  reasonable_asd_expiry_date: Yup.date()
    .nullable()
    .test(
      "ASD",
      "ASD expiry date is required when ASD is selected",
      function (value) {
        const selectedValue = this.parent["reasonable_test_used_alcohol"];

        if (selectedValue === "alco-sensor" && !value) {
          return this.createError({
            path: "asd_expiry_date",
            message: "This field is required",
          });
        }

        if (value && value < new Date()) {
          return this.createError({
            path: "asd_expiry_date",
            message: "Expired!",
          });
        }

        return true;
      }
    ), // Only for 24h / VI, required if prescribed_test_used = "Yes" and prohibition_type = "alcohol" and reasonable_test_used_alcohol = "alco-sensor", min. value: date_of_driving, max. value: date_of_driving + 28 days
  reasonable_result_alcohol: Yup.string()
    .nullable()
    .test(
      "result_alcohol",
      "Test result is required when alco-sensor is selected",
      function (value) {
        const selectedValue = this.parent["reasonable_test_used_alcohol"];

        if (selectedValue === "alco-sensor" && !value) {
          return this.createError({
            path: "result_alcohol",
            message: "This field is required",
          });
        }

        return true;
      }
    ), // Only for 24h / VI, required if prescribed_test_used = "Yes" and prohibition_type = "alcohol" and reasonable_test_used_alcohol = "alco-sensor"
  reasonable_bac_result_mg: Yup.number()
    .nullable()
    .positive("BAC result must be a positive number")
    .integer("BAC result must be an integer")
    .min(2, "BAC result must be greater than 1")
    .max(998, "BAC result must be less than 999")
    .test(
      "bac_result_mg",
      "bac_result_mg is required when instrument is selected",
      function (value) {
        const selectedValue = this.parent["test-used-alcohol"];

        if (selectedValue === "instrument" && !value) {
          return this.createError({
            path: "bac_result_mg",
            message: "This field is required",
          });
        }

        return true;
      }
    ), // Only for 24h / VI, required if prescribed_test_used = "Yes" and prohibition_type = "alcohol" and reasonable_test_used_alcohol = "instrument", numeric 51-600
  reasonable_approved_instrument_used: Yup.string(), // Only for 24h / VI, required if prescribed_test_used = "Yes" and prohibition_type = "alcohol" and reasonable_test_used_alcohol = "instrument"
  reasonable_can_drive_drug: Yup.boolean(), // Only for 24h / VI, required if prescribed_test_used = "Yes" and reasonable_test_used_acohol = "PPCT"
  reasonable_can_drive_alcohol: Yup.boolean(), // Only for 24h / VI, required if prescribed_test_used = "Yes" and prohibition_type = "alcohol" reasonable_test_used_alcohol = "PPCT"

  /** Officer */
  "officer-lastname": Yup.string().required("Last Name is required"), // Required
  "officer-prime-id": Yup.string().required("PRIME ID is required"), // Required
  "officer-agency": Yup.string().required("Agency is required"), // Required, max. 30 characters

  /** Disposition of Vehicle (12h only) */
  vehicle_location: Yup.string(), // Only for 12h
  vehicle_released_to: Yup.string(), // Change name for 12h form? Or remove this? Only for 12h, required if vehicle_location = "released"
  date_released: Yup.date(), // Change name for 12h form? Or remove this? Only for 12h, required if vehicle_location = "released"
  time_released: Yup.string(), // Change name for 12h form? Or remove this? Only for 12h, required if vehicle_location = "released"
  location_of_keys: Yup.string(), // Change name for 12h form? Or remove this? Only for 12h, required
  "ILO-name": Yup.string(), // Change name for 12h form? Or remove this? Only for 12h, required if vehicle_location = "private"
});
