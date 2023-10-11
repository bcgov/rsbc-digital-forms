import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { useFormikContext} from 'formik';
import PropTypes from 'prop-types';
import { Radio } from '../../common/Radio/radio';
import { Input } from '../../common/Input/Input';



export const VehicleImpoundmentIRP = (props) => {
    const { values } = useFormikContext();

    return(
        <div className='border-design-form left text-font'>
            <h3 >Impoundment for Immediate Roadside Prohibition</h3>
            
            <Row>
                <Col>
                    <Radio label="was an IRP issued as a part of this vehicular impound?" name="irp_impound" options={[
                    { label: 'Yes', value: 'YES' },
                    { label: 'No', value: 'NO' }
                    ]} required />
                </Col>
            </Row>
            
        {values['irp_impound'] === 'YES' &&
        <>
            <Row>
                <Col>
                    <Radio label="was an IRP issued as a part of this vehicular impound?" name="irp_impound_duration" options={[
                    { label: '3-day Vehicle Impoundment(Optional for 3-Day IRPs', value: '3DAY' },
                    { label: '7-day Vehicle Impoundment(Optional for 7-Day IRPs', value: '7DAY' },
                    { label: '30-day Vehicle Impoundment(MANDATORY for 30-Day and 90-Day IRPs', value: '30DAY' }
                    ]} required />
                </Col>
            </Row>
            <Row>
                <Col sm={6}>
                    <Input label="IRP Number" name="IRP_number"  className="field-height field-width" type="text" required></Input>
                </Col>
                <Col sm={6}>
                    <Input label="This VI Number" name="VI_number"  className="field-height field-width" type="text" required></Input>
                </Col>
            </Row>
        </>
        }
    </div>
    )
}

VehicleImpoundmentIRP.propTypes = {};