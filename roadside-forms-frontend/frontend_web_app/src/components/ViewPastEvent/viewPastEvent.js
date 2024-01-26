import React, { useEffect, useState } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import Select from "react-select";
import { useLocation, useNavigate } from "react-router-dom";
import { SVGprint } from "../Forms/Print/svgPrint";
import { formsPNG, staticResources } from "../../utils/helpers";
import { db } from "../../db";
import { ArrowBack } from "@mui/icons-material";
import { useRecoilValue } from "recoil";

export const ViewPastEvent = () => {
  const location = useLocation();
  const [event, setEvent] = useState({});
  const [selected, setSelected] = useState("pastEvent");
  const state = location.state;
  const navigate = useNavigate();
  const impoundAtom = useRecoilValue(staticResources["impound_lot_operators"]);

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

  const options = [
    { value: "pastEvent", label: "Police/ICBC" },
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
              impoundLotOperators={impoundAtom}
            />
          );
        }
      }
    }
    return componentsToRender;
  };
  return (
    <div style={{ marginTop: "15px" }}>
      <Row id="history-button-container">
        <Col sm={2}>
          <Button
            style={{ marginLeft: "10px" }}
            variant="primary"
            onClick={() => navigate("/")}
          >
            <ArrowBack />
            Return to Dashboard
          </Button>
        </Col>
        <Col sm={{ span: 4, offset: 2 }}>
          <Select
            defaultValue={options[0]}
            name="Print"
            options={options}
            onChange={(e) => {
              setSelected(e.value);
            }}
          />
        </Col>
        <Col sm={2}>
          <Button variant="primary" onClick={() => window.print()}>
            Print
          </Button>
        </Col>
      </Row>
      {renderSVGForm(event, selected)}
    </div>
  );
};
