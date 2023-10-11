import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { useFormikContext} from 'formik';
import { Radio } from '../../common/Radio/radio';
import { Input } from '../../common/Input/Input';



export const Unlicensed = (props) => {
    const { values } = useFormikContext();
    return(
        <div className='border-design-form left text-font'>
            <h3 >Unlicensed Driver</h3>
            <Row>
                <Col sm={12}>
                    <Input label="UL Prohibition Number" name="unlicenced_prohibition_number"  className="field-height field-width" type="text" required></Input>
                </Col>
            </Row>
            <Row>
                <Col>
                    <Radio label="Does the officer have grounds to believe that the driver resides in British Columbia? (explain in incident details)" name="belief_driver_bc_resident" options={[
                    { label: 'Yes', value: 'YES' },
                    { label: 'No', value: 'NO' }
                    ]} required />
                </Col>
            </Row>
            <Row>
                <Col>
                    <Radio label="Out-of-Province DL produced" name="out_of_province_dl" options={[
                    { label: 'Yes', value: 'YES' },
                    { label: 'No', value: 'NO' }
                    ]} required />
                </Col>
            </Row>
            {values['out_of_province_dl'] === 'YES' &&
            <Row>
                <Col sm={12}>
                    <Input label="Driver's Licence Number" name="out_of_province_dl_number"  className="field-height field-width" type="text" required></Input>
                </Col>
            </Row>}
        </div>
    )
}

Unlicensed.propTypes = {};