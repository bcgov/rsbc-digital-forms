import { Radio } from "../../common/Radio/radio"
import { Input } from "../../common/Input/Input"
import { SearchableSelect } from "../../common/Select/SearchableSelect"
import { DatePickerField } from '../../common/DateField/DatePicker';
import { TimeInputField } from '../../common/Input/TimeInputField';
import { TestAdministered } from "./testAdministered";
import PropTypes from 'prop-types';

export const Prohibition = (props) => {
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