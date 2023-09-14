import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Checkbox } from '../../common/Checkbox/checkbox';
import './vehicleImpound.scss';

export const VehicleImpoundmentReason = (props) => {
    
    return(
        <div className='border-design-form left text-font'>
            <h3>Impoundment for Driving Behaviour</h3>
            <Row>
                <Col className="left checkboxs">
                    <Checkbox name="excessive_speed" >Excessive Speed<span className="light-text"> - commiting an offence under section 148 of the Motor Vehicle Act.</span></Checkbox>
                    <Checkbox name="prohibited" >Prohibited<span className="light-text"> - Driving while prohibited under the Motor Vehicle Act, "Criminal Code, Youth Justice Act or youth Criminal Justice Act (Canada).</span></Checkbox>
                    <Checkbox name="suspended" >Suspended<span className="light-text"> - Driving while suspended under section 89 or section 323 of the Motor Vehicle Act.</span></Checkbox>
                    <Checkbox name="street_racing" >Street Racing<span className="light-text"> - Driving or operating a motor vehicle in a race as defined in the Motor Vehicle Act and the officer inteds to charge with an offence.</span></Checkbox>
                    <Checkbox name="stunt_driving" >Stunt Driving<span className="light-text"> - Driving or operating a motor vehicle in a stunt as defined in the Motor Vehicle Act and the officer inteds to charge with an offence.</span></Checkbox>
                    <Checkbox name="motorcycle_seating" >Motorcycle (seating)<span className="light-text"> - commiting an offence under section 194 (1) or (2) of the Motor Vehicle Act.</span></Checkbox>
                    <Checkbox name="motorcycle_restrictions" disabled>Motorcycle (restrictions)<span className="light-text"> - Commiting an offence under section 25(15) of the Motor Vehicle Act relating to a restriction or condition of a motorcycle learner or novice driver's licence.</span></Checkbox>
                    <Checkbox name="unlicensed" >Unlicenced (UL)<span className="light-text"> - Driving without a valid drivers licence and with a notice on the driving record idicating a previous conviction for driving while unlicensed</span></Checkbox>
                </Col>
            </Row>
        </div>
    )
}

VehicleImpoundmentReason.propTypes = {};