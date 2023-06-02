import "./commonForm.scss"
import PropTypes from 'prop-types';
import React, { useState, useEffect} from 'react';
import { Input } from "../common/Input/Input"
import { SearchableSelect } from "../common/Select/SearchableSelect"
import { useFormikContext } from 'formik';
import { Button } from "../common/Button/Button"
import { MultiSelectField } from "../common/Select/MultiSelectField";

export const VehicleInfo = (props) => {
    const {vehicles, years, vehicleStyles, vehicleColours, jurisdictions, provinces} = props;
    const { values} = useFormikContext();
    const [disableBtn, setdisableBtn] = useState(true);
    const driversLicenceJurisdiction = values['vehicle-jurisdiction'];

    useEffect(() => {
        if (driversLicenceJurisdiction === 'BC'){
            setdisableBtn(false);
        } else{
            setdisableBtn(true)
        }
    }, [driversLicenceJurisdiction])
    return (
        <div className='vehicle-info border-design-form left'>
            <h3 >Vehicle Information</h3>
            <div>
                <div className="row" style={{ minHeight: '85px' }}>
                    <div className="col-sm-5" ><SearchableSelect  className='field-height field-width' label="Jurisdiction"  name="vehicle-jurisdiction" options={jurisdictions} /></div>
                    <div className=" col-sm-5"><Input className='field-height field-width' label="Plate Number" name="plate-number" type="text"/></div>
                    <div className=" col-sm-2 mt-4"><Button primary size='medium' label="ICBC Prefill" disabled={disableBtn}/></div>
                </div>
                <div className="row" style={{ minHeight: '85px' }}>
                    <div className=" col-sm-5"><Input label="Registration Number" name="registration-number" className="field-height field-width" type="text"/></div>
                </div>
                <div className="row" style={{ minHeight: '85px' }}>
                    <div className=" col-sm-3"><SearchableSelect  className='field-height field-width' label="Vehicle Year"  name="vehicle-year" options={years} /></div>
                    <div className=" col-sm-3"><SearchableSelect  className='field-height field-width' label="Vehicle Make and Model"  name="vehicle-make-model" options={vehicles} /></div>
                    <div className=" col-sm-3"><SearchableSelect  className='field-height field-width' label="Vehicle Style"  name="vehicle-style" options={vehicleStyles} /></div>
                    <div className=" col-sm-3"><MultiSelectField  className='field-width' label="Vehicle Colour(s)"  name="vehicle-colour" options={vehicleColours} /></div>
                    </div>
                    <div className="row" style={{ minHeight: '85px' }}>
                        <div className=" col-sm-5"><Input label="VIN Number" name="vin-number" className="field-height field-width" type="text"/></div>
                        <div className=" col-sm-3"><SearchableSelect  className='field-height field-width' label="NSC Prov / State"  name="nsc-prov-state" options={provinces} /></div>
                        <div className=" col-sm-4"><Input label="NSC Number" name="nsc-number" className="field-height field-width" type="text"/></div>
                    </div>
            </div>
        </div>
    )
}

VehicleInfo.propTypes = {
    vehicles: PropTypes.array.isRequired,
    vehicleStyles: PropTypes.array.isRequired,
    vehicleColours: PropTypes.array.isRequired,
    jurisdictions: PropTypes.array.isRequired,
    provinces: PropTypes.array.isRequired,
    years: PropTypes.array.isRequired,
};