.PHONY: build_start down start_local

# Docker build and start the local docker stack
build_start_common:
	docker compose -f docker-compose.yml build --no-cache && docker compose -f docker-compose.yml up --force-recreate  $(c)

sample_event_rows_to_db:
	docker exec -it rsbc-digital-forms-db-1 psql -U testuser -d test -c "INSERT INTO event (event_id, icbc_sent_status, vi_sent_status, icbc_retry_count, vi_retry_count, driver_licence_no, driver_jurisdiction, driver_last_name, driver_given_name, driver_dob, driver_address, driver_city, driver_prov, driver_postal, driver_phone, vehicle_jurisdiction, vehicle_plate_no, vehicle_registration_no, vehicle_year, vehicle_mk_md, vehicle_style, vehicle_colour, vehicle_vin_no, nsc_prov_state, nsc_no, owned_by_corp, corporation_name, regist_owner_last_name, regist_owner_first_name, regist_owner_address, regist_owner_dob, regist_owner_city, regist_owner_prov, regist_owner_postal, regist_owner_phone, printed, created_dt, updated_dt,created_by) VALUES (1, 'pending', 'pending', 0, 0, 'AB1234567', 'BC', 'Doe', 'John', '1990-01-01', '123 Main St', 'Vancouver', 'BC', 'V6A 1A1', 1234567890, 'BC', 'ABC123', '12345678', '2022', 'Toyota Corolla', 'Sedan', 'Red', '12345678901234567', 'BC', 'BSC1234567', false, NULL, 'Doe', 'Jane', '456 Main St', '1990-01-01', 'Vancouver', 'BC', 'V6A 1A1', 1234567890, false, '2022-11-01 12:00:00', '2022-11-01 12:00:00','123456');"

sample_24h_rows_to_db:
	docker exec -it rsbc-digital-forms-db-1 psql -U testuser -d test -c "INSERT INTO twenty_four_hour_form (form_id, event_id, vehicle_impounded, reason_for_not_impounding, vehicle_released_to, date_released, time_released, location_of_keys, impound_lot_operator, type_of_prohibition, intersection_or_address_of_offence, offence_city, agency_file_no, date_of_driving, time_of_driving, reasonable_ground, reasonable_ground_other, prescribed_test_used, date_of_test, time_of_test, reason_for_not_using_prescribed_test, test_used_alcohol, asd_expiry_date, result_alcohol, bac_result_mg, test_used_drugs, test_result_drugs, requested_prescribed_test, requested_test_used, time_of_requested_test, \"requested_ASD_expiry_date\", requested_alcohol_test_result, \"requested_BAC_result\", requested_approved_instrument_used, created_dt, updated_dt) VALUES (1, 1, true, NULL, 'John Smith', '2022-11-01', '12:00 PM', 'On the driver', 'ABC Impound Lot', 'Immediate Roadside Prohibition', 'Main St and 1st Ave', 'Vancouver', '123456', '2022-11-01', '11:30 AM', 'Odour of liquor', NULL, true, '2022-11-01', '12:30 PM', NULL, 'Approved Screening Device', '2022-11-01', 'Pass', 50, NULL, NULL, false, NULL, NULL, NULL, NULL, NULL, NULL, '2022-11-01 12:00:00', '2022-11-01 12:00:00');"

sample_vi_rows_to_db:
	docker exec -it rsbc-digital-forms-db-1 psql -U testuser -d test -c "INSERT INTO vi_form (form_id, event_id, created_dt, updated_dt, gender, driver_licence_expiry, driver_licence_class, unlicenced_prohibition_number, belief_driver_bc_resident, out_of_province_dl, out_of_province_dl_number, date_of_impound, irp_impound, irp_impound_duration, \"IRP_number\", \"VI_number\", excessive_speed, prohibited, suspended, street_racing, stunt_driving, motorcycle_seating, motorcycle_restrictions, unlicensed, linkage_location_of_keys, linkage_location_of_keys_explanation, linkage_driver_principal, linkage_owner_in_vehicle, linkage_owner_aware_possesion, linkage_vehicle_transfer_notice, linkage_other, speed_limit, vehicle_speed, speed_estimation_technique, speed_confirmation_technique, incident_details, incident_details_extra_page) VALUES(1, 1, '2022-11-01 12:00:00', '2022-11-01 12:00:00', 'Male', '2022-11-01', 'Class 5', '123456', true, false, '', '2022-11-01', false, '', 'IRP123456', 'VI123456', false, false, false, false, false, false, false, false, false, '', false, false, false, false, false, '', '', '', '', '', false);"

sample_user_rows_to_db:
	docker exec -it rsbc-digital-forms-db-1 psql -U testuser -d test -c "INSERT INTO \"user\" (user_guid, business_guid, username, agency, badge_number, last_name, first_name, display_name, login) VALUES ('123456', '789012', 'johndoe', 'ABC Agency', 'AB1234', 'Doe', 'John', 'John Doe', 'johndoe@abcagency.com');"

sample_storage_ref_row:
	docker exec -it rsbc-digital-forms-db-1 psql -U testuser -d test -c "INSERT INTO form_storage_refs (form_id_vi, event_id, form_type, storage_key, created_dt, updated_dt) VALUES (1, 1, 'vi', 'test22/abcd.pdf', '2022-11-01 12:00:00', '2022-11-01 12:00:00');"

populate_test_records: sample_event_rows_to_db sample_24h_rows_to_db sample_vi_rows_to_db sample_storage_ref_row


build_start_form_handler:
	docker compose -f docker-compose-form-handler.yml build --no-cache && docker compose -f docker-compose-form-handler.yml up --force-recreate  $(c)
start_form_handler_local:
	docker compose -f docker-compose-form-handler.yml up --force-recreate  $(c)
down_form_handler:
	docker compose -f docker-compose-form-handler.yml down $(c)

start_local:
	docker compose -f docker-compose.yml up --force-recreate  $(c)

# Stop the local docker stack
down_common:
	docker compose -f docker-compose.yml down $(c)

down_form_handler:
	docker compose -f docker-compose-form-handler.yml down $(c)