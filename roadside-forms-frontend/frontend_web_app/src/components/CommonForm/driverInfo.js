import { Input } from "../common/Input/Input"
import React, { useState, useEffect} from 'react';
import { SearchableSelect } from "../common/Select/SearchableSelect"
import PropTypes from 'prop-types';
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { DateOfBirthField } from "../common/DateField/dateOfBirthField"
import {DatePickerField} from "../common/DateField/DatePicker"
import { PhoneField } from "../common/Input/phoneField";
import { useFormikContext } from 'formik';
import "./commonForm.scss"

export const DriverInfo = (props) => {
    const {jurisdictions, provinces} = props;
    const { values } = useFormikContext();
    const [disableBtn, setdisableBtn] = useState(true);
    const driversLicenceJurisdiction = values['drivers_licence_jurisdiction'];

    useEffect(() => {
        if (driversLicenceJurisdiction && driversLicenceJurisdiction.value === 'BC'){
            setdisableBtn(false);
        } else{
            setdisableBtn(true)
        }
    }, [driversLicenceJurisdiction])
    
    return (
            <div className='driver-info border-design-form left'>
                <h3 >Driver's Information</h3>
                <div>
                    <Row style={{ minHeight: '85px' }}>
                        <Col sm={4}><Input className='field-height field-width' label="Driver's Licence Number" name="driver_licence_no" type="text"/></Col>
                        <Col sm={1} className="mt-4 pr-2"><Button className="slim-button" variant="primary" disabled={disableBtn}>ICBC Prefill</Button></Col>
                        <Col sm={1} className="mt-4 left" ><Button className="slim-button" variant="primary" disabled={disableBtn}>Scan DL</Button></Col>
                        <Col sm={6} ><SearchableSelect  className='field-height field-width' label="Province / State/ International"  name="drivers_licence_jurisdiction" options={jurisdictions} /></Col>
                    </Row>
                    <Row style={{ minHeight: '85px' }}>
                        <Col sm={4}><Input label="Last Name" name="driver_last_name"  className="field-height field-width" type="text" required/></Col>
                        <Col sm={4}><Input label="Given Name" name="driver_given_name" className="field-height field-width" type="text"/></Col>
                        <Col sm={4}><DateOfBirthField className="field-height field-width" label="Date Of Birth" name="driver_dob"/></Col>
                    </Row>
                    <Row style={{ minHeight: '85px' }}>
                        <Col sm={9}><Input label="Address" name="driver_address" className="field-height field-width" type="text" required/></Col>
                        <Col sm={3}><PhoneField className="field-height field-width" label="Phone number" name="driver_phone" /></Col>
                    </Row>
                    <Row  style={{ minHeight: '85px' }}>
                        <Col sm={4}><Input label="City" name="driver_city" className="field-height field-width" type="text" required/></Col>
                        <Col sm={4}><SearchableSelect  className='field-height field-width' label="Province / State"  name="driver_prov_state" options={provinces} required/></Col>
                        <Col sm={4}><Input className='field-height field-width' label="Postal / Zip"  name="driver_postal"/></Col>
                    </Row>
                    {values['VI'] && (
                        <Row  style={{ minHeight: '85px' }}>
                        <Col sm={4}><Input label="Gender" name="gender" className="field-height field-width" type="text" /></Col>
                        <Col sm={4}><DatePickerField className='field-height field-width' label="Licence Expiry Date"  name="driver_licence_expiry" /></Col>
                        <Col sm={4}><Input className='field-height field-width' label="BCDL Class"  name="driver_licence_class"/></Col>
                    </Row>
                    )}
                </div>
            </div>
    )
}
DriverInfo.propTypes = {
    jurisdictions: PropTypes.array.isRequired,
    provinces: PropTypes.array.isRequired
};