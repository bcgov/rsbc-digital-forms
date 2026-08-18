DO $$
DECLARE
  counter INT := 0;
	amount_of_forms INT := 299999;
	form_type TEXT := 'IRP';
	prefix TEXT := '4';
	second_part TEXT := '0';
	initial_number int := 700000;
	current_number int := 0;
	form_number TEXT := '';
BEGIN

	SELECT COALESCE(MAX(SUBSTRING(id FROM 3 FOR 6)::INT), 0) INTO current_number
	FROM form
	WHERE form.form_type = 'IRP' AND form.id LIKE prefix || second_part || '%';

	RAISE NOTICE 'current %', current_number ;

	IF initial_number < current_number THEN
		initial_number := current_number;
	END IF;

	RAISE NOTICE 'initial %', initial_number ; 
	WHILE counter < amount_of_forms LOOP
		counter := counter + 1;
		current_number := initial_number + counter;
		IF current_number >= 1000000 THEN
			RAISE EXCEPTION 'Exceeded maximum number of forms for this prefix';
		END IF;
		form_number := prefix || second_part || LPAD(current_number::TEXT, 6, '0');
		RAISE NOTICE 'Form number: %', form_number;
		INSERT INTO form (id, form_type) VALUES 
			(form_number, 'IRP');
	END LOOP;
END;
$$;

-- delete from form f where form_type = 'IRP' and id in ('40999997', '40953088', '40929344', '40802854', '40802203', '40748473');