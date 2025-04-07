-- Set the form_id to delete (this is the form_id field in form_process_mapper, not the ID)
DO $$
DECLARE
    v_form_id VARCHAR := '67e63af81c5536c61069ad44'; -- Replace with your form_id
    v_form_mapper_id INT;
BEGIN
    -- First, get the form_process_mapper.id for this form_id
    SELECT id INTO v_form_mapper_id 
    FROM form_process_mapper 
    WHERE form_id = v_form_id;
    
    IF v_form_mapper_id IS NULL THEN
        RAISE EXCEPTION 'Form with form_id % not found', v_form_id;
    END IF;

    -- 1. Delete application_audit records
    DELETE FROM application_audit 
    WHERE form_id = v_form_id;

    -- 2. Delete draft records (via application)
    DELETE FROM draft
    WHERE application_id IN (
        SELECT id 
        FROM application 
        WHERE form_process_mapper_id = v_form_mapper_id
    );

    -- 3. Delete application records
    DELETE FROM application
    WHERE form_process_mapper_id = v_form_mapper_id;

    -- 4. Delete form bundling records
    DELETE FROM form_bundling
    WHERE form_process_mapper_id = v_form_mapper_id 
       OR parent_form_id = v_form_id;

    -- 5. Delete form history records
    DELETE FROM form_history
    WHERE form_id = v_form_id;

    -- 6. Update any templates that reference this form
    UPDATE templates
    SET parent_form_id = NULL
    WHERE parent_form_id = v_form_id;

    -- 7. Finally delete the form record itself
    DELETE FROM form_process_mapper
    WHERE id = v_form_mapper_id;
    
    RAISE NOTICE 'Successfully deleted form with form_id % and all related data', v_form_id;
END $$;