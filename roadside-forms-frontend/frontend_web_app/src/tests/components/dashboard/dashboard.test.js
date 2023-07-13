import React from 'react';
import { render, act } from '@testing-library/react';
import { RecoilRoot } from 'recoil';
import { Dashboard } from '../../../components/Dashboard/Dashboard';
import { StaticDataApi } from '../../../api/staticDataApi';
import { vehicleStyles, jurisdictions, provinces, vehicles, vehicleColours, cities, impoundLotOperators } from '../../../atoms/staticData';
jest.mock('react-router-dom', () => ({
    ...jest.requireActual('react-router-dom'),
    useNavigate: jest.fn(),
  }));
describe('Dashboard component', () => {
    test('renders dashboard component correctly', async () => {
    StaticDataApi.get = jest.fn().mockResolvedValue({});
    
    let container; 

    await act(async () => {
      ({ container } = await render( 
        <RecoilRoot
          initializeState={(snap) => {
            snap.set(vehicleStyles, [  {
                "code": "2DR",
                "name": "2-DOOR SEDAN"
            },
            {
                "code": "3DR",
                "name": "3-DOOR HATCH"
            }]);
            snap.set(jurisdictions, [{
                "objectCd": "AL",
                "objectDsc": "ALABAMA"
            },
            {
                "objectCd": "AK",
                "objectDsc": "ALASKA"
            }]);
            snap.set(provinces, [{
                "objectCd": "AK",
                "objectDsc": "ALASKA"
            },
            {
                "objectCd": "ALTA",
                "objectDsc": "ALBERTA"
            }]);
            snap.set(vehicles, [{
                "mk": "AC",
                "search": "A C (GREAT BRITAIN)",
                "md": ""
            },
            {
                "mk": "AC",
                "search": "A C (GREAT BRITAIN) - 3000 ME",
                "md": "300"
            }]);
            snap.set(vehicleColours, [
                {"code": 'test', 
                "display_name": 'test'}
            ]);
            snap.set(cities, [{
                "objectCd": "OH3H",
                "objectDsc": "100 TEST 1 HOUSE"
            },
            {
                "objectCd": "OHdM",
                "objectDsc": "106 TEST HOUSE"
            }]);
            snap.set(impoundLotOperators, [
            {
                "name": "Tset",
                "lot_address": "Test ST",
                "city": "TEST",
                "phone": "250-000-5343"
            },
            {
                "name": "Tset",
                "lot_address": "Test ST",
                "city": "TEST",
                "phone": "250-000-5343"
            }]);
          }}
        >
          <Dashboard />
        </RecoilRoot>
      ));
    });

    expect(container).toMatchSnapshot();
});
});
