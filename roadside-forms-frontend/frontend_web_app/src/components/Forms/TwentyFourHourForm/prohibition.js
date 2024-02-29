import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useFormikContext } from "formik";
import PropTypes from "prop-types";
import { Radio } from "../../common/Radio/radio";
import { Input } from "../../common/Input/Input";
import { SearchableSelect } from "../../common/Select/SearchableSelect";
import { DatePickerField } from "../../common/DateField/DatePicker";
import { TimeInputField } from "../../common/Input/TimeInputField";

export const Prohibition = (props) => {
  const { values } = useFormikContext();
  const { cities } = props;

  // Do some title work
  // When it's VI, time & place
  // When it's 24 hour, prohibition
  // When it's 12 hour,
  return (
    <div className="border-design-form left text-font">
      <h3>
        {(values["TwentyFourHour"] || values["TwelveHour"]) && "Prohibition"}
        {values["VI"] && values["TwentyFourHour"] && " & "}
        {values["VI"] && "Time and Place"}
      </h3>
      {values["TwentyFourHour"] && (
        <Row>
          <Col>
            <Radio
              label="Type of Prohibition"
              name="type_of_prohibition"
              options={[
                { label: "Alcohol 215(2)", value: "alcohol" },
                { label: "Drugs 215(3)", value: "drugs" },
              ]}
              required
            />
          </Col>
        </Row>
      )}
      {values["TwelveHour"] && (
        <Row>
          <Col>
            <Radio
              label="Type of Prohibition"
              name="type_of_prohibition"
              options={[
                { label: "Alcohol 90.3(2)", value: "alcohol" },
                { label: "Drugs 90.3(2.1)", value: "drugs" },
              ]}
              required
            />
          </Col>
        </Row>
      )}
      <Row>
        <Col sm={8}>
          <Input
            label="Intersection or Address of Offence"
            name="intersection_or_address_of_offence"
            className="field-height field-width"
            type="text"
            required
          ></Input>
        </Col>
        <Col sm={4}>
          <SearchableSelect
            className="field-height field-width"
            label="City"
            name="offence_city"
            options={cities}
            required
          />
        </Col>
      </Row>
      <Row>
        <Col sm={2}>
          <Input
            label="Agency File #"
            name="agency_file_no"
            className="field-height field-width"
            type="text"
            required
          ></Input>
        </Col>
        <Col sm={5}>
          <DatePickerField
            name="date_of_driving"
            label="Date of Driving - care or control"
            className="field-height field-width"
            required
          />
        </Col>
        <Col sm={5}>
          <TimeInputField
            label="Time of Driving - care or control"
            className="field-height field-width"
            name="time_of_driving"
            required
          />
        </Col>
      </Row>
    </div>
  );
};

Prohibition.propTypes = {
  cities: PropTypes.array.isRequired,
};
