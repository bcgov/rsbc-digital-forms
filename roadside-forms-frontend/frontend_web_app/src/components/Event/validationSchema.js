/** FIXME:
 * Fix typos:
 * - reasonable
 * - possesion
 * - license / licence
 */

import * as Yup from "yup";
import moment from "moment-timezone";

const validateRequiredDateWithMax = (
  selectedValue,
  errorPath,
  maxDate,
  errorMessage
) => {
  return function (value) {
    if (selectedValue && !value) {
      return this.createError({
        path: errorPath,
        message: errorMessage,
      });
    }

    if (selectedValue && value) {
      const today = moment().startOf("day");
      const yesterday = moment().subtract(1, "days").startOf("day");
      if (
        !moment(value).isSame(today, "day") &&
        !moment(value).isSame(yesterday, "day")
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

export const validationSchema = Yup.object().shape(
  {
    /** Form Types */
    VI: Yup.boolean(),
    TwelveHour: Yup.boolean(),
    TwentyFourHour: Yup.boolean(),
    IRP: Yup.boolean(),

    /** Driver's Information */
    driver_licence_no: Yup.string(),
    drivers_licence_jurisdiction: Yup.object().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () =>
        Yup.object()
          .required("Jurisdiction is required")
          .test(
            "jurisdiction_valid",
            "Please select a valid jurisdiction for drivers licence.",
            (option) => {
              return option.value !== "XX" && option.value !== "XZ";
            }
          ),
    }), // Only for 24h / VI
    driver_last_name: Yup.string().required("Last Name is required"),
    driver_given_name: Yup.string(),
    driver_dob: Yup.string()
      .nullable()
      .test("dob-validation", "Invalid Date of Birth", function (dob) {
        if (!dob) {
          // Return true if the field is empty
          return true;
        }

        const currentDate = moment();
        const inputDate = moment(dob);

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
    driver_phone: Yup.string()
      .notRequired()
      .matches(/^$|^\d{3}-\d{3}-\d{4}$/, "Phone Number format ###-###-####"),
    driver_city: Yup.string(),
    driver_prov_state: Yup.object().test(
      "driver_provState_valid",
      "Please select a valid province, state, or country for driver.",
      (option) => {
        return option.value !== "XX" && option.value !== "XZ";
      }
    ),
    driver_postal: Yup.string(),
    // gender: Yup.string(), // Only for VI
    driver_licence_expiry: Yup.date()
      .nullable()
      .when("VI", {
        is: true,
        then: () =>
          Yup.date()
            .nullable()
            .min(
              new Date(1980, 0, 1),
              "Licence expiry date cannot be earlier than 1980"
            ), // Cannot be less than 1980. Only for VI
      }),
    driver_licence_class: Yup.string().when("VI", {
      is: true,
      then: () =>
        Yup.string()
          .matches(
            /^$|^\d{1,3}(,\d{1,3})*$/,
            "DL Class may be up to three classes, separated by commas"
          )
          .max(5, "Up to three classes are permitted"), // Up to three digits, separated by commas. Only for VI
    }),

    /** Vehicle Information */
    vehicle_jurisdiction: Yup.object().test(
      "vehicle_jurisdiction_valid",
      "Please select a valid province, state, or country for vehicle info.",
      (option) => {
        return option.value !== "XX" && option.value !== "XZ";
      }
    ), // Select one
    vehicle_plate_no: Yup.string(),
    vehicle_registration_no: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () =>
        Yup.string().max(20, "Registration No. must be 20 characters or less"),
    }), // Max 20 characters, only for 24h / VI
    vehicle_year: Yup.object().nullable().required("Vehicle Year is required"), // Select one
    vehicle_mk_md: Yup.object().nullable().required("Make / Model is required"), // Select one
    vehicle_style: Yup.object().nullable().required("Style is required"), // Select one
    vehicle_colour: Yup.array()
      .required("Color is required")
      .min(1, "Select at least one vehicle colour")
      .max(2, "Select at most two colours"), // Select up 1-2
    vehicle_vin_no: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () =>
        Yup.string()
          .required("VIN is required")
          .min(13, "VIN must be at least 13 characters")
          .max(18, "VIN must be 20 characters or less"), // 13-18 characters, only for 24h / VI
    }),

    nsc_prov_state: Yup.object()
      .nullable()
      .when(["nsc_no"], {
        is: (nsc_no) => !!nsc_no && nsc_no.length > 0,
        then: () =>
          Yup.object()
            .nullable()
            .required("NSC Province/State is required when NSC no. is provided")
            .test(
              "nsc_prov_state",
              "Please select a valid NSC Province/State.",
              (option) => {
                return option.value !== "";
              }
            ),
        otherwise: () => Yup.object().nullable(),
      }),

    nsc_no: Yup.string()
      .max(14, "NSC no. must be 14 characters or less")
      .when(["nsc_prov_state"], {
        is: (nsc_prov_state) => !!nsc_prov_state && !!nsc_prov_state.value,
        then: () =>
          Yup.string()
            .required("NSC no. is required when NSC Province/State is provided")
            .max(14, "NSC no. must be 14 characters or less"),
        otherwise: () => Yup.string(),
      }),

    /** Registered Owner */
    owned_by_corp: Yup.boolean().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.boolean(),
    }), // Only for 24h / VI
    driver_is_regist_owner: Yup.boolean().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.boolean(),
    }), // Only for VI
    regist_owner_last_name: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.string(),
    }), // Only for 24h / VI
    regist_owner_first_name: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.string(),
    }), // Only for 24h / VI
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
            message: "Registered Owner must be between 10 to 120 years old",
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
            message: "Registered Owner must be at least 10 years old",
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
    corporation_name: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.string(),
    }), // Only for 24h / VI
    regist_owner_address: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.string(),
    }), // Only for 24h / VI
    regist_owner_phone: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () =>
        Yup.string().matches(
          /^$|^\d{3}-\d{3}-\d{4}$/,
          "Phone Number format ###-###-####"
        ),
    }),
    regist_owner_email: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.string().email(),
    }), // Only for 24h / VI
    regist_owner_city: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.string(),
    }), // Only for 24h / VI
    regist_owner_prov_state: Yup.object().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () =>
        Yup.object().test(
          "regist_owner_prov_state_valid",
          "Please select a valid province, state, or country for vehicle's registered owner.",
          (option) => {
            return option.value !== "XX" && option.value !== "XZ";
          }
        ),
    }), // Only for 24h / VI
    regist_owner_postal: Yup.string().when(["VI", "TwentyFourHour"], {
      is: (VI, TwentyFourHour) => VI || TwentyFourHour,
      then: () => Yup.string(),
    }), // Only for 24h / VI

    /** Vehicle Impoundment or Disposition (24h/VI Only) */
    date_of_impound: Yup.date()
      .nullable()
      .max(new Date(), "Date of impound cannot be a future date")
      .when(["VI", "form_printed_successfully"], {
        is: (VI, form_printed_successfully) => VI && !form_printed_successfully,
        then: () =>
          Yup.date()
            .max(new Date(), "Date of impound cannot be a future date")
            .required("Date of impound is required")
            .test(
              "date_of_impound",
              "Date of Impound is required",
              validateRequiredDateWithMax(
                Yup.ref("TwentyFourHour"),
                "date_of_impound",
                new Date(),
                "Date of impound is required"
              )
            )
            .test(
              "date_of_impound",
              "Date of Impound cannot be before date of driving",
              function (value) {
                if (value && this.parent.date_of_driving) {
                  return (
                    moment(value).startOf("day") >=
                    moment(this.parent.date_of_driving).startOf("day")
                  );
                }
                return true;
              }
            ),
      }), // Only for VI, required if VI is selected

    vehicle_impounded: Yup.string().when("TwentyFourHour", {
      is: true,
      then: () => Yup.string().required("Vehicle impounded field is required"),
    }), // Only for 24h
    reason_for_not_impounding: Yup.string().when(
      ["TwentyFourHour", "vehicle_impounded"],
      {
        is: (TwentyFourHour, vehicle_impounded) =>
          TwentyFourHour && vehicle_impounded === "NO",
        then: () =>
          Yup.string().required("Reason for not impounding field is required"),
      }
    ), // Only for 24h / VI, required if vehicle_impounded = "No"
    vehicle_released_to: Yup.string()
      .nullable()
      .when(
        [
          "TwentyFourHour",
          "TwelveHour",
          "vehicle_impounded",
          "reason_for_not_impounding",
          "vehicle_location",
        ],
        {
          is: (
            TwentyFourHour,
            TwelveHour,
            vehicle_impounded,
            reason_for_not_impounding,
            vehicle_location
          ) =>
            // (TwentyFourHour || TwelveHour) &&
            // vehicle_impounded === "NO" &&
            // reason_for_not_impounding === "released",
            (TwentyFourHour &&
              vehicle_impounded === "NO" &&
              reason_for_not_impounding === "released") ||
            (TwelveHour && vehicle_location === "released"),
          then: () => Yup.string().required("Vehicle Released To is required"),
        }
      ),
    date_released: Yup.date()
      .nullable()
      .when(
        [
          "TwentyFourHour",
          "TwelveHour",
          "vehicle_impounded",
          "reason_for_not_impounding",
          "vehicle_location",
          "form_printed_successfully",
        ],
        {
          is: (
            TwentyFourHour,
            TwelveHour,
            vehicle_impounded,
            reason_for_not_impounding,
            vehicle_location,
            form_printed_successfully
          ) =>
            ((TwentyFourHour &&
              vehicle_impounded === "NO" &&
              reason_for_not_impounding === "released") ||
              (TwelveHour &&
                (vehicle_location === "released" ||
                  vehicle_location === "private"))) &&
            !form_printed_successfully,
          then: () =>
            Yup.date()
              .nullable()
              .max(new Date(), "Date of release cannot be a future date")
              .test(
                "released",
                "Date of release is required when release is selected",
                validateRequiredDateWithMax(
                  Yup.ref("reason_for_not_impounding"),
                  "date_released",
                  new Date(),
                  "Date released is required"
                )
              ),
        }
      ), // Only for 24h / VI, required if vehicle_impounded = "No" and reason_for_not_impounding = "released"
    // Need to make sure this is after time of driving - care or ctrl
    time_released: Yup.string()
      .nullable()
      .when(
        [
          "TwentyFourHour",
          "TwelveHour",
          "vehicle_impounded",
          "reason_for_not_impounding",
          "vehicle_location",
        ],
        {
          is: (
            TwentyFourHour,
            TwelveHour,
            vehicle_impounded,
            reason_for_not_impounding,
            vehicle_location
          ) =>
            (TwentyFourHour &&
              vehicle_impounded === "NO" &&
              reason_for_not_impounding === "released") ||
            (TwelveHour &&
              (vehicle_location === "released" ||
                vehicle_location === "private")),
          then: () =>
            Yup.string()
              .required("Time released is required")
              .matches(
                /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/,
                "Time Released must match 24h format HH:MM"
              )
              .test(
                "time_released",
                "Time released cannot be in the future",
                function (value) {
                  if (value && this.parent.date_released) {
                    return (
                      moment(this.parent.date_released)
                        .set("hour", value.slice(0, 2))
                        .set("minute", value.slice(3)) <= moment()
                    );
                  }
                  return true;
                }
              )
              .test(
                "time_released",
                "Release time must be at least 1 minute after time of driving - care or control",
                function (value) {
                  if (
                    this.parent.date_of_driving &&
                    this.parent.time_of_driving &&
                    this.parent.date_released &&
                    value
                  ) {
                    const dateOfDriving = moment(this.parent.date_of_driving);
                    const timeOfDriving = moment(
                      this.parent.time_of_driving,
                      "HHmm"
                    );
                    const dateOfTest = moment(this.parent.date_released);
                    const timeOfTest = moment(value, "HHmm");

                    const timeOfDrivingCareOrControl = moment(dateOfDriving)
                      .add(timeOfDriving.hours(), "hours")
                      .add(timeOfDriving.minutes(), "minutes");

                    const testTime = moment(dateOfTest)
                      .add(timeOfTest.hours(), "hours")
                      .add(timeOfTest.minutes(), "minutes");

                    return timeOfDrivingCareOrControl.isBefore(testTime);
                  }
                }
              ),
        }
      ), // Only for 24h / VI, required if vehicle_impounded = "No" and reason_for_not_impounding = "released"
    location_of_keys: Yup.string().when(
      ["TwentyFourHour", "TwelveHour", "vehicle_impounded", "vehicle_location"],
      {
        is: (TwentyFourHour, TwelveHour, vehicle_impounded, vehicle_location) =>
          (TwentyFourHour && vehicle_impounded === "YES") ||
          (TwelveHour && vehicle_location === "roadside"),
        then: () => {
          return Yup.string().required("Location of keys is required");
        },
      }
    ), // Only for 24h / VI, required if vehicle_impounded = "Yes"
    "ILO-name": Yup.string().when(
      ["TwentyFourHour", "VI", "vehicle_impounded"],
      {
        is: (TwentyFourHour, VI, vehicle_impounded) => {
          return (TwentyFourHour || VI) && vehicle_impounded === "YES";
        },
        then: () => {
          return Yup.string().required("Impound Lot Operator Name is required");
        },
      }
    ), // Only for 24h / VI, required if vehicle_impounded = "Yes"
    "ILO-address": Yup.string().when(
      ["TwentyFourHour", "VI", "vehicle_impounded"],
      {
        is: (TwentyFourHour, VI, vehicle_impounded) => {
          return (TwentyFourHour || VI) && vehicle_impounded === "YES";
        },
        then: () => {
          return Yup.string().required("Public Lot Address is required");
        },
      }
    ), // Only for 24h / VI, required if vehicle_impounded = "Yes"
    "ILO-city": Yup.string().when(
      ["TwentyFourHour", "VI", "vehicle_impounded"],
      {
        is: (TwentyFourHour, VI, vehicle_impounded) => {
          return (TwentyFourHour || VI) && vehicle_impounded === "YES";
        },
        then: () => {
          return Yup.string().required("ILO City is required");
        },
      }
    ), // Only for 24h / VI, required if vehicle_impounded = "Yes"
    "ILO-phone": Yup.string().when(
      ["TwentyFourHour", "VI", "vehicle_impounded"],
      {
        is: (TwentyFourHour, VI, vehicle_impounded) => {
          return (TwentyFourHour || VI) && vehicle_impounded === "YES";
        },
        then: () => {
          return Yup.string().required("Public Phone Number is required");
        },
      }
    ), // Only for 24h / VI, required if vehicle_impounded = "Yes"

    /** Prohibition */
    type_of_prohibition: Yup.string().when(["TwentyFourHour", "TwelveHour"], {
      is: (TwentyFourHour, TwelveHour) => TwentyFourHour || TwelveHour,
      then: () =>
        Yup.string()
          .required("Type of prohibition is required")
          .oneOf(
            ["alcohol", "drugs"],
            "Please select an option for type of prohibition"
          ),
    }), // Required for 12h and 24h forms
    intersection_or_address_of_offence: Yup.string().when(
      ["TwentyFourHour", "TwelveHour", "VI"],
      {
        is: (TwentyFourHour, TwelveHour, VI) =>
          TwentyFourHour || TwelveHour || VI,
        then: () =>
          Yup.string()
            .required("Intersection or Address of Offence is required")
            .max(
              30,
              "Intersection or Address of Offence must be 30 characters or less"
            ),
      }
    ), // Required, max 30 characters
    offence_city: Yup.object()
      .nullable()
      .when(["TwentyFourHour", "TwelveHour", "VI"], {
        is: (TwentyFourHour, TwelveHour, VI) =>
          TwentyFourHour || TwelveHour || VI,
        then: () => Yup.object().required("Offence city is required"),
      }), // Required, dropdown, pick one, BC municipalities only
    agency_file_no: Yup.string().when(["TwentyFourHour", "TwelveHour", "VI"], {
      is: (TwentyFourHour, TwelveHour, VI) =>
        TwentyFourHour || TwelveHour || VI,
      then: () => Yup.string().required("Agency File # is required"),
    }),
    date_of_driving: Yup.date()
      .nullable()
      .when(
        ["TwentyFourHour", "TwelveHour", "VI", "form_printed_successfully"],
        {
          is: (TwentyFourHour, TwelveHour, VI, form_printed_successfully) =>
            (TwentyFourHour || TwelveHour || VI) && !form_printed_successfully,
          then: () =>
            Yup.date()
              .max(new Date(), "Date of driving cannot be a future date")
              .nullable()
              .test(
                "prohibition",
                "Date of driving is required",
                validateRequiredDateWithMax(
                  Yup.ref("TwentyFourHour"),
                  "date_of_driving",
                  new Date(),
                  "Date of driving is required"
                )
              ),
        }
      ), // Required, must be today or yesterday
    time_of_driving: Yup.string().when(["TwentyFourHour", "TwelveHour", "VI"], {
      is: (TwentyFourHour, TwelveHour, VI) =>
        TwentyFourHour || TwelveHour || VI,
      then: () =>
        Yup.string()
          .required("Time of Driving is required")
          .matches(
            /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/,
            "Time of Driving must match 24h format HH:MM"
          )
          .test(
            "time_of_driving",
            "Time of Driving cannot be in the future",
            function (value) {
              if (value && this.parent.date_of_driving) {
                return (
                  moment(this.parent.date_of_driving)
                    .set("hour", value.slice(0, 2))
                    .set("minute", value.slice(3)) <= moment()
                );
              }
              return true;
            }
          ),
    }),

    /** Impoundment for Immediate Roadside Prohibition */
    irp_impound: Yup.string().when(["VI", "TwelveHour", "TwentyFourHour"], {
      is: (VI, TwelveHour, TwentyFourHour) =>
        VI && !TwelveHour && !TwentyFourHour,
      then: () => Yup.string().required("Was an IRP issued? is required"),
    }), // Only for VI, required
    irp_impound_duration: Yup.string().when(
      ["VI", "TwelveHour", "TwentyFourHour", "irp_impound"],
      {
        is: (VI, TwelveHour, TwentyFourHour, irp_impound) =>
          VI && !TwelveHour && !TwentyFourHour && irp_impound === "YES",
        then: () => Yup.string().required("IRP Impound Duration is required"),
      }
    ), // Only for VI, only if irp_impound === "Yes"
    IRP_number: Yup.string().when(
      ["VI", "TwelveHour", "TwentyFourHour", "irp_impound"],
      {
        is: (VI, TwelveHour, TwentyFourHour, irp_impound) =>
          VI && !TwelveHour && !TwentyFourHour && irp_impound === "YES",
        then: () => Yup.string().required("IRP Number is required"),
      }
    ), // Only for VI, required
    VI_number: Yup.string().when(
      ["VI", "TwelveHour", "TwentyFourHour", "irp_impound"],
      {
        is: (VI, TwelveHour, TwentyFourHour, irp_impound) =>
          VI && !TwelveHour && !TwentyFourHour && irp_impound === "YES",
        then: () => Yup.string().required("This VI Number is required"),
      }
    ), // Only for VI, required

    /** Impoundment for Driving Behaviour */
    excessive_speed: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    prohibited: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    suspended: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    street_racing: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    stunt_driving: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    motorcycle_seating: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    motorcycle_restrictions: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    unlicensed: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI

    impoundment_reason: Yup.object()
      .shape({
        /** Reasonable Grounds */
        excessive_speed: Yup.boolean().when("VI", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for VI
        prohibited: Yup.boolean().when("VI", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for VI
        suspended: Yup.boolean().when("VI", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for VI
        street_racing: Yup.boolean().when("VI", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for VI
        stunt_driving: Yup.boolean().when("VI", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for VI
        motorcycle_seating: Yup.boolean().when("VI", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for VI
        motorcycle_restrictions: Yup.boolean().when("VI", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for VI
        unlicensed: Yup.boolean().when("VI", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for VI
      })
      .test(
        "at_least_one_impoundment_reason",
        "Please select at least one option from the list of Impoundment for Driving Behaviour",
        function (value) {
          if (this.parent.VI && 
            (this.parent.TwelveHour || this.parent.TwentyFourHour || this.parent.irp_impound === "NO")) {
            // At least one is required
            return (
              this.parent.excessive_speed ||
              this.parent.prohibited ||
              this.parent.suspended ||
              this.parent.street_racing ||
              this.parent.stunt_driving ||
              this.parent.motorcycle_seating ||
              this.parent.motorcycle_restrictions ||
              this.parent.unlicensed
            );
          }
          return true;
        }
      ),

    /** Excessive Speed */
    speed_limit: Yup.number()
      .nullable()
      .when(["VI", "excessive_speed"], {
        is: (VI, excessive_speed) => VI && excessive_speed,
        then: () =>
          Yup.number()
            .required("Speed Limit is required")
            .max(999, "Speed Limit must be 3 digits or less"),
      }), // Only for VI, required if excessive_speed is true, max 3 digits long
    vehicle_speed: Yup.number()
      .nullable()
      .when(["VI", "excessive_speed"], {
        is: (VI, excessive_speed) => VI && excessive_speed,
        then: () =>
          Yup.number()
            .required("Vehicle Speed is required")
            .max(999, "Vehicle Speed must be 3 digits or less")
            .test(
              "vehicle_speed",
              "Vehicle Speed must be at least 41km/h above the speed limit",
              function (value) {
                if (value && this.parent.speed_limit) {
                  return value >= this.parent.speed_limit + 41;
                }
                return true;
              }
            ),
      }), // Only for VI, required if excessive_speed is true, max 3 digits long
    speed_estimation_technique: Yup.string().when(["VI", "excessive_speed"], {
      is: (VI, excessive_speed) => VI && excessive_speed,
      then: () =>
        Yup.string().required("Speed estimation technique is required"),
    }), // Only for VI, required if excessive_speed is true, checkbox multi-select
    speed_confirmation_technique: Yup.string().when(["VI", "excessive_speed"], {
      is: (VI, excessive_speed) => VI && excessive_speed,
      then: () =>
        Yup.string().required("Speed confirmation technique is required"),
    }), // Only for VI, required if excessive_speed is true, checkbox multi-select

    /** unlicensed Driver */
    unlicenced_prohibition_number: Yup.string().when(["VI", "unlicensed"], {
      is: (VI, unlicensed) => VI && unlicensed,
      then: () => Yup.string().required("UL Prohibition Number is required"),
    }), // Only for VI, required if unlicensed is true
    belief_driver_bc_resident: Yup.string().when(["VI", "unlicensed"], {
      is: (VI, unlicensed) => VI && unlicensed,
      then: () =>
        Yup.string().required("Belief driver is BC resident is required"),
    }), // Only for VI, required if unlicensed is true
    out_of_province_dl: Yup.string().when(["VI", "unlicensed"], {
      is: (VI, unlicensed) => VI && unlicensed,
      then: () => Yup.string().required("Out of Province DL? is required"),
    }), // Only for VI, required if unlicensed is true and belief_driver_bc_resident is "Yes"
    out_of_province_dl_number: Yup.string().when(
      ["VI", "unlicensed", "belief_driver_bc_resident"],
      {
        is: (VI, unlicensed, belief_driver_bc_resident, out_of_province_dl) =>
          VI && unlicensed && belief_driver_bc_resident && out_of_province_dl,
        then: () =>
          Yup.string().required("Out of Province DL Number is required"),
      }
    ), // Only for VI, required if unlicensed is true and belief_driver_bc_resident is "Yes"
    out_of_province_dl_jurisdiction: Yup.object()
      .nullable()
      .when(["VI", "unlicensed", "belief_driver_bc_resident"], {
        is: (VI, unlicensed, belief_driver_bc_resident, out_of_province_dl) =>
          VI && unlicensed && belief_driver_bc_resident && out_of_province_dl,
        then: () =>
          Yup.object().required("Out of Province DL Jurisdiction is required"),
      }), // Only for VI, required if unlicensed is true and belief_driver_bc_resident is "Yes"
    out_of_province_dl_expiry: Yup.date()
      .nullable()
      .when(["VI", "unlicensed", "belief_driver_bc_resident"], {
        is: (VI, unlicensed, belief_driver_bc_resident, out_of_province_dl) =>
          VI && unlicensed && belief_driver_bc_resident && out_of_province_dl,
        then: () =>
          Yup.date().required("Out of Province DL Expiry Date is required"),
      }), // Only for VI, required if unlicensed is true and belief_driver_bc_resident is "Yes"

    /** Linkage Factors */
    linkage_location_of_keys: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    linkage_location_of_keys_explanation: Yup.string().when("VI", {
      is: true,
      then: () => Yup.string(),
    }), // Only for VI, requried if linkage_location_of_keys is true
    linkage_driver_principal: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    linkage_owner_in_vehicle: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    linkage_owner_aware_possesion: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    linkage_vehicle_transfer_notice: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    linkage_other: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI

    /** Incident Details */
    incident_details_extra_page: Yup.boolean().when("VI", {
      is: true,
      then: () => Yup.boolean(),
    }), // Only for VI
    incident_details: Yup.string().when("VI", {
      is: true,
      then: () =>
        Yup.string().max(
          4000,
          "Incident Details must be 4000 characters or less"
        ),
    }), // Only for VI, max 4000 characters

    reasonable_grounds: Yup.object()
      .shape({
        /** Reasonable Grounds */
        witnessed_by_officer: Yup.boolean().when("TwentyFourHour", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for 24h
        admission_by_driver: Yup.boolean().when("TwentyFourHour", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for 24h
        independent_witness: Yup.boolean().when("TwentyFourHour", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for 24h
        reasonable_ground_other: Yup.boolean().when("TwentyFourHour", {
          is: true,
          then: () => Yup.boolean(),
        }), // Only for 24h
      })
      .test(
        "at_least_one_reasonable_grounds",
        "Please select at least one option from the list of reasonable grounds",
        function (value) {
          if (this.parent.TwentyFourHour) {
            return (
              this.parent.witnessed_by_officer ||
              this.parent.admission_by_driver ||
              this.parent.independent_witness ||
              this.parent.reasonable_ground_other
            );
          }
          return true;
        }
      ),

    reasonable_ground_other_reason: Yup.string().when(
      ["TwentyFourHour", "reasonable_ground_other"],
      {
        is: (TwentyFourHour, reasonable_ground_other) =>
          TwentyFourHour && reasonable_ground_other,
        then: () =>
          Yup.string().required("Reasonable Grounds: Other is required"),
      }
    ), // Only for 24h required if reasonable_ground_other is true
    prescribed_test_used: Yup.string().when("TwentyFourHour", {
      is: true,
      then: () => Yup.string().required("Prescribed Test Used is required"),
    }), // Only for 24h required
    reasonable_date_of_test: Yup.date()
      .nullable()
      .when(["TwentyFourHour", "prescribed_test_used"], {
        is: (TwentyFourHour, prescribed_test_used) =>
          TwentyFourHour && prescribed_test_used === "YES",
        then: () =>
          Yup.date()
            .required("Date of Test is required")
            .max(
              moment().endOf("day"),
              "Date of Test cannot be a future date"
            ),
      }), // Only for 24h required if prescribed_test_used is "Yes"
    reasonable_time_of_test: Yup.string().when(
      ["TwentyFourHour", "prescribed_test_used"],
      {
        is: (TwentyFourHour, prescribed_test_used) =>
          TwentyFourHour && prescribed_test_used === "YES",
        then: () =>
          Yup.string()
            .required("Time of Test is required")
            .matches(
              /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/,
              "Time of Test must match 24h format HH:MM"
            )
            .test(
              "reasonable_time_of_test",
              "Time of test must be at least 1 minute after time of driving - care or control",
              function (value) {
                if (
                  this.parent.date_of_driving &&
                  this.parent.time_of_driving &&
                  this.parent.reasonable_date_of_test &&
                  value
                ) {
                  const dateOfDriving = moment(this.parent.date_of_driving);
                  const timeOfDriving = moment(
                    this.parent.time_of_driving,
                    "HHmm"
                  );
                  const dateOfTest = moment(
                    this.parent.reasonable_date_of_test
                  );
                  const timeOfTest = moment(value, "HHmm");

                  const timeOfDrivingCareOrControl = moment(dateOfDriving)
                    .add(timeOfDriving.hours(), "hours")
                    .add(timeOfDriving.minutes(), "minutes");

                  const testTime = moment(dateOfTest)
                    .add(timeOfTest.hours(), "hours")
                    .add(timeOfTest.minutes(), "minutes");

                  return timeOfDrivingCareOrControl.isBefore(testTime);
                }
              }
            )
            .test(
              "reasonable_time_of_test",
              "Time of test cannot be in the future",
              function (value) {
                if (value && this.parent.reasonable_date_of_test) {
                  return (
                    moment(this.parent.reasonable_date_of_test)
                      .set("hour", value.slice(0, 2))
                      .set("minute", value.slice(3)) <= moment()
                  );
                }
                return true;
              }
            ),
      }
    ), // Only for 24h required if prescribed_test_used is "Yes",
    reason_for_not_using_prescribed_test: Yup.string().when(
      ["TwentyFourHour", "prescribed_test_used"],
      {
        is: (TwentyFourHour, prescribed_test_used) =>
          TwentyFourHour && prescribed_test_used === "NO",
        then: () =>
          Yup.string().required("Reason for not prescribing test is required"),
      }
    ), // Only for 24h, required if prescribed_test_used is "No"

    /** Test Administred */
    resonable_test_used_alcohol: Yup.string().when(
      ["TwentyFourHour", "type_of_prohibition", "prescribed_test_used"],
      {
        is: (TwentyFourHour, type_of_prohibition, prescribed_test_used) =>
          TwentyFourHour &&
          type_of_prohibition === "alcohol" &&
          prescribed_test_used === "YES",
        then: () =>
          Yup.string().required("Type of test used - alcohol is required"),
      }
    ), // Only for 24h / VI, required if type_of_prohibition = "alcohol"
    reasonable_test_used_drugs: Yup.string().when(
      ["TwentyFourHour", "type_of_prohibition", "prescribed_test_used"],
      {
        is: (TwentyFourHour, type_of_prohibition, prescribed_test_used) =>
          TwentyFourHour &&
          type_of_prohibition === "drugs" &&
          prescribed_test_used === "YES",
        then: () =>
          Yup.string().required("Type of test used - drugs is required"),
      }
    ), // Only for 24h / VI, required if type_of_prohibition = "drugs"
    reasonable_asd_expiry_date: Yup.date()
      .nullable()
      .when(
        [
          "TwentyFourHour",
          "type_of_prohibition",
          "resonable_test_used_alcohol",
          "prescribed_test_used",
        ],
        {
          is: (
            TwentyFourHour,
            type_of_prohibition,
            resonable_test_used_alcohol,
            prescribed_test_used
          ) =>
            TwentyFourHour &&
            type_of_prohibition === "alcohol" &&
            resonable_test_used_alcohol === "alco-sensor" &&
            prescribed_test_used === "YES",
          then: () =>
            Yup.date()
              .nullable()
              .required("ASD Expiry Date is required")
              .min(moment().startOf("day"), "ASD Test is expired")
              .max(
                moment().add(28, "days").startOf("day").toDate(),
                "ASD Test is expired"
              ),
        }
      ), // Only for 24h, required if prescribed_test_used = "Yes" and type_of_prohibition = "alcohol" and reasonable_test_used_alcohol = "alco-sensor", min. value: date_of_driving, max. value: date_of_driving + 28 days
    reasonable_result_alcohol: Yup.string().when(
      [
        "TwentyFourHour",
        "type_of_prohibition",
        "resonable_test_used_alcohol",
        "prescribed_test_used",
      ],
      {
        is: (
          TwentyFourHour,
          type_of_prohibition,
          resonable_test_used_alcohol,
          prescribed_test_used
        ) =>
          TwentyFourHour &&
          type_of_prohibition === "alcohol" &&
          resonable_test_used_alcohol === "alco-sensor" &&
          prescribed_test_used === "YES",
        then: () => Yup.string().required("ASD Result is required"),
      }
    ), // Only for 24h, required if prescribed_test_used = "Yes" and type_of_prohibition = "alcohol" and reasonable_test_used_alcohol = "alco-sensor"
    reasonable_bac_result_mg: Yup.number()
      .nullable()
      .when(
        [
          "TwentyFourHour",
          "type_of_prohibition",
          "resonable_test_used_alcohol",
          "prescribed_test_used",
        ],
        {
          is: (
            TwentyFourHour,
            type_of_prohibition,
            resonable_test_used_alcohol,
            prescribed_test_used
          ) =>
            TwentyFourHour &&
            type_of_prohibition === "alcohol" &&
            resonable_test_used_alcohol === "instrument" &&
            prescribed_test_used === "YES",
          then: () =>
            Yup.number()
              .required("BAC result is required")
              .positive("BAC result must be a positive number")
              .integer("BAC result must be an integer")
              .min(2, "BAC result must be greater than 1")
              .max(998, "BAC result must be less than 999"),
        }
      ), // Only for 24h, required if prescribed_test_used = "Yes" and type_of_prohibition = "alcohol" and reasonable_test_used_alcohol = "instrument", numeric 51-600
    resonable_approved_instrument_used: Yup.string().when(
      [
        "TwentyFourHour",
        "type_of_prohibition",
        "resonable_test_used_alcohol",
        "reasonable_test_used_drugs",
        "prescribed_test_used",
      ],
      {
        is: (
          TwentyFourHour,
          type_of_prohibition,
          resonable_test_used_alcohol,
          reasonable_test_used_drugs,
          prescribed_test_used
        ) =>
          (TwentyFourHour &&
            prescribed_test_used === "YES" &&
            type_of_prohibition === "alcohol" &&
            resonable_test_used_alcohol === "instrument") ||
          (type_of_prohibition === "drugs" &&
            reasonable_test_used_drugs === "approved-drug"),

        then: () =>
          Yup.string().required("Approved Instrument Used is required"),
      }
    ), // Only for 24h, required if prescribed_test_used = "Yes" and type_of_prohibition = "alcohol" and reasonable_test_used_alcohol = "instrument"
    reasonable_can_drive_drug: Yup.boolean().when(
      ["TwentyFourHour", "type_of_prohibition", "reasonable_test_used_drugs"],
      {
        is: (TwentyFourHour, type_of_prohibition, reasonable_test_used_drugs) =>
          TwentyFourHour &&
          type_of_prohibition === "drugs" &&
          reasonable_test_used_drugs === "PPCT",
        then: () =>
          Yup.boolean().oneOf(
            [true],
            "Ability to drive affected by a drug must be checked"
          ),
      }
    ), // Only for 24h, required if prescribed_test_used = "Yes" and reasonable_test_used_acohol = "PPCT"
    reasonable_can_drive_alcohol: Yup.boolean().when(
      ["TwentyFourHour", "type_of_prohibition", "resonable_test_used_alcohol"],
      {
        is: (
          TwentyFourHour,
          type_of_prohibition,
          resonable_test_used_alcohol
        ) =>
          TwentyFourHour &&
          type_of_prohibition === "alcohol" &&
          resonable_test_used_alcohol === "PPCT",
        then: () =>
          Yup.boolean().oneOf(
            [true],
            "Ability to drive affected by alcohol must be checked"
          ),
      }
    ), // Only for 24h, required if prescribed_test_used = "Yes" and type_of_prohibition = "alcohol" reasonable_test_used_alcohol = "PPCT"

    /** Officer */
    "officer-lastname": Yup.string().required("Last Name is required"), // Required
    "officer-prime-id": Yup.string().required("PRIME ID is required"), // Required
    "officer-agency": Yup.string().required("Agency is required"), // Required, max. 30 characters

    /** Disposition of Vehicle (12h only) */
    vehicle_location: Yup.string().when(["TwelveHour", "VI"], {
      is: (TwelveHour, VI) => TwelveHour && !VI,
      then: () => Yup.string().required("Vehicle Location is required"),
    }), // Only for 12h

    /** eCOS (12h and 24h only) */
    document_served: Yup.string().when(
      ["TwelveHour", "TwentyFourHour", "form_printed_successfully"],
      {
        is: (TwelveHour, TwentyFourHour, form_printed_successfully) =>
          (TwelveHour || TwentyFourHour) && form_printed_successfully,
        then: () => Yup.string().required("Document served is required"),
      }
    ),
    confirmation_of_service: Yup.boolean().when(
      ["form_printed_successfully", "document_served", "VI"],
      {
        is: (form_printed_successfully, document_served, VI) =>
          form_printed_successfully && !VI && document_served === "YES",
        then: () =>
          Yup.boolean().oneOf([true], "Confirmation of service is required"),
      }
    ),

    /** Police Details (24h only) */
    requested_prescribed_test: Yup.string().when(
      [
        "TwentyFourHour",
        "form_printed_successfully",
        "ecos_confirmed",
        "prescribed_test_used",
      ],
      {
        is: (
          TwentyFourHour,
          form_printed_successfully,
          ecos_confirmed,
          prescribed_test_used
        ) =>
          TwentyFourHour &&
          form_printed_successfully &&
          ecos_confirmed &&
          prescribed_test_used === "NO",
        then: () =>
          Yup.string().required("Requested prescribed test is required"),
      }
    ),
    requested_test_used_alcohol: Yup.string().when(
      ["requested_prescribed_test", "type_of_prohibition"],
      {
        is: (requested_prescribed_test, type_of_prohibition) =>
          requested_prescribed_test === "YES" &&
          type_of_prohibition === "alcohol",
        then: () => Yup.string().required("Test administred is required"),
      }
    ),
    requested_test_used_drug: Yup.string().when(
      ["requested_prescribed_test", "type_of_prohibition"],
      {
        is: (requested_prescribed_test, type_of_prohibition) =>
          requested_prescribed_test === "YES" &&
          type_of_prohibition === "drugs",
        then: () => Yup.string().required("Test administred is required"),
      }
    ),
    time_of_requested_test: Yup.string().when(
      ["requested_prescribed_test", "requested_test_used_alcohol"],
      {
        is: (requested_prescribed_test, requested_test_used_alcohol) =>
          requested_prescribed_test === "YES" &&
          (requested_test_used_alcohol === "instrument" ||
            requested_test_used_alcohol === "alco-sensor" ||
            requested_test_used_alcohol === "PPCT"),
        then: () =>
          Yup.string()
            .required("Time of requested test is required")
            .matches(
              /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/,
              "Time of requested test must match 24h format HH:MM"
            ),
        // .test(
        //   "time_of_requested_test valdation",
        //   "Time of Requested test must be after time of driving.",
        //   function (time_of_requested_test) {
        //     if (time_of_requested_test && this.parent.time_of_driving) {
        //       const test_date = moment(this.parent.date_of_driving)
        //         .set("hour", time_of_requested_test.slice(0, 2))
        //         .set("minute", time_of_requested_test.slice(3));
        //       const driving_date = moment(this.parent.date_of_driving)
        //         .set("hour", this.parent.time_of_driving.slice(0, 2))
        //         .set("minute", this.parent.time_of_driving.slice(3));

        //       return test_date > driving_date;
        //     }
        //     return true;
        //   }
        // )
        // .test(
        //   "time_of_requested_test valdation",
        //   "Time of Requested test cannot be in the future.",
        //   function (time_of_requested_test) {
        //     if (time_of_requested_test && this.parent.time_of_driving) {
        //       const test_date = moment(this.parent.date_of_driving)
        //         .set("hour", time_of_requested_test.slice(0, 2))
        //         .set("minute", time_of_requested_test.slice(3));
        //       const driving_date = moment(this.parent.date_of_driving)
        //         .set("hour", this.parent.time_of_driving.slice(0, 2))
        //         .set("minute", this.parent.time_of_driving.slice(3));

        //       return test_date > driving_date;
        //     }
        //     return true;
        //   }
        // ),
      }
    ),
    requested_ASD_expiry_date: Yup.date()
      .nullable()
      .when(["requested_prescribed_test", "requested_test_used_alcohol"], {
        is: (requested_prescribed_test, requested_test_used_alcohol) =>
          requested_prescribed_test === "YES" &&
          requested_test_used_alcohol === "alco-sensor",
        then: () =>
          Yup.date()
            .nullable()
            .required("ASD Expiry Date is required")
            .min(moment().startOf("day"), "ASD Test is expired")
            .max(
              moment().add(28, "days").startOf("day").toDate(),
              "ASD Test is expired"
            ),
      }),
    requested_alcohol_test_result: Yup.string().when(
      ["requested_prescribed_test", "requested_test_used_alcohol"],
      {
        is: (requested_prescribed_test, requested_test_used_alcohol) =>
          requested_prescribed_test === "YES" &&
          requested_test_used_alcohol === "alco-sensor",
        then: () => Yup.string().required("ASD Result is required"),
      }
    ),
    requested_BAC_result: Yup.number()
      .nullable()
      .when(["requested_prescribed_test", "requested_test_used_alcohol"], {
        is: (requested_prescribed_test, requested_test_used_alcohol) =>
          requested_prescribed_test === "YES" &&
          requested_test_used_alcohol === "instrument",
        then: () =>
          Yup.number()
            .required("BAC result is required")
            .positive("BAC result must be a positive number")
            .integer("BAC result must be an integer")
            .min(2, "BAC result must be greater than 1")
            .max(998, "BAC result must be less than 999"),
      }),
    requested_approved_instrument_used: Yup.string().when(
      [
        "requested_prescribed_test",
        "requested_test_used_alcohol",
        "requested_test_used_drug",
      ],
      {
        is: (
          requested_prescribed_test,
          requested_test_used_alcohol,
          requested_test_used_drug
        ) =>
          requested_prescribed_test === "YES" &&
          (requested_test_used_alcohol === "instrument" ||
            requested_test_used_drug === "approved-drug"),
        then: () =>
          Yup.string().required("Approved Instrument Used is required"),
      }
    ),
    requested_can_drive_drug: Yup.boolean().when(
      ["requested_prescribed_test", "requested_test_used_drug"],
      {
        is: (requested_prescribed_test, requested_test_used_drug) =>
          requested_prescribed_test === "YES" &&
          requested_test_used_drug === "PPCT",
        then: () =>
          Yup.boolean().oneOf(
            [true],
            "Ability to drive affected by a drug must be checked"
          ),
      }
    ),
    requested_can_drive_alcohol: Yup.boolean().when(
      ["requested_prescribed_test", "requested_test_used_alcohol"],
      {
        is: (requested_prescribed_test, requested_test_used_alcohol) =>
          requested_prescribed_test === "YES" &&
          requested_test_used_alcohol === "PPCT",
        then: () =>
          Yup.boolean().oneOf(
            [true],
            "Ability to drive affected by alcohol must be checked"
          ),
      }
    ),
  },
  ["nsc_no", "nsc_prov_state"]
);
