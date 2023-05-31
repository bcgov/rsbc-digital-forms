import { Checkbox } from "../common/Checkbox/checkbox"
import { Input } from "../common/Input/Input"
import Button from 'react-bootstrap/Button';
import { PhoneField } from "../common/Input/phoneField"
import { useEffect } from 'react';
import PropTypes from 'prop-types';
import { SearchableSelect } from "../common/Select/SearchableSelect"
import { useFormikContext } from 'formik';
import "./commonForm.scss"

export const RegisteredOwnerInfo = (props) => {
    const { provinces } = props;
    const { values, setValues } = useFormikContext();
    const ownedByCorp = values['owned-by-corp'];


    useEffect(() => {
        // If user autofill owner info from driver info and then click owned by corp checkbox, this logic will remove autofilled owner info
        if (ownedByCorp && (values['owner-last-name'] !== '' || values['owner-first-name'] !== '')) {
          const updatedValues = {
            ...values,
            'owner-last-name': '',
            'owner-first-name': ''
          };
      
          setValues(updatedValues);
        }
      }, [ownedByCorp, setValues, values]);

    const handlePopulateFields = () => {
        // Get the driver information and populate registered owner fields when prefill button is clicked
        const driverInfo = {
          "owner-last-name": ownedByCorp ?  '' : values['last-name'] ,
          "owner-first-name": ownedByCorp ? '': values['given-name'],
          "registered-owner-address": values['address'],
          "registered-owner-phone": values['phone'],
          "registered-owner-city": values['city'],
          "registered-owner-prov-state":  values['prov-state'],
          "registered-owner-postal":  values['postal-code'],
        };
        setValues({
            ...values,
            ...driverInfo,
          });
        };

    return (
        <div className='registered-owner-info border-design-form left'>
            <div className="row" style={{ minHeight: '40px' }}>
                <div className="col-sm-10"><h3>Registered Owner</h3></div>
                <div className="col-sm-2 right"><Button className="slim-button" variant="primary" onClick={handlePopulateFields}>Fill from driver</Button></div>
            </div>
            <div className="row" style={{ minHeight: '85px' }}>
                <div className="col-sm-12 mt-4">
                    <Checkbox name="owned-by-corp">Owned by Corporate Entity</Checkbox>
                </div>
            </div>
            {ownedByCorp ? (
            <div className="row" style={{ minHeight: '85px' }}>
                <div className="col-sm-12">
                    <Input className='field-height field-width' name="corp-name" label="Corporation Name" />
                </div>
            </div>
            ) : (
            <div className="row" style={{ minHeight: '85px' }}>
                <div className="col-sm-6">
                    <Input className='field-height field-width' name="owner-last-name" label="Owner's Last Name" />
                </div>
                <div className="col-sm-6">
                    <Input className='field-height field-width' name="owner-first-name" label="Owner's First Name" />
                </div>
            </div>
            )}
            <div className="row" style={{ minHeight: '85px' }}>
                <div className=" col-sm-9"><Input label="Address" name="registered-owner-address" className="field-height field-width" type="text"/></div>
                <div className=" col-sm-3"><PhoneField className="field-height field-width" label="Phone number" name="registered-owner-phone" /></div>
            </div>
            <div className="row" style={{ minHeight: '85px' }}>
                <div className=" col-sm-4"><Input label="City" name="registered-owner-city" className="field-height field-width" type="text"/></div>
                <div className=" col-sm-4"><SearchableSelect  className='field-height field-width' label="Province / State"  name="registered-owner-prov-state" options={provinces} /></div>
                <div className=" col-sm-4"><Input className='field-height field-width' label="Postal / Zip"  name="registered-owner-postal"/></div>
            </div>
        </div>
    )
}

RegisteredOwnerInfo.propTypes = {
    provinces: PropTypes.array.isRequired
};