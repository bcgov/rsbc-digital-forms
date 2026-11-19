# ICBC Payload Field Mappings

## Overview
This document maps ICBC payload fields to their source data columns from the dataframe (`event_data`, `form_data`, `user_data`).

## Field Mappings Table

| ICBC Payload Field | Source Column | Source Table | Notes |
|---|---|---|---|
| `dlNumber` | `driver_licence_no` | `event_data` | Padded to 8 digits with leading zeros if shorter |
| `dlJurisdiction` | `driver_jurisdiction` | `event_data` | Mapped via JurisdictionCrossRef lookup to `icbc_jurisdiction_code` |
| `lastName` | `driver_last_name` | `event_data` | Converted to uppercase |
| `firstName` | `driver_given_name` | `event_data` | Converted to uppercase |
| `birthdate` | `driver_dob` | `event_data` | Formatted as `YYYYMMDD` |
| `plateJurisdiction` | `vehicle_jurisdiction` | `event_data` | Mapped via JurisdictionCrossRef lookup to `icbc_jurisdiction_code` |
| `plateNumber` | `vehicle_plate_no` | `event_data` | Converted to uppercase and spaces removed |
| `pujCode` | `nsc_prov_state` | `event_data` | Mapped via JurisdictionCrossRef lookup to `icbc_jurisdiction_code` |
| `nscNumber` | `nsc_no` | `event_data` | National Safety Code number (conditional on both `nsc_prov_state` and `nsc_no` present) |
| `section` | `type_of_prohibition` + `event_type` | `event_data` | Conditional mapping: <br> - alcohol + 12h → "90.32" <br> - alcohol + 24h → "215.2" <br> - drugs + 12h → "90.321" <br> - drugs + 24h → "215.3" |
| `violationLocation` | `offence_city` | `event_data` | Mapped via CityCrossRef lookup to `icbc_city_name_legacy` |
| `noticeNumber` | `twelve_hour_number` or `twenty_four_hour_number` | `form_data` | Depends on `event_type` (12h or 24h) |
| `violationDate` | `date_of_driving` | `event_data` | Converted to local timezone and formatted as `YYYYMMDD` |
| `violationTime` | `time_of_driving` | `event_data` | Spaces removed |
| `officerDetachment` | `agency_id` | `user_data` | Mapped via AgencyCrossref lookup to `icbc_city_name`, converted to uppercase |
| `officerNumber` | `badge_number` | `user_data` | Direct mapping |
| `officerName` | `last_name` | `user_data` | Converted to uppercase |
| `pdf` | `file_data` (parameter) | Direct | PDF file data passed directly |

## Source Data Tables/Objects

### event_data
Contains violation and vehicle information:
- `driver_licence_no`
- `driver_jurisdiction`
- `driver_last_name`
- `driver_given_name`
- `driver_dob`
- `vehicle_jurisdiction`
- `vehicle_plate_no`
- `nsc_prov_state`
- `nsc_no`
- `type_of_prohibition` (alcohol or drugs)
- `offence_city`
- `date_of_driving`
- `time_of_driving`

### form_data
Contains form-specific information:
- `twelve_hour_number`
- `twenty_four_hour_number`

### user_data
Contains officer/agency information:
- `agency` (agency name)
- `agency_id`
- `badge_number`
- `last_name`

### Direct Parameters
- `file_data`: PDF file data (passed directly)
- `event_type`: Type of event (12h or 24h) - used for conditional logic

## Cross-Reference Tables Used

1. **JurisdictionCrossRef**: Maps jurisdiction codes to ICBC jurisdiction codes
   - Lookup field: `jurisdiction_code`
   - Returns field: `icbc_jurisdiction_code`

2. **CityCrossRef**: Maps city codes to ICBC city names
   - Lookup field: `city_code`
   - Returns field: `icbc_city_name_legacy`

3. **AgencyCrossref**: Maps agency IDs to ICBC city names
   - Lookup field: `agency_id`
   - Returns field: `icbc_city_name`
