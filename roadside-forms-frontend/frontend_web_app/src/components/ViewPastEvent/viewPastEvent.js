import React, { useEffect, useState } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import Select from "react-select";
import { useLocation } from "react-router-dom";
import { SVGprint } from "../Forms/Print/svgPrint";
import { formsPNG } from "../../utils/helpers";
import { db } from "../../db";

export const ViewPastEvent = () => {
  const location = useLocation();
  const [event, setEvent] = useState({});
  const [selected, setSelected] = useState("stageTwo");
  const state = location.state;

  useEffect(() => {
    try {
      db.event
        .where("event_id")
        .equals(state.eventId)
        .first()
        .then((value) => setEvent(value));
    } catch (error) {
      console.log(error);
    }
  }, [setEvent, state]);

  console.log(event);
  const options = [
    { value: "stageTwo", label: "Police/ICBC" },
    { value: "stageOne", label: "Driver/ILO" },
  ];

  const renderSVGForm = (values, renderStage) => {
    const forms = {
      TwentyFourHour: values["TwentyFourHour"],
      TwelveHour: values["TwelveHour"],
      IRP: values["IRP"],
      VI: values["VI"],
    };
    const componentsToRender = [];
    for (const item in forms) {
      if (forms[item]) {
        for (const form in formsPNG[renderStage][item]) {
          if (form === "ILO" && values["vehicle_impounded"] === "NO") {
            break;
          }
          componentsToRender.push(
            <SVGprint
              key={item + form}
              form={formsPNG[renderStage][item][form]["png"]}
              formAspect={formsPNG[renderStage][item][form]["aspectClass"]}
              formLayout={item}
              formType={form}
              values={values}
            />
          );
        }
      }
    }
    return componentsToRender;
  };
  return (
    <div>
      <Row id="history-button-container">
        <Col sm={{ span: 4, offset: 4 }}>
          <Select
            defaultValue={options[0]}
            name="Print"
            options={options}
            onChange={(e) => {
              setSelected(e.value);
            }}
          />
        </Col>
        <Col sm={4}>
          <Button variant="primary" onClick={() => window.print()}>
            Print
          </Button>
        </Col>
      </Row>
      {renderSVGForm(event, selected)}
    </div>
  );
};
