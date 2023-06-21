import React from 'react';

import './svgPrint.scss'
import { printFormatHelper } from '../../../utils/helpers';
import form from '../../../assets/MV2634_102018_driver.png';
import * as data from './print_layout.json'

export const SVGprint = ({values}) => {
    console.log(values)
    return (
        <div>
            <svg viewBox='0 0 223 210' xmlns='http://www.w3.org/2000/svg' className='svg-wrapper'>
                <image href={form} width="223" height="202"/>
                {Object.keys(data).map((key, index) => {
                    if(data[key]['field_type'] === "text"){
                        return (<text id={key} x={data[key]["start"]["x"]+"px"} y={data[key]["start"]["y"]+"px"} className="fontSmall" fill="black">{printFormatHelper(values,data[key], key)}</text>)
                    }else if(data[key]["field_type"] === "checkbox"){
                        return( <text id={key} x={data[key]["start"]["x"]} y={data[key]["start"]["y"]} className="fontText">X</text>)
                    }
                    return null

                })}
            </svg>
        </div>
    );
  }
