import React from 'react';
import CloseIcon from '@mui/icons-material/Close';
import './svgPrint.scss'
import form from '../../../assets/MV2634_102018_driver.png';

const items = {
    "VIOLATION_NUMBER": {
      "field_type": "text",
      "font_size": 18,
      "function": "getFormattedFormId",
      "parameters": "",
      "start": {
        "x": 31,
        "y": 158.9
      }
    },
    "DRIVER_NAME": {
      "field_type": "text",
      "font_size": 10,
      "function": "getValuesConcatenatedWithCommas",
      "parameters": ["last_name","first_name"],
      "start": {
        "x": 33.2,
        "y": 185.4
      }
    },
    "DRIVER_DL_NUMBER": {
      "field_type": "text",
      "font_size": 10,
      "function": "getStringValue",
      "parameters": "drivers_number",
      "start": {
        "x": 33.2,
        "y": 207.8
      }
    },
    "DRIVER_DOB": {
      "field_type": "text",
      "font_size": 10,
      "function": "getFormattedDate",
      "parameters": ["dob", "YYYY-MM-DD"],
      "start": {
        "x": 238,
        "y": 207.8
      }
    },
    "MV2721_IMPOUNDMENT_DURATION_30": {
        "field_type": "checkbox",
        "font_size": 2,
        "function": "isExists",
        "start": {
          "x": 68,
          "y": -161.5
        }
      },
}

export const SVGtest = () => {
    return (
        <div>
            <svg width="700" height="800" xmlns='http://www.w3.org/2000/svg' transform='rotate(-90)'>
                <image href={form} width="100%" height="100%"/>
                {Object.keys(items).map((key, index) => {
                    if(items[key]['field_type'] === "text"){
                        return (<text id={key} x={items[key]["start"]["x"]} y={items[key]["start"]["y"]} fontSize={items[key]["fontSize"]} fill="black">Testing</text>)
                    }else if(items[key]["field_type"] === "checkbox"){
                        return( <CloseIcon id={key} width="15px" className="svg_icons" x={items[key]["start"]["x"]} y={items[key]["start"]["y"]} color="blue"/>)
                    }
                    return null

                })}
            </svg>
        </div>
    );
  }
