import { NumericInput } from "../../common/Input/NumericInput";
import { useFormikContext } from "formik";
import { Checkbox } from "../../common/Checkbox/checkbox";
import { Radio } from "../../common/Radio/radio";
import { DatePickerField } from "../../common/DateField/DatePicker";
export const TestAdministered = (props) => {
  const { values } = useFormikContext();
  const typeOfProhibition =
    values["type_of_prohibition"] === "alcohol" && values["TwentyFourHour"]
      ? "Alcohol 215(2)"
      : values["type_of_prohibition"] === "drugs" && values["TwentyFourHour"]
      ? " Drugs 215(3)"
      : values["type_of_prohibition"] === "alcohol" && values["TwelveHour"]
      ? "Alcohol 90.3(2)"
      : "Drugs 90.3(2.1)";
  return (
    <>
      {values["prescribed_test_used"] === "YES" && (
        <div className="border-design-form left text-font">
          <h3>Test Administered - {typeOfProhibition}</h3>
          {values["type_of_prohibition"] === "alcohol" && (
            <div className="test-admin-alcohol">
              <div className="row">
                <div className="col">
                  <Radio
                    label="Which test was used?"
                    name="test_used_alcohol"
                    options={[
                      { label: "Alco-Sensor FST(ASD)", value: "alco-sensor" },
                      { label: "Approved Instrument", value: "instrument" },
                      {
                        label: "Prescribed Physical Coordination Test (SFST)",
                        value: "physical-cordination-test",
                      },
                    ]}
                    required
                  />
                </div>
              </div>
              {values["test_used_alcohol"] === "alco-sensor" && (
                <div className="row">
                  <div className="col-sm-12">
                    <DatePickerField
                      name="asd_expiry_date"
                      label="ASD Expiry Date"
                      className="field-height field-width"
                      required
                    />
                    <Radio
                      label="Result"
                      name="result_alcohol"
                      options={[
                        { label: "51-99 mg%", value: "51-99 mg%" },
                        { label: "Over 99 mg%", value: "Over 99 mg%" },
                      ]}
                      required
                    />
                  </div>
                </div>
              )}
              {values["test_used_alcohol"] === "instrument" && (
                <div className="row">
                  <div className="col-sm-12 mt-2">
                    <NumericInput
                      label="BAC Result(mg%)"
                      name="bac_result_mg"
                      required
                    />
                  </div>
                </div>
              )}
            </div>
          )}
          {values["type_of_prohibition"] === "drugs" && (
            <div className="test-admin-drug">
              <div className="row">
                <div className="col-sm-12">
                  <Radio
                    label="Which test was used?"
                    name="test_used_drugs"
                    options={[
                      { label: "Approved Drug", value: "approved-drug" },
                      {
                        label: "Screening Equipment",
                        value: "screening-equipment",
                      },
                      {
                        label: "Prescribed Physical Coordination Test (SFST)",
                        value: "physical-cordination-test-sfts",
                      },
                      {
                        label: "Prescribed Physical Coordination Test (DRE)",
                        value: "physical-cordination-test-dre",
                      },
                    ]}
                    required
                  />
                </div>
              </div>
              <div className="row">
                <div className="col-sm-12">
                  <span> Test Result </span>
                </div>
                <div className="col-sm-12">
                  <Checkbox name="THC">THC</Checkbox>
                  <Checkbox name="Cocaine">Cocaine</Checkbox>
                </div>
              </div>
            </div>
          )}
        </div>
      )}
    </>
  );
};
