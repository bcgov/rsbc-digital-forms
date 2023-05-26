import { Radio } from '../../common/Radio/radio';
import { Checkbox } from '../../common/Checkbox/checkbox';
import { Input } from '../../common/Input/Input';
import { useFormikContext } from 'formik';

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
        </div>
    )
}