import React, { useEffect } from 'react';
import EditIcon from '@mui/icons-material/Edit';
import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import AddIcon from '@mui/icons-material/Add';
import Table from 'react-bootstrap/Table';
import { useSetRecoilState} from 'recoil';

import { staticResources } from '../../utils/helpers';
import { StaticDataApi } from '../../api/staticDataApi';
import { Button } from '../common/Button/Button';
import './dashboard.scss'

export const Dashboard = () => {
  const setAgencyResource = useSetRecoilState(staticResources["agencies"]);
  const setCityResource = useSetRecoilState(staticResources["cities"]);
  const setCountryResource = useSetRecoilState(staticResources["countries"]);
  const setJurisdictionResource = useSetRecoilState(staticResources["jurisdictions"]);
  const setImpoundResource = useSetRecoilState(staticResources["impound_lot_operators"]);
  const setProvinceResource = useSetRecoilState(staticResources["provinces"]);
  const setVehicleStyleResource = useSetRecoilState(staticResources["vehicle_styles"]);
  const setVehicleResource = useSetRecoilState(staticResources["vehicles"]);

  useEffect(() => {
    const agencyData = StaticDataApi.get("agencies").data
    const cityData = StaticDataApi.get("cities").data
    const contryData = StaticDataApi.get("countries").data
    const jurisdictionData = StaticDataApi.get("jurisdictions").data
    const impoundData = StaticDataApi.get("impound_lot_operators").data
    const provinceData = StaticDataApi.get("provinces").data
    const vehicleStyleData = StaticDataApi.get("vehicle_styles").data
    const vehicleData = StaticDataApi.get("vehicles").data
    
    setVehicleResource(vehicleData)
    setVehicleStyleResource(vehicleStyleData)
    setProvinceResource(provinceData)
    setImpoundResource(impoundData)
    setJurisdictionResource(jurisdictionData)
    setCountryResource(contryData)
    setCityResource(cityData)
    setAgencyResource(agencyData)
  }, [setVehicleResource,setVehicleStyleResource,setProvinceResource,setImpoundResource,setJurisdictionResource,setCountryResource,setCityResource,setAgencyResource,]);

      return (
      <>
      <div className='border-design text-font'>
        <div className='dashboard-header'>
          <h3><EditIcon/>Events in Progress</h3>
          <Button primary size="large" onClick={() => {}} label="New Event" icon={<AddIcon/>} />
        </div>
        <hr className='hr' />
        <Table>
          <thead>
            <tr>
              <th>Date & Time</th>
              <th>Form Types</th>
              <th>Location</th>
              <th>Surname</th>
              <th>Plate #</th>
              <th>Next Step</th>
            </tr>
          </thead>
        </Table>
      </div>
      <div className='border-design text-font'>
        <div className='dashboard-header'>
          <h3><ErrorOutlineIcon/>Waiting for Transmission to Server</h3>
          <span>Automatically re-trying in x seconds</span>
        </div>
        <hr className='hr' />
        <Table>
          <thead>
            <tr>
              <th>Date & Time</th>
              <th>Form #</th>
              <th>Form Type</th>
              <th>Location</th>
              <th>Surname</th>
              <th>Plate #</th>
            </tr>
          </thead>
        </Table>
        </div>
        <div className='border-design text-font'>
        <div className='dashboard-header'>
          <h3><CheckCircleOutlineIcon/>Completed</h3>
          <span>Last updated on date</span>
        </div>
        <hr className='hr' />
        <Table>
          <thead>
            <tr>
              <th>Date & Time</th>
              <th>Form #</th>
              <th>Form Type</th>
              <th>Location</th>
              <th>Surname</th>
              <th>Plate #</th>
            </tr>
          </thead>
        </Table>
      </div>
      </>
    );
  }
