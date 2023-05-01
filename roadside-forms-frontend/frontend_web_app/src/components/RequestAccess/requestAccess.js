import React, { useState } from 'react';
import { Button } from '../common/Button/Button';
import { Formik, Form} from 'formik';
import { validate } from './validate';
import WarningIcon from '@mui/icons-material/Warning';
import { Input }from '../common/Input/Input'
import { Select } from '../common/Select/Select';
import { UserApi } from '../../api/userApi';
import { staticResources } from '../../utils/helpers';
import { useSetRecoilState, useRecoilValue, atom } from 'recoil';
import { StaticDataApi } from '../../api/staticDataApi';

export const RequestAccess= () => {
  const [showApplication, setShowApplication] = useState(false)
  const [showApplicationReceived, setShowApplicationReceived] = useState(false)
  const setResource = useSetRecoilState(staticResources["agencies"]);
  const atomResource = useRecoilValue(staticResources["agencies"])

  const initialValues = {
    last_name: '',
    first_name: '',
    agency:'',
    badge_number:''
  };

  const options = [
    { value: 'Option 1', label: 'Option 1' },
    { value: 'Option 2', label: 'Option 2' },
    { value: 'Option 3', label: 'Option 3' },
  ];

 
  const onSubmit = (values, { setSubmitting }) => {
    const data = values;
    UserApi.post(data)
      .then((data) => {
        console.log("Success", data);
        setSubmitting(false);
        setShowApplication(false);
        setShowApplicationReceived(true);
      })
      .catch((error) => {
        console.log("Error", error);
      })
  };

  const handleClick = () => {
    setShowApplication(true);
    setResource(StaticDataApi.get("agencies")).then( () => {
      console.log(atomResource)
    })
  }

  return (
    <div className='border-design text-font'>
      {!showApplicationReceived && (<div>
        <p>
          <span className="fw-bold">Welcome to the Digital Forms system</span>
        </p>
        <p>
          <em>WARNING: This system is for use by authorized law enforcement officers only.</em>
        </p>
        <p>
          You currently do not have access to the Digital Forms system.
        </p>
        <p>
          Please apply for access after completing the training course and with the approval of your unit commander.
        </p>
      </div>)}
      {!showApplication && !showApplicationReceived && <Button primary size="large" label="Apply for Access" onClick={handleClick}/>}
      {showApplication && ( <div>
        <div className=' d-flex justify-content-center mt-2'>
          <Formik initialValues={initialValues} validate={validate} onSubmit={onSubmit}>
          {({ isSubmitting }) => (
            <Form>
              <div className='row'>
                <div className='col-sm-3'>
                  <Input label="SURNAME" name="last_name" className="field-width" type="text"></Input>
                </div>
                <div className='col-sm-3'>
                  <Input label="Given" name="first_name" className="field-width" type="text"></Input>
                </div>
                <div className='col-sm-4'>
                  <Select label="Agency or RCMP Detachment" className="field-width" name="agency" options={options} />
                </div>
                <div className='col-sm-2'>
                  <Input label="PRIME ID" name="badge_number" className="field-width" type="text" maxLength={6} ></Input>
                </div>
              </div>
              <div className="info-container">
                <div className="row">
                  <div className="col" />
                  <div className="col-9 left-align" style={{textAlign: 'center'}}>
                    <p>
                      <WarningIcon className="text-warning" /> <span className="fw-bold">PRIME ID</span> is the username you use to log into the MDT (CAD) and the MRE.<br />
                    </p>
                    <ul className='ml-10'style={{ listStylePosition: 'inside', textAlign: 'center'}}>
                        <li >For independents, this is your agency's two-letter abbreviation followed by 2 to 4 numbers.</li><br />
                        <li >For RCMP members, this will be your 6 digit HRMIS.</li>
                    </ul>
                  </div>
                  <div className="col" />
                </div>
              </div>
              <Button primary size='large' label="Apply for Access" type="submit" disabled={isSubmitting}/>
            </Form>
          )}
          </Formik>
        </div>
      </div>)}
      {showApplicationReceived && (<div>
        <p>
          <span class="fw-bold">Application received.</span> Thank-you!
        </p>
        <p>
          Your application will be reviewed and approved within 24 business hours.
        </p>
      </div>)}
    </div>
  );
}
