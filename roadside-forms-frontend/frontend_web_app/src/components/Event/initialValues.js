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
    gender: "",
    driver_licence_expiry: "",
    driver_licence_class: "",

    /** Vehicle Information */
    vehicle_jurisdiction: { value: "BC", label: "BRITISH COLUMBIA" },
    vehicle_plate_no: "",
    vehicle_registration_no: "",
    vehicle_year: "",
    vehicle_mk_md: "",
    vehicle_style: "",
    vehicle_colour: [],
    vehicle_vin_no: "",
    nsc_prov_state: { value: "BC", label: "BRITISH COLUMBIA" },
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
    date_of_impound: "",
    vehicle_impounded: "",
    reason_for_not_impounding: "",
    vehicle_released_to: "",
    date_released: "",
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
    offence_city: "",
    agency_file_no: "",
    date_of_driving: "",
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
    speed_limit: "",
    vehicle_speed: "",
    speed_estimation_technique: "",
    speed_confirmation_technique: "",

    /** Unlicenced Driver */
    unlicenced_prohibition_number: "",
    belief_driver_bc_resident: "",
    out_of_province_dl: "",
    out_of_province_dl_number: "",
    out_of_province_dl_jurisdiction: "",
    out_of_province_dl_expiry: "",

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
    reasonable_date_of_test: "",
    reasonable_time_of_test: "",
    reason_for_not_using_prescribed_test: "",

    /** Test Administred */
    resonable_test_used_alcohol: "",
    reasonable_test_used_drugs: "",
    reasonable_asd_expiry_date: "",
    reasonable_result_alcohol: "",
    reasonable_bac_result_mg: "",
    resonable_approved_instrument_used: "",
    reasonable_can_drive_drug: "",
    reasonable_can_drive_alcohol: "",

    /** Officer */
    "officer-lastname": user.last_name || "",
    "officer-prime-id": user.badge_number || "",
    "officer-agency": user.agency || "",

    /** Disposition of Vehicle (12h only) */
    vehicle_location: "",

    /** eCOS */
    confirmation_of_service_date: null,
    "document-served": "",
    confirmation_of_service: false,

    /** Other */
    is_nsc: false,
  };
};
