import React, { useState } from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Checkbox } from '../../common/Checkbox/checkbox';
import { TextAreaInput } from '../../common/Input/TextAreaInput';


export const IncidentDetails = (props) => {
    const [input, setInput] = useState("") 
    const handleChange = event => {
        setInput(event.target.value);
      };
    return(
        <div className='border-design-form left text-font'>
            <h3>Incident Details</h3>
            <Row>
                <Col className="left checkboxs">
                    <Checkbox name="incident_details_extra_page" >Will a seperate document be attached?</Checkbox>
                    <span>{input.length + "/2000"}</span>
                    <TextAreaInput  name="incident_details"  className="text-area-height field-width" maxLength="2000" value={input} placeholder="Enter details here..." onChange={handleChange}/>
                </Col>
            </Row>
        </div>
    )
}

IncidentDetails.propTypes = {};