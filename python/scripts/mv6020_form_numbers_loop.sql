DO $$
DECLARE
  counter INT := 0;
	amount_of_forms INT := 20000;
	form_type TEXT := 'MV6020';
	prefix TEXT := 'Z';
	second_part TEXT := 'A';
	initial_number int := 0;
	current_number int := 0;
	form_number TEXT := '';
BEGIN

	SELECT COALESCE(MAX(SUBSTRING(id FROM 3 FOR 6)::INT), 0) INTO initial_number
	FROM form
	WHERE form.form_type = 'MV6020' AND form.id LIKE prefix || second_part || '%';

	WHILE counter < amount_of_forms LOOP
		counter := counter + 1;
		current_number := initial_number + counter;
		IF current_number >= 1000000 THEN
			RAISE EXCEPTION 'Exceeded maximum number of forms for this prefix';
		END IF;
		form_number := prefix || second_part || LPAD(current_number::TEXT, 6, '0');
		RAISE NOTICE 'Form number: %', form_number;
		INSERT INTO form (id, form_type) VALUES 
			(form_number, 'MV6020');
	END LOOP;
END;
$$;