import React, { useState } from 'react';
import { Radio } from '../../../common/Radio/radio';
import { useFormikContext } from 'formik';
import { Input } from '../../../common/Input/Input';
import { DatePickerField } from '../../../common/DateField/DatePicker';
import { TimeInputField } from '../../../common/Input/TimeInputField';
import { PhoneField } from '../../../common/Input/phoneField';
import { SearchableSelect } from '../../../common/Select/SearchableSelect';
import PropTypes from 'prop-types';

export const VehicleImpoundment = (props) => {
    const {impoundLotOperators} = props;
    const { values, setFieldValue  } = useFormikContext();
 
    const handleILOChange = (selectedOption) => {
      if (selectedOption) {
        const [name, address, city, phone] = selectedOption.value.split(', ');
        console.log(name,address)
        setFieldValue('ILO-name', name);
        setFieldValue('ILO-address', address);
        setFieldValue('ILO-city', city);
        setFieldValue('ILO-phone', phone);
      } else {
        setFieldValue('ILO-name', '');
        setFieldValue('ILO-address', '');
        setFieldValue('ILO-city', '');
        setFieldValue('ILO-phone', '');
      }
    };

    const reasonForNotImpounding = [
      {label:"Released to other driver",value:"released"},
      {label:"Left at roadside",value:"roadside"},
      {label:"Private tow",value:"private"},
      {label:"Seized for investigation",value:"investigation"}
  ]
    return(
        <div className='border-design-form left text-font'>
            <h3 >Vehicle Impoundment or Dispostion</h3>
            <div className="row">
                <div className="col">
                    <Radio label="Vehicle Impounded?" name="vehicle-impounded" options={[
                    { label: 'Yes', value: 'YES' },
                    { label: 'No', value: 'NO' }
                    ]} required />
                </div>
            </div>
        {values['vehicle-impounded'] === 'YES' && (<>
            <div className="row">
                <div className="col">
                    <Radio label="Location of Keys?" name="key-location" options={[
                        {value:"WITH VEHICLE", label:"With vehicle"},
                        {value:"WITH DRIVER", label:"With driver"}
                    ]} required/>
                </div>
                </div>
            <div className='impound-lot-operator'>
                <div className='row'>
                <div className="col-sm-12">
                    <SearchableSelect  onChange={handleILOChange} className='field-height field-width' label="Search for Impound Lot Operator"  name="ILO-options" options={impoundLotOperators}/>
                </div>
                </div>
                <div className='impoud-lot-fields' style={{backgroundColor: "lightgray"}}>
                    <div className='row'>
                        <div className='col-sm-12'>
                            <Input value={values['ILO-name']} label="Impound Lot Operator Name" name="ILO-name"  className="field-height field-width" type="text" required></Input>
                        </div>
                    </div>
                    <div className='row'>
                        <div className='col-sm-4'>
                            <Input value={values['ILO-address']} label="Public Lot Address" name="ILO-address"  className="field-height field-width" type="text" required></Input>
                        </div>
                        <div className='col-sm-4'>
                            <Input value={values['ILO-city']} label="City" name="ILO-city"  className="field-height field-width" type="text" required></Input>
                        </div>
                        <div className='col-sm-4'>
                            <PhoneField value={values['ILO-phone']} className="field-height field-width" label="Public Phone Number" name="ILO-phone" required></PhoneField>
                        </div>
                    </div>
                </div>
            </div>
        </>)}
        {values['vehicle-impounded'] === 'NO' && (
        <>
            <div className="row" style={{ minHeight: '85px' }}>
                <div className="col">
                    <Radio label="Reason for not impounding?" name="reason-for-not-impounding" options={reasonForNotImpounding} required/>
                </div>
            </div>
            {values['reason-for-not-impounding'] === 'released' && (
                <div className='row' style={{ minHeight: '85px' }}>
                    <div className='col-sm-4'>
                        <Input label="Vehicle Released To" name="vehicle-released-to"  className="field-height field-width" type="text" required></Input>
                    </div>
                    <div className='col-sm-4'>
                        <DatePickerField name="date-released" label="Date Released" className="field-height field-width" required/>
                    </div>
                    <div className='col-sm-4'>
                        <TimeInputField label="Time" className="field-height field-width" name="time-released" required/>
                    </div>
                </div>
            )}
        </>)}
    </div>
    )
}

VehicleImpoundment.propTypes = {
    impoundLotOperators: PropTypes.array.isRequired
};