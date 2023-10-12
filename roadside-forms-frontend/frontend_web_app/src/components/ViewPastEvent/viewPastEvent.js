import React, { useEffect, useState } from "react";
import { Button } from "../common/Button/Button";
import { useLocation } from "react-router-dom";
import { SVGprint } from "../Forms/Print/svgPrint";
import { formsPNG } from "../../utils/helpers";
import { db } from "../../db";

export const ViewPastEvent = () => {
  const location = useLocation();
  const [event, setEvent] = useState({});
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

  return <div>{renderSVGForm(event, "stageOne")}</div>;
};
