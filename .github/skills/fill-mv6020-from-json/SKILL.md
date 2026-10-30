---
name: fill-mv6020-from-json
description: 'Fill an open MV6020 browser form from a local JSON file. Use when asked to load or populate an MV6020 form from JSON, including entities, involved persons, status-dependent Boxes 11–20a, and saving as a draft without submitting.'
argument-hint: 'Path to the MV6020 JSON file'
---

# Fill an MV6020 Form from JSON

Populate a currently open MV6020 form using a local JSON file, then verify the values and draft save. Never submit the form.

## Requirements and safety

- Keep JSON contents in the local workspace/session and the browser page. Do not send form data to external services or print the full payload in chat.
- Use the user's explicit file path when provided. Otherwise use the currently selected/open JSON file if it is accessible. If the file cannot be identified, ask which file to use.
- Use the user's shared browser page. If no page is shared, ask the user to share the form page; do not silently open or use another unrelated form.
- Read the page before changing it. If the page contains an existing draft or user-entered data, ask before replacing it. Do not submit, finalize, or otherwise transmit the form.
- Do not infer missing values or invent statuses or personal data. Preserve source values and let the form's own rules control derived/disabled fields.

## Procedure

1. **Load and validate the JSON.**
   - Parse the file locally. Accept either an MV6020 object with a `data` property or the form data object itself.
   - Confirm it contains an `entities` array. Record the expected entity count and each entity's involved-person count.
   - For each involved person, resolve status from the non-empty `status` field or `status_option.value`. If neither is present, stop and ask for the correct status; do not guess.
   - Preserve the full `{label, value}` object for each selected option. For status, use the matching source `status_option` when its value is available; otherwise use the form's matching option label for that status value.

2. **Inspect the shared page and target form.**
   - Use the browser page tools to read the current page and confirm it is the intended MV6020 form.
   - Identify the active Form.io form instance and confirm its entity component is present. If there are multiple candidate forms or no active form, ask the user which one to use.
   - If the form has existing data that would be replaced, ask before proceeding.

3. **Load the source data while preserving session metadata.**
   - Apply the JSON's form data to the open form using its Form.io form instance and normal submission/value update mechanism so the form recalculates and renders its components.
   - Preserve the open form's session/application metadata (such as current user, application ID/status, submitter identity, draft state, and form details) rather than replacing these with values from the JSON.
   - Do not copy the collision case number from the JSON. Remove `collision_case_num`, `collision_case_prefix` and `form_number` from the source data (or keep the open form's current values) so the form generates the case number itself. Do not patch or re-apply these fields.
   - Confirm the rendered entity and involved-person row counts match the JSON before editing person fields.

4. **Select each involved-person status through the form component.**
   - For every entity and person, set the actual `status_option` select component using its `{label, value}` option. Do not only write a status string into the JSON/submission: the selection triggers the form logic that reveals/enables Boxes 11–20a and configures related fields.
   - Allow the form to process the status change before setting the dependent fields. Reacquire component instances after a redraw if needed.
   - Verify both `status_option.value` and the derived `status` value match the source status.

5. **Populate the person fields and preserve identity.**
   - For people whose status makes the fields applicable, populate the available source values for Box 11–20a: `position_of_person`, `safety_equipment_used`, `ejection_from_vehicle`, `vehicle_occupied`, `severe_injury_location`, `injury_type`, `consciousness_state`, `injured_taken_to`, `injured_taken_by`, `injury_classification`, and `age`.
   - Set select/choice fields using their source option objects, not just their display labels or codes.
   - For the first involved person of each entity, set `given_name`, `surname`, and `sex` to match the entity. Match `age` to `age_at_collision` when that entity field is present. Do not change the remaining involved persons' personal details.
   - Respect status-specific behavior. For example, a `noDriver` status may disable and clear non-applicable fields; do not force values into disabled controls. Skip source fields that are blank, null, or empty objects.

6. **Verify and save only as a draft.**
   - Re-read form state and confirm the form generated a case number (do not compare it to the JSON), entity count, involved-person counts, all statuses, first-person identity matches, and every applicable non-empty source Box 11–20a value.
   - Report any mismatch or calculation error explicitly. Do not claim completion if values were not accepted by the form.
   - Wait until the form indicates it is saved to drafts (or its equivalent save confirmation). Do not click a submit/finalize action.
   - Tell the user the draft was populated and whether it is saved; clearly state that it was not submitted.
