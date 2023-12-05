import { useRecoilValue } from "recoil";
import { userAtom } from "../../atoms/users";

export const InitialValues = () => {
  const user = useRecoilValue(userAtom);

  return {
    /** Form Types */
    VI: false,
    TwelveHour: false,
    TwentyFourHour: false,
    IRP: false,

    /** Driver's Information */
    driver_licence_no: "",
    drivers_licence_jurisdiction: { value: "BC", label: "BRITISH COLUMBIA" },
    driver_last_name: "",
    driver_given_name: "",
    driver_dob: "",
    driver_address: "",
    driver_phone: "",
    driver_city: "",
    driver_prov_state: { value: "BC", label: "BRITISH COLUMBIA" },
    driver_postal: "",
    gender: {},
    driver_licence_expiry: null,
    driver_licence_class: "",

    /** Vehicle Information */
    vehicle_jurisdiction: { value: "BC", label: "BRITISH COLUMBIA" },
    vehicle_plate_no: "",
    vehicle_registration_no: "",
    vehicle_year: null,
    vehicle_mk_md: null,
    vehicle_style: null,
    vehicle_colour: [],
    vehicle_vin_no: "",
    nsc_prov_state: null,
    nsc_no: "",
    owned_by_corp: false,
    driver_is_regist_owner: false,
    regist_owner_last_name: "",
    regist_owner_first_name: "",
    regist_owner_dob: "",
    corporation_name: "",
    regist_owner_address: "",
    regist_owner_phone: "",
    regist_owner_email: "",
    regist_owner_city: "",
    regist_owner_prov_state: { value: "BC", label: "BRITISH COLUMBIA" },
    regist_owner_postal: "",

    /** Vehicle Impoundment or Disposition (24h/VI Only) */
    date_of_impound: null,
    vehicle_impounded: "",
    reason_for_not_impounding: "",
    vehicle_released_to: "",
    date_released: null,
    time_released: "",
    location_of_keys: "",
    "ILO-name": "",
    "ILO-address": "",
    "ILO-city": "",
    "ILO-phone": "",
    "ILO-options": {},

    /** Prohibition */
    type_of_prohibition: "",
    intersection_or_address_of_offence: "",
    offence_city: null,
    agency_file_no: "",
    date_of_driving: null,
    time_of_driving: "",

    /** Impondment for Immediate Roadside Prohibition */
    irp_impound: "",
    irp_impound_duration: "",
    IRP_number: "",
    VI_number: "",

    /** Impoundment for Driving Behaviour */
    excessive_speed: false,
    prohibited: false,
    suspended: false,
    street_racing: false,
    stunt_driving: false,
    motorcycle_seating: false,
    motorcycle_restrictions: false,
    unlicensed: false,

    /** Excessive Speed */
    speed_limit: null,
    vehicle_speed: null,
    speed_estimation_technique: "",
    speed_confirmation_technique: "",

    /** Unlicenced Driver */
    unlicenced_prohibition_number: "",
    belief_driver_bc_resident: "",
    out_of_province_dl: "",
    out_of_province_dl_number: "",
    out_of_province_dl_jurisdiction: null,
    out_of_province_dl_expiry: null,

    /** Linkage Factors */
    linkage_location_of_keys: false,
    linkage_location_of_keys_explanation: "",
    linkage_driver_principal: false,
    linkage_owner_in_vehicle: false,
    linkage_owner_aware_possesion: false,
    linkage_vehicle_transfer_notice: false,
    linkage_other: false,

    /** Incedent Details */
    incident_details_extra_page: false,
    incident_details: "",

    /** Reasonable Grounds */
    witnessed_by_officer: false,
    admission_by_driver: false,
    independent_witness: false,
    reasonable_ground_other: false,
    reasonable_ground_other_reason: "",
    prescribed_test_used: "",
    reasonable_date_of_test: null,
    reasonable_time_of_test: "",
    reason_for_not_using_prescribed_test: "",

    /** Test Administred */
    resonable_test_used_alcohol: "",
    reasonable_test_used_drugs: "",
    reasonable_asd_expiry_date: null,
    reasonable_result_alcohol: "",
    reasonable_bac_result_mg: null,
    resonable_approved_instrument_used: "",
    reasonable_can_drive_drug: false,
    reasonable_can_drive_alcohol: false,

    /** Officer */
    "officer-lastname": user.last_name || "",
    "officer-prime-id": user.badge_number || "",
    "officer-agency": user.agency || "",

    /** Disposition of Vehicle (12h only) */
    vehicle_location: "",

    /** eCOS */
    confirmation_of_service_date: null,
    document_served: "",
    confirmation_of_service: false,

    /** Police Details */
    requested_prescribed_test: "",
    requested_test_used_alcohol: "",
    requested_test_used_drug: "",
    time_of_requested_test: "",
    requested_ASD_expiry_date: null,
    requested_alcohol_test_result: "",
    requested_BAC_result: null,
    requested_approved_instrument_used: "",
    requested_can_drive_drug: false,
    requested_can_drive_alcohol: false,

    /** Other */
    is_nsc: false,
    ecos_confirmed: false,
    form_printed_successfully: false,
  };
};
