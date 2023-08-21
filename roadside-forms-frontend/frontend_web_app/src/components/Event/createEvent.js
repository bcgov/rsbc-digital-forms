import React, { useState, useEffect } from 'react';
import { Formik, Form } from 'formik';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal'
import { Checkbox } from '../common/Checkbox/checkbox';
import { validationSchema } from './validationSchema';
import { DriverInfo } from '../CommonForm/driverInfo';
import { InitialValues } from './initialValues';
import { VehicleInfo } from '../CommonForm/vehicleInfo';
import { OfficerInfo } from '../CommonForm/officerInfo';
import { TwentyFourHourForm } from '../Forms/TwentyFourHourForm/twentyFourHourForm';
import { RegisteredOwnerInfo } from '../CommonForm/registeredOwnerInfo';
import { useRecoilValue } from 'recoil';
import { useNavigate } from 'react-router-dom';
import { ConfirmationStep } from './ConfirmationStep/confirmationStep';
import { PoliceDetails } from '../Forms/TwentyFourHourForm/policeDetails';
import { staticResources, getEventDataToSave, formsPNG } from '../../utils/helpers';
import {SVGprint} from '../Forms/Print/svgPrint'
import {db} from '../../db'
import './createEvent.scss';

export const CreateEvent = () => {
    const vehicleStylesAtom = useRecoilValue(staticResources["vehicle_styles"]);
    const vehicleColoursAtom = useRecoilValue(staticResources["vehicle_colours"]);
    const jurisdictionsAtom = useRecoilValue(staticResources["jurisdictions"]);
    const provincesAtom = useRecoilValue(staticResources["provinces"]);
    const cityAtom = useRecoilValue(staticResources["cities"]);
    const vehiclesAtom= useRecoilValue(staticResources["vehicles"]);
    const impoundAtom= useRecoilValue(staticResources["impound_lot_operators"]);
    const [formValues, setFormValues] = useState([]);
    const [jurisdictions, setJurisdictions] = useState([]);
    const [provinces, setProvinces] = useState([]);
    const [vehicleStyles, setVehicleStyles] = useState([]);
    const [vehicles, setVehicles] = useState([]);
    const [vehicleColours, setVehicleColours] = useState([]);
    const [cities, setCities] = useState([]);
    const [impoundLotOperators, setImpoundLotOperators] = useState([]);
    const [currentStep, setCurrentStep] = useState(0);
    const [show, setShow] = useState(false);
    const [modalTitle, setModalTitle] = useState('');
    const [modalBody, setModalBody] = useState('');
    const [modalButtonText, setModalButtonText] = useState('');
    const [isPrinted, setIsPrinted] = useState(false);
    const [modalCloseFunc, setmodalCloseFunc] = useState(() => () => null);

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

    const handleClose = async () => {
        setShow(false) 
        modalCloseFunc()
        setmodalCloseFunc(() => () => null)
        setModalBody('')
        setModalTitle('')
        setModalButtonText('')
    }

    const handleModalClose = async () => {
        setShow(false)
        setmodalCloseFunc(() => () => null)
        setModalBody('')
        setModalTitle('')
        setModalButtonText('')
    }

    const handleShow = (title, body, buttonText, func) => {
        setModalTitle(title);
        setModalBody(body);
        setModalButtonText(buttonText);
        setmodalCloseFunc(() => func)
        setShow(true);
    }

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

    const handlePrintForms = async () => {
        setIsPrinted(true);
        window.print();
        nextPage()
    }

    const printForms = async () => {
        handleShow('Print Form', 'If you print this form you cannot go back and edit it, please confirm you wish to proceed.', 'Print', () => handlePrintForms() )   
    }

    const handleGoBackandSave = (values) => {
        const eventData = getEventDataToSave(values);
        if(eventData["event_id"]===undefined){
            // need a beter solution to this
            eventData["event_id"] = 1
        }
        db.event.put(eventData)
        navigate('/');
    }

    const handleWithdraw = () => {
        navigate('/');
    };

    const nextPage = () => {
        setCurrentStep(currentStep + 1);
      };

    const prevPage = () => {
        setCurrentStep(currentStep - 1);
      };

    const withdrawProhibition = () => {
        handleShow('Confirm Withdraw Prohibition', 'Are you sure you want to withdraw this prohibition.', 'Withdraw', () => handleWithdraw() )   
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
                <Checkbox name="IRP" disabled={values['24Hour'] || values['12Hour']} >Immediate Roadside Prohibition</Checkbox>
                <Checkbox name="VI" >Vehicle Impound</Checkbox>
                <Checkbox name="24Hour" disabled={values['IRP'] || values['12Hour']} >24-hour Driving Prohibition</Checkbox>
                <Checkbox name="12Hour" disabled={values['24Hour'] || values['IRP']} >12-hour Driving Prohibition</Checkbox>
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
          case 2:
            return(
                <ConfirmationStep/>
            )
          case 3:
            return(
                values['prescribed-device'] === 'NO' ? <PoliceDetails/> : null
            )
          // Add more cases for each page
          default:
            return null;
        }
      };

    return (
        <div id='event-container' className='text-font'>
            <div id='button-container' className='m-4'>
                <Button  variant="primary" onClick={() => handleGoBackandSave(formValues)}>Save & Return to Main Menu</Button>
            </div>
            <div className="outline">
            <Formik 
                innerRef={(formikActions) => (formikActions? setFormValues(formikActions.values) : setFormValues({}))}
                initialValues={InitialValues()} 
                validationSchema={validationSchema} 
                onSubmit={onSubmit}>
                {({ isSubmitting, values }) => (
                    <Form>
                        <Modal id="popconfirm-modal" show={show} onHide={handleModalClose}>
                            <Modal.Header closeButton>
                            <Modal.Title>{modalTitle}</Modal.Title>
                            </Modal.Header>
                            <Modal.Body>{modalBody}</Modal.Body>
                            <Modal.Footer>
                            <Button variant="secondary" onClick={handleModalClose}>
                                Close
                            </Button>
                            <Button variant="primary" onClick={handleClose}>
                                {modalButtonText}
                            </Button>
                            </Modal.Footer>
                        </Modal>
                        {renderPage(currentStep, values)}
                        <div id='button-container' className="flex">  
                        {((currentStep > 0 && !isPrinted) || values['prescribed-device'] === 'YES') && (
                            <div className='left'>
                                <Button type="button" onClick={() => prevPage()}>
                                    Previous
                                </Button>
                            </div>
                        )}
                        {(currentStep === 3 && values['prescribed-device'] === 'NO') && (
                            <div className='left'>
                                <Button type="button" onClick={() => withdrawProhibition()}>
                                    Withdraw Prohibition
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