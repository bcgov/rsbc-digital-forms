import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useFormikContext } from "formik";
import { Input } from "../../common/Input/Input";
import { NumericInput } from "../../common/Input/NumericInput";
import { Checkbox } from "../../common/Checkbox/checkbox";
import { Radio } from "../../common/Radio/radio";
import { DatePickerField } from "../../common/DateField/DatePicker";
import { useEffect, useState } from "react";
export const TestAdministered = (props) => {
  const { values } = useFormikContext();

  const [typeOfProhibition, setTypeOfProhibition] = useState("");

  useEffect(() => {
    if (values["TwentyFourHour"]) {
      if (values["type_of_prohibition"] === "alcohol") {
        setTypeOfProhibition("Alcohol 215(2)");
      }
      if (values["type_of_prohibition"] === "drugs") {
        setTypeOfProhibition("Drugs 215(2.1)");
      }
    }
    if (values["TwelveHour"]) {
      if (values["type_of_prohibition"] === "alcohol") {
        setTypeOfProhibition("Alcohol 90.3(2)");
      }
      if (values["type_of_prohibition"] === "drugs") {
        setTypeOfProhibition("Drugs 90.3(2.1)");
      }
    }
  }, [
    values["TwentyFourHour"],
    values["TwelveHour"],
    values["type_of_prohibition"],
  ]);

  useEffect(() => {
    if (values["prescribed_test_used"] === "NO") {
      values["resonable_test_used_alcohol"] = "";
      values["reasonable_test_used_drugs"] = "";
      values["reasonable_asd_expiry_date"] = null;
      values["reasonable_result_alcohol"] = "";
      values["reasonable_bac_result_mg"] = null;
      values["resonable_approved_instrument_used"] = "";
      values["reasonable_can_drive_drug"] = false;
      values["reasonable_can_drive_alcohol"] = false;
    }
  }, [values["prescribed_test_used"]]);

  useEffect(() => {
    if (values["type_of_prohibition"] === "alcohol") {
      // alco-sensor / instrument / PPCT
      if (values["resonable_test_used_alcohol"] !== "alco-sensor") {
        values["reasonable_asd_expiry_date"] = null;
        values["reasonable_result_alcohol"] = "";
      }
      if (values["resonable_test_used_alcohol"] !== "instrument") {
        values["reasonable_bac_result_mg"] = null;
        values["resonable_approved_instrument_used"] = "";
      }
      if (values["resonable_test_used_alcohol"] !== "PPCT") {
        values["reasonable_can_drive_alcohol"] = false;
      }
    }
  }, [values["resonable_test_used_alcohol"]]);

  useEffect(() => {
    if (values["type_of_prohibition"] === "drugs") {
      if (values["reasonable_test_used_drugs"] !== "PPCT") {
        values["reasonable_can_drive_drug"] = false;
      }
      if (values["reasonable_test_used_drugs"] !== "approved-drug") {
        values["reasonable_approved_instrument_used"] = "";
      }
    }
  }, [values["reasonable_test_used_drugs"]]);

  return (
    <>
      {values["prescribed_test_used"] === "YES" && (
        <div className="border-design-form left text-font">
          <h3>Test Administered - {typeOfProhibition}</h3>
          {values["type_of_prohibition"] === "alcohol" && (
            <div className="test-admin-alcohol">
              <Row>
                <Col>
                  <Radio
                    label="Which test was used?"
                    name="resonable_test_used_alcohol"
                    options={[
                      { label: "Alco-Sensor FST(ASD)", value: "alco-sensor" },
                      { label: "Approved Instrument", value: "instrument" },
                      {
                        label: "Prescribed Physical Coordination Test",
                        value: "PPCT",
                      },
                    ]}
                    required
                  />
                </Col>
              </Row>
              {values["resonable_test_used_alcohol"] === "alco-sensor" && (
                <Row>
                  <Col sm={12}>
                    <DatePickerField
                      name="reasonable_asd_expiry_date"
                      label="ASD Expiry Date"
                      className="field-height field-width"
                      required
                    />
                    <Radio
                      label="Result"
                      name="reasonable_result_alcohol"
                      options={[
                        { label: "51-59 mg%", value: "51-59" },
                        { label: "Warn", value: "WARN" },
                        { label: "Fail", value: "FAIL" },
                      ]}
                      required
                    />
                  </Col>
                </Row>
              )}
              {values["resonable_test_used_alcohol"] === "instrument" && (
                <Row>
                  <Col sm={4}>
                    <NumericInput
                      label="BAC Result(mg%)"
                      name="reasonable_bac_result_mg"
                      required
                    />
                  </Col>
                  <Col sm={4}>
                    <Input
                      label="Approved Instrument Used"
                      name="resonable_approved_instrument_used"
                      required
                    />
                  </Col>
                </Row>
              )}
            </div>
          )}
          {values["type_of_prohibition"] === "drugs" && (
            <div className="test-admin-drug">
              <Row>
                <Col sm={12}>
                  <Radio
                    label="Which test was used?"
                    name="reasonable_test_used_drugs"
                    options={[
                      { label: "Approved Instrument", value: "approved-drug" },
                      {
                        label: "Prescribed Physical Coordination Test",
                        value: "PPCT",
                      },
                    ]}
                    required
                  />
                </Col>
              </Row>
              {/* <Row>
                <Col sm={12}>
                  <span> Test Result </span>
                </Col>
                <Col sm={12}>
                  <Checkbox name="THC">THC</Checkbox>
                  <Checkbox name="Cocaine">Cocaine</Checkbox>
                </Col>
              </Row> */}
            </div>
          )}
          {values["type_of_prohibition"] === "drugs" &&
            values["reasonable_test_used_drugs"] === "PPCT" && (
              <Row>
                <Col sm={4}>
                  <Checkbox name="reasonable_can_drive_drug">
                    Ability to drive affected by a drug?
                  </Checkbox>
                </Col>
              </Row>
            )}
          {values["type_of_prohibition"] === "drugs" &&
            values["reasonable_test_used_drugs"] === "approved-drug" && (
              <Row>
                <Col sm={4}>
                  <Input
                    label="Approved Instrument Used"
                    name="resonable_approved_instrument_used"
                    required
                  />
                </Col>
              </Row>
            )}
          {values["type_of_prohibition"] === "alcohol" &&
            values["resonable_test_used_alcohol"] === "PPCT" && (
              <Row>
                <Col sm={6}>
                  <Checkbox name="reasonable_can_drive_alcohol">
                    Ability to drive affected by alcohol? (only select if PPCT
                    test used)
                  </Checkbox>
                </Col>
              </Row>
            )}
        </div>
      )}
    </>
  );
};
