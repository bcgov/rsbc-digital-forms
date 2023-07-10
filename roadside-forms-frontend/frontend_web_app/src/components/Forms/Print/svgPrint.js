import React from 'react';

import './svgPrint.scss'
import { printFormatHelper, printCheckHelper} from '../../../utils/helpers';
import formLayout from './print_layout.json'

export const SVGprint = ({form, formAspect, formType, values}) => {
    return (
        <div>
            <svg viewBox='0 0 223 210' xmlns='http://www.w3.org/2000/svg' className={'svg-wrapper' + formAspect}>
                <image href={form} width="223" height="202"/>
                {Object.keys(formLayout[formType]).map((key,index) => {
                    const currentLayout = formLayout[formType]
                    if(currentLayout[key]['field_type'] === "text"){
                        return (<text id={key} x={currentLayout[key]["start"]["x"]+"px"} y={currentLayout[key]["start"]["y"]+"px"} className={currentLayout[key]["classNames"]} fill="black">{printFormatHelper(values,currentLayout[key], key)}</text>)
                    }else if(currentLayout[key]["field_type"] === "checkbox"){
                        return( <text id={key} x={currentLayout[key]["start"]["x"]} y={currentLayout[key]["start"]["y"]} className={currentLayout[key]["classNames"]}>{printCheckHelper(values,currentLayout[key], key) ? "X" : null }</text>)
                    }else if(currentLayout[key]["field_type"] === "always"){
                        return( <text id={key} x={currentLayout[key]["start"]["x"]} y={currentLayout[key]["start"]["y"]} className={currentLayout[key]["classNames"]}>{currentLayout[key]["field_value"]}</text>)
                    }
                    return null
                })}
            </svg>
        </div>
    );
  }
