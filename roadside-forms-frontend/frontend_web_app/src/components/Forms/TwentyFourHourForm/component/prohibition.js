import { Radio } from "../../../common/Radio/radio"
import { Input } from "../../../common/Input/Input"
import { SearchableSelect } from "../../../common/Select/SearchableSelect"
import { DatePickerField } from '../../../common/DateField/DatePicker';
import { TimeInputField } from '../../../common/Input/TimeInputField';
import { NumericInput } from "../../../common/Input/NumericInput";
import { useFormikContext } from 'formik';
import { Checkbox } from "../../../common/Checkbox/checkbox";
import PropTypes from 'prop-types';

export const Prohibition = (props) => {
    const { values } = useFormikContext();
    const {cities} = props;
    return (
        <div className='border-design-form left text-font'>
            <h3 >Prohibition</h3>
            <div className="row">
                <div className="col">
                    <Radio label= "Type of Prohibition (select one)" name="type-of-prohibition" options={[
                    { label: 'Alcohol 215(2)', value: 'alcohol' },
                    { label: 'Drugs 215(3)', value: 'drugs' }
                    ]} required />
                </div>
            </div>
            {values["type-of-prohibition"] === "alcohol" && (
            <div className="test-admin-alcohol">
                <div className="row">
                    <div className="col">
                        <Radio label= "Which test was used?" name="test-used-alcohol" options={[
                            { label: 'Alco-Sensor FST(ASD)', value: 'alco-sensor' },
                            { label: 'Approved Instrument', value: 'instrument' },
                            { label: 'Prescribed Physical Coordination Test (SFST)', value: 'physical-cordination-test' }
                            ]} required />
                    </div>
                </div> 
                {(values["test-used-alcohol"] === "alco-sensor" || values["test-used-alcohol"] ==="instrument") &&<div className="row">
                     <div className="col-sm-12">
                        {values["test-used-alcohol"] === "alco-sensor" &&
                            <DatePickerField name="ASD-expiry-date" label="ASD Expiry Date" className="field-height field-width" required/>}
                        {values["test-used-alcohol"] === "instrument" && 
                            <Radio label= "Result" name="alcohol-test-result" options={[
                                { label: '51-99 mg%', value: '51-99 mg%' },
                                { label: 'Over 99 mg%', value: 'Over 99 mg%' },
                                ]} required />}
                    </div>
                </div>}
                <div className="row">
                    <div className="col-sm-12 mt-2">
                        <NumericInput label="BAC Result(mg%)" name="BAC-result" required/>
                    </div>
                </div>
            </div>)}
            {values["type-of-prohibition"] === "drugs" && (
            <div className="test-admin-drug">
                <div className="row">
                    <div className="col-sm-12">
                        <Radio label= "Which test was used?" name="test-used-drug" options={[
                            { label: 'Alco-Sensor FST(ASD)', value: 'alco-sensor' },
                            { label: 'Approved Instrument', value: 'instrument' },
                            { label: 'Prescribed Physical Coordination Test (SFST)', value: 'physical-cordination-test' }
                            ]} required />
                    </div>
                </div>
                <div className="row">
                    <div className="col-sm-12">
                    <span> Test Result </span>
                </div>
                    <div className="col-sm-12">
                        <Checkbox name="THC" >THC</Checkbox>
                        <Checkbox name="Cocaine" >Cocaine</Checkbox>
                    </div>
                </div>
            </div>)}
            <div className="row">
                <div className="col-sm-8">
                    <Input label="Intersection or Address of Offence" name="offence-address"  className="field-height field-width" type="text" required></Input>
                </div>
                <div className="col-sm-4">
                    <SearchableSelect  className='field-height field-width' label="City"  name="offence-city" options={cities} required/>
                </div>
            </div>
            <div className="row">
                <div className="col-sm-2">
                    <Input label="Agency File #" name="offence-agency-file"  className="field-height field-width" type="text" required></Input>
                </div>
                <div className='col-sm-5'>
                    <DatePickerField name="date-of-driving" label="Date of Driving - care or control" className="field-height field-width" required/>
                </div>
                <div className='col-sm-5'>
                    <TimeInputField label="Time of Driving - care or control" className="field-height field-width" name="time-of-driving" required/>
                </div>
            </div>
        </div>
    )
}

Prohibition.propTypes = {
    cities: PropTypes.array.isRequired
};