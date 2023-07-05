import { NumericInput } from "../../common/Input/NumericInput";
import { useFormikContext } from 'formik';
import { Checkbox } from "../../common/Checkbox/checkbox";
import { Radio } from "../../common/Radio/radio"
import { DatePickerField } from '../../common/DateField/DatePicker';
export const TestAdministered = (props) => {
    const { values } = useFormikContext();
    return(
        <>{values["prescribed-device"] === 'YES' && (<div className='border-design-form left text-font'>
            <h3 >Test Administered - {values["type-of-prohibition"] === "alcohol" ? 'Alcohol 215(2)' : 'Drugs 215(3)'}</h3>
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
            </div>
         )} </>
    )
}