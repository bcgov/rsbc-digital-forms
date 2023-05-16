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
import { useNavigate} from 'react-router-dom';
import './dashboard.scss'

export const Dashboard = () => {
  const navigate = useNavigate();
  const setAgencyResource = useSetRecoilState(staticResources["agencies"]);
  const setCityResource = useSetRecoilState(staticResources["cities"]);
  const setCountryResource = useSetRecoilState(staticResources["countries"]);
  const setJurisdictionResource = useSetRecoilState(staticResources["jurisdictions"]);
  const setImpoundResource = useSetRecoilState(staticResources["impound_lot_operators"]);
  const setProvinceResource = useSetRecoilState(staticResources["provinces"]);
  const setVehicleStyleResource = useSetRecoilState(staticResources["vehicle_styles"]);
  const setVehicleColourResource = useSetRecoilState(staticResources["vehicle_colours"]);
  const setVehicleResource = useSetRecoilState(staticResources["vehicles"]);

  useEffect(() => {
    const fetchData = async () => {
      try {
          const agencyData = await StaticDataApi.get("agencies")
          const cityData = await StaticDataApi.get("cities")
          const contryData = await StaticDataApi.get("countries")
          const jurisdictionData = await StaticDataApi.get("jurisdictions")
          const impoundData = await StaticDataApi.get("impound_lot_operators")
          const provinceData = await StaticDataApi.get("provinces")
          const vehicleStyleData = await StaticDataApi.get("vehicle_styles")
          const vehicleColourData = await StaticDataApi.get("vehicle_colours")
          const vehicleData = await StaticDataApi.get("vehicles")
          
          setVehicleResource(vehicleData.data)
          setVehicleStyleResource(vehicleStyleData.data)
          setVehicleColourResource(vehicleColourData.data)
          setProvinceResource(provinceData.data)
          setImpoundResource(impoundData.data)
          setJurisdictionResource(jurisdictionData.data)
          setCountryResource(contryData.data)
          setCityResource(cityData.data)
          setAgencyResource(agencyData.data)
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };
  
       fetchData();
    }, [
      setVehicleResource,
      setVehicleColourResource,
      setVehicleStyleResource,
      setProvinceResource,
      setImpoundResource,
      setJurisdictionResource,
      setCountryResource,
      setCityResource,
      setAgencyResource,
    ]);


  const handleClick = () => {
    navigate("/createEvent");
  }
      return (
      <>
      <div className='border-design text-font'>
        <div className='dashboard-header'>
          <h3><EditIcon/>Events in Progress</h3>
          <Button primary size="large" onClick={handleClick} label="New Event" icon={<AddIcon/>} />
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
