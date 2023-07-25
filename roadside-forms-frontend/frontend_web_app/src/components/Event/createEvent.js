import React, { useState, useEffect } from 'react';
import { Formik, Form } from 'formik';
import Row from 'react-bootstrap/Row';
import { Checkbox } from '../common/Checkbox/checkbox';
import { validationSchema } from './validationSchema';
import Button from 'react-bootstrap/Button';
import { DriverInfo } from '../CommonForm/driverInfo';
import { InitialValues } from './initialValues';
import { VehicleInfo } from '../CommonForm/vehicleInfo';
import { OfficerInfo } from '../CommonForm/officerInfo';
import { TwentyFourHourForm } from '../Forms/TwentyFourHourForm/twentyFourHourForm';
import { RegisteredOwnerInfo } from '../CommonForm/registeredOwnerInfo';
import { useRecoilValue } from 'recoil';
import { staticResources } from '../../utils/helpers';
import { useNavigate } from 'react-router-dom';
import { SVGprint } from '../Forms/Print/svgPrint';
import { formsPNG } from '../../utils/helpers';
import './createEvent.scss';

export const CreateEvent = () => {
    const vehicleStylesAtom = useRecoilValue(staticResources["vehicle_styles"]);
    const vehicleColoursAtom = useRecoilValue(staticResources["vehicle_colours"]);
    const jurisdictionsAtom = useRecoilValue(staticResources["jurisdictions"]);
    const provincesAtom = useRecoilValue(staticResources["provinces"]);
    const cityAtom = useRecoilValue(staticResources["cities"]);
    const vehiclesAtom= useRecoilValue(staticResources["vehicles"]);
    const impoundAtom= useRecoilValue(staticResources["impound_lot_operators"]);
    const [jurisdictions, setJurisdictions] = useState([]);
    const [provinces, setProvinces] = useState([]);
    const [vehicleStyles, setVehicleStyles] = useState([]);
    const [vehicles, setVehicles] = useState([]);
    const [vehicleColours, setVehicleColours] = useState([]);
    const [cities, setCities] = useState([]);
    const [impoundLotOperators, setImpoundLotOperators] = useState([]);
    const [currentStep, setCurrentStep] = useState(0);

    const navigate = useNavigate();

    useEffect(() => {
        setJurisdictions(
            jurisdictionsAtom.map((each) => ({ label: each.objectDsc, value: each.objectCd }))
        );
        setImpoundLotOperators(
            impoundAtom.map((each) => ({
                label: each.name + ', ' +each.lot_address+', '+each.city+', '+each.phone,
                value: each.name + ', ' +each.lot_address+', '+each.city+', '+each.phone }))
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
        setCities(
            cityAtom.map((each) => ({ label: each.objectDsc, value: each.objectCd }))
        );
      }, [
        vehicleStylesAtom,
        jurisdictionsAtom,
        provincesAtom,
        vehiclesAtom,
        vehicleColoursAtom,
        cityAtom,
        impoundAtom
    ]);

    const generateYearOptions = () => {
        const currentYear = new Date().getFullYear();
        const startYear = 1900;
        const years = [];
      
        for (let year = startYear; year <= currentYear; year++) {
          years.push({ value: year, label: year.toString() });
        }
      
        return years;
      };

    const onSubmit = (values, { setSubmitting }) => {
        setSubmitting(false);
    };

    const printForms = () => window.print()
    

    const handleGoBack = () => {
        navigate('/');
      };

      const nextPage = () => {
        setCurrentStep(currentStep + 1);
      };

      const prevPage = () => {
        setCurrentStep(currentStep - 1);
      };

      const renderSVGForm = (values) => {
        const forms = {"TwentyFourHour": values["24Hour"], "TwelveHour": values["12Hour"], "IRP": values["IRP"], "VI": values["VI"] }
        const componentsToRender = []
        for(const item in forms){
            if (forms[item]) {
                for (const form in formsPNG[item]) {
                    if (form === "ILO" && !forms["VI"]){ 
                        break
                    }
                    componentsToRender.push(<SVGprint key={item+form} form={formsPNG[item][form]["png"]} formAspect={formsPNG[item][form]["aspectClass"]} formType={form} values={values}/>)
                }
            }
        }
        return componentsToRender
      }

      const renderPage = (currentStep, values) => {
        switch (currentStep) {
          case 0:
            return (
            <>
            <div className='row mt-2'>
            <div className='col-sm-4 left checkboxs'>
                <h4>Documents to Generate</h4>
                <Checkbox name="IRP" >Immediate Roadside Prohibition</Checkbox>
                <Checkbox name="VI" >Vehicle Impound</Checkbox>
                <Checkbox name="24Hour" >24-hour Driving Prohibition</Checkbox>
                <Checkbox name="12Hour" >12-hour Driving Prohibition</Checkbox>
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
        </div>
        { values['24Hour'] &&  <TwentyFourHourForm cities={cities} impoundLotOperators={impoundLotOperators}/> }
        <OfficerInfo/>
        </>
                
            );
          case 1:
            return(
                <div>
                    {renderSVGForm(values)}
                </div> 
            )
          // Add more cases for each page
          default:
            return null;
        }
      };

    return (
        <div id='event-container' className='text-font'>
            <div id='button-container' className='m-4'>
                <Button  variant="primary" onClick={handleGoBack}>Save & Return to Main Menu</Button>
            </div>
            <div className="outline">
            <Formik 
                initialValues={InitialValues()} 
                validationSchema={validationSchema} 
                onSubmit={onSubmit}>
                {({ isSubmitting, values }) => (
                    <Form>
                        {renderPage(currentStep, values)}
                        <div id='button-container' className="flex">  
                        {currentStep > 0 && (
                            <div className='left'>
                                <Button type="button" onClick={() => prevPage()}>
                                    Previous
                                </Button>
                            </div>
                        )}
                        <div className='right'>
                            {currentStep <  4 ?
                                (currentStep === 1 ? 
                                    <Button type="button" onClick={() => printForms()}>
                                        Print
                                    </Button>
                                    : (    
                                <Button type="button" onClick={() => nextPage()}>
                                    Next
                                </Button>
                            )) : (
                                <Button variant="primary" type="submit">Submit</Button>   
                            )}
                        </div>
                        </div>
                    </Form>
                )}
            </Formik>
            </div>
        </div>
    );
}