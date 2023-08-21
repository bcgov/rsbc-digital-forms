import { Radio } from '../../common/Radio/radio';
import { Checkbox } from '../../common/Checkbox/checkbox';
import { Input } from '../../common/Input/Input';
import { useFormikContext } from 'formik';
import { DatePickerField } from '../../common/DateField/DatePicker';
import { TimeInputField } from '../../common/Input/TimeInputField';

export const ReasonableGrounds = () => {
    const { values } = useFormikContext();
    return (
        <div className='border-design-form left text-font'>
            <h3 >Reasonable Grounds</h3>
            <div className='row'>
            <div className="col-sm-12">
                <span> The driver was operating a motor vehicle or had care and control of a motor vehicle for the purposes of MVA section 215(1) based on (select at least one): </span>
            </div>
            <div className='col-sm-12 left checkboxs'>
                <Checkbox name="witnessed-by-officer" >Witnessed by Officer</Checkbox>
                <Checkbox name="admission-by-driver" >Admission by Driver</Checkbox>
                <Checkbox name="independent-witness" >Independent witness</Checkbox>
                <Checkbox name="video-surveillance" >Video surveillance</Checkbox>
                <Checkbox name="other-reasonable-ground" >Other</Checkbox>
            </div>
            {values["other-reasonable-ground"] && (<div className='col-sm-12 left other-selected'>
                <Input label="Other" name="other-reason"  className="field-height field-width" type="text"/>
            </div>)}
            </div>
            <div className="row">
                <div className="col">
                    <Radio label="Was a prescribed test used to form reasonable grounds?" name="prescribed-device" options={[
                    { label: 'Yes', value: 'YES' },
                    { label: 'No', value: 'NO' }
                    ]}/>
                </div>
            </div>
            {values["prescribed-device"] === 'YES' && <div className="row">
                <div className='col-sm-6'>
                    <DatePickerField name="date-of-test" label="Date of Test" className="field-height field-width" required/>
                </div>
                <div className='col-sm-6'>
                    <TimeInputField label="Time" className="field-height field-width" name="time-of-test" required/>
                </div>
                </div>}
            {values["prescribed-device"] === 'NO' && <div className="row">
                <div className="col">
                    <Radio label="Why was a prescribed test not used?" name="reason_prescribed_test_not_used" options={[
                    { label: 'Refused by driver', value: 'refused' },
                    { label: 'Opinion formed the driver was affected by alcohol and/or drugs', value: 'opinion' }
                    ]}/>
                </div>
            </div>}
        </div>
    )
}