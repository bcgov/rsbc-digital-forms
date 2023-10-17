import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useFormikContext } from "formik";
import { NumericInput } from "../../common/Input/NumericInput";
import { Input } from "../../common/Input/Input";
import { Radio } from "../../common/Radio/radio";
import { TimeInputField } from "../../common/Input/TimeInputField";
import { DatePickerField } from "../../common/DateField/DatePicker";

export const PoliceDetails = (props) => {
  const { values } = useFormikContext();
  console.log(values["requested_prescribed_test"]);
  return (
    <div className="border-design-form left text-font">
      <Row>
        <Col>
          <Radio
            label="Did the Driver request a breath test or prescribed physical coordination test?"
            name="requested_prescribed_test"
            options={[
              { label: "Yes", value: "Yes" },
              { label: "No", value: "No" },
            ]}
            required
          />
        </Col>
      </Row>
      {values["requested_prescribed_test"] === "Yes" && (
        <div>
          <div className="test-admin-alcohol">
            <Row>
              <Col>
                <Radio
                  label="If yes, what test was administered?"
                  name="requested_test_used"
                  options={[
                    {
                      label: "Yes, Alco-Sensor FST(ASD)",
                      value: "alco-sensor",
                    },
                    { label: "Yes, Approved Instrument", value: "instrument" },
                    {
                      label:
                        "Yes, Prescribed Physical Coordination Test (SFST)",
                      value: "physical-cordination-test",
                    },
                    {
                      label:
                        "No test was administered in forming reasonable grounds",
                      value: "no-test",
                    },
                  ]}
                  required
                />
              </Col>
              {(values["requested_test_used"] === "instrument" ||
                values["requested_test_used"] === "physical-cordination-test" ||
                values["requested_test_used"] === "alco-sensor") && (
                <Col sm={4}>
                  <TimeInputField
                    label="Time the test was administered"
                    className="field-height field-width"
                    name="time_of_requested_test"
                    required
                  />
                </Col>
              )}
            </Row>
            {values["requested_test_used"] === "alco-sensor" && (
              <Row>
                <Col sm={12}>
                  <DatePickerField
                    name="requested_ASD_expiry_date"
                    label="ASD Expiry Date"
                    className="field-height field-width"
                    required
                  />
                  <Radio
                    label="Result"
                    name="requested_alcohol_test_result"
                    options={[
                      { label: "51-99 mg%", value: "51-99 mg%" },
                      { label: "Over 99 mg%", value: "Over 99 mg%" },
                    ]}
                    required
                  />
                </Col>
              </Row>
            )}

            {values["requested_test_used"] === "instrument" && (
              <Row>
                <Col sm={4}>
                  <NumericInput
                    label="BAC Result(mg%)"
                    name="requested_BAC_result"
                    required
                  />
                </Col>
                <Col sm={4}>
                  <Input
                    label="Approved Instrument used"
                    name="requested_approved_instrument_used"
                    required
                  />
                </Col>
              </Row>
            )}
          </div>
        </div>
      )}{" "}
    </div>
  );
};
