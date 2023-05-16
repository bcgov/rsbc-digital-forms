import React, { useState, useEffect } from 'react';
import { Formik, Form} from 'formik';
import { Checkbox } from '../common/Checkbox/checkbox';
import { validationSchema } from './validationSchema';
import { Button } from '../common/Button/Button';
import { DriverInfo } from '../CommonForm/driverInfo';
import { InitialValues } from './initialValues';
import { VehicleInfo } from '../CommonForm/vehicleInfo';
import { OfficerInfo } from '../CommonForm/officerInfo';
import { RegisteredOwnerInfo } from '../CommonForm/registeredOwnerInfo';
import { useRecoilValue } from 'recoil';
import { staticResources } from '../../utils/helpers';
import { useNavigate } from 'react-router-dom';
import './createEvent.scss';

export const CreateEvent = () => {
    const vehicleStylesAtom = useRecoilValue(staticResources["vehicle_styles"]);
    const vehicleColoursAtom = useRecoilValue(staticResources["vehicle_colours"]);
    const jurisdictionsAtom = useRecoilValue(staticResources["jurisdictions"]);
    const provincesAtom = useRecoilValue(staticResources["provinces"]);
    const vehiclesAtom= useRecoilValue(staticResources["vehicles"]);
    const [jurisdictions, setJurisdictions] = useState([]);
    const [provinces, setProvinces] = useState([]);
    const [vehicleStyles, setVehicleStyles] = useState([]);
    const [vehicles, setVehicles] = useState([]);
    const [vehicleColours, setVehicleColours] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        setJurisdictions(
            jurisdictionsAtom.map((each) => ({ label: each.objectDsc, value: each.objectCd }))
        );
        setProvinces(
            provincesAtom.map((each) => ({ label: each.objectDsc, value: each.objectCd }))
        );
        setVehicleStyles(
            vehicleStylesAtom.map((each) => ({ label: each.name, value: each.code }))
        );
        setVehicleColours(
            vehicleColoursAtom.map((each) => ({ label: each.display_name, value: each.code }))
        );
        setVehicles(
            vehiclesAtom.map((each) => ({ label: each.search, value: each.search }))
        );
      }, [
        vehicleStylesAtom,
        jurisdictionsAtom,
        provincesAtom,
        vehiclesAtom,
        vehicleColoursAtom
    ]);

    console.log("vehicleColours", vehicleColours);

    const generateYearOptions = () => {
        const currentYear = new Date().getFullYear();
        const startYear = 1991;
        const years = [];
      
        for (let year = startYear; year <= currentYear; year++) {
          years.push({ value: year, label: year.toString() });
        }
      
        return years;
      };

    const onSubmit = (values, { setSubmitting }) => {
        console.log('submit data', values);
        setSubmitting(false);
    };

    const handleGoBack = () => {
        navigate(-1);
      };

    return (
        <div className='text-font'>
            <div className='m-4'>
                <Button onClick={handleGoBack}  primary size='large' label="Save & Return to Main Menu"/>
            </div>
            <div className="outline">
            <Formik initialValues={InitialValues()} validationSchema={validationSchema} onSubmit={onSubmit}>
                {({ isSubmitting }) => (
                    <Form>
                        <div className='row mt-2'>
                            <div className='col-sm-4 left checkboxs'>
                                <h4>Documents to Generate</h4>
                                <Checkbox name="IRP">Immediate Roadside Prohibition</Checkbox>
                                <Checkbox name="VI">Vehicle Impound</Checkbox>
                                <Checkbox name="24Hour">24-hour Driving Prohibition</Checkbox>
                                <Checkbox name="12Hour">12-hour Driving Prohibition</Checkbox>
                            </div>
                            <div className='col-sm-4 form-id-border'>
                                <h5>IRP number: 21-9876540</h5>
                                <h5>VI number: 22-1234560</h5>
                            </div>
                            <div className='col-sm-4 time-of-completion center mt-5'>
                                <span>Estimated time to complete:</span>
                                <h5>12 minutes</h5>
                            </div>
                        </div>
                        <div className='common-fields'>
                            <DriverInfo jurisdictions={jurisdictions} provinces={provinces}/>
                            <VehicleInfo vehicleColours={vehicleColours} years={generateYearOptions()} provinces={provinces} jurisdictions={jurisdictions} vehicles={vehicles} vehicleStyles={vehicleStyles}/>
                            <RegisteredOwnerInfo provinces={provinces}/>
                            <OfficerInfo></OfficerInfo>
                        </div>
                        <div className='right'>
                            <Button primary size='large' label="Next: Preview" type="submit" disabled={isSubmitting}/>
                        </div>
                    </Form>
                )}
            </Formik>
            </div>
        </div>
    );
}