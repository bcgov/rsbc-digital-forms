import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Input } from "../common/Input/Input";
import "./commonForm.scss";

export const OfficerInfo = () => {
  return (
    <div className="officer-info border-design-form left">
      <h3>Officer</h3>
      <div>
        <Row style={{ minHeight: "85px" }}>
          <Col sm={5}>
            <Input
              className="field-height field-width"
              label="Last Name of Peace Officer Serving Prohibition Notice"
              name="officer-lastname"
              type="text"
              disabled
              required
            />
          </Col>
          <Col sm={3}>
            <Input
              className="field-height field-width"
              label="PRIME ID"
              name="officer-prime-id"
              type="text"
              disabled
              required
            />
          </Col>
          <Col sm={4}>
            <Input
              className="field-height field-width"
              label="Agency or RCMP Detachment"
              name="officer-agency"
              type="text"
              disabled
              required
            />
          </Col>
        </Row>
      </div>
    </div>
  );
};
