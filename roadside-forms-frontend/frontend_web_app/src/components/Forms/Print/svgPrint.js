import React from "react";

import "./svgPrint.scss";
import { printFormatHelper, printCheckHelper } from "../../../utils/helpers";
import formFieldLayout from "./print_layout.json";

export const SVGprint = ({
  form,
  formAspect,
  formLayout,
  formType,
  values,
  impoundLotOperators,
}) => {
  const formFields = formFieldLayout[formLayout][formType];
  const allFormFields = formFieldLayout[formLayout]["fields"];
  const viewBox = formFieldLayout[formLayout]["viewbox"];

  if (Object.keys(values).length) {
    return (
      <div>
        <svg
          viewBox={viewBox}
          xmlns="http://www.w3.org/2000/svg"
          className={"svg-wrapper" + formAspect}
        >
          <image href={form} width="223" height="202" />
          {formFields?.map((item) => {
            if (allFormFields[item]["field_type"] === "text") {
              return (
                <text
                  id={item}
                  x={allFormFields[item]["start"]["x"] + "px"}
                  y={allFormFields[item]["start"]["y"] + "px"}
                  className={allFormFields[item]["classNames"]}
                  fill="black"
                >
                  {printFormatHelper(
                    values,
                    allFormFields[item],
                    item,
                    impoundLotOperators
                  )}
                </text>
              );
            } else if (allFormFields[item]["field_type"] === "checkbox") {
              return (
                <text
                  id={item}
                  x={allFormFields[item]["start"]["x"]}
                  y={allFormFields[item]["start"]["y"]}
                  className={allFormFields[item]["classNames"]}
                >
                  {printCheckHelper(values, allFormFields[item], item)
                    ? "X"
                    : null}
                </text>
              );
            } else if (allFormFields[item]["field_type"] === "always") {
              return (
                <text
                  id={item}
                  x={allFormFields[item]["start"]["x"]}
                  y={allFormFields[item]["start"]["y"]}
                  className={allFormFields[item]["classNames"]}
                >
                  {allFormFields[item]["field_value"]}
                </text>
              );
            } else if (allFormFields[item]["field_type"] === "textArea") {
              return (
                <foreignObject
                  id={item}
                  x={allFormFields[item]["start"]["x"] + "px"}
                  y={allFormFields[item]["start"]["y"] + "px"}
                  className={allFormFields[item]["classNames"]}
                  fill="black"
                >
                  {printFormatHelper(
                    values,
                    allFormFields[item],
                    item,
                    impoundLotOperators
                  )}
                </foreignObject>
              );
            }
            return null;
          })}
          {/* ) */}
        </svg>
      </div>
    );
  }
  return <div />;
};
