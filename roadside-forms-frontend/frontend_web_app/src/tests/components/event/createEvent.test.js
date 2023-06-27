import React from 'react';
import { render, act } from '@testing-library/react';
import { RecoilRoot } from 'recoil';
import { CreateEvent } from '../../../components/Event/createEvent';
import { useNavigate } from 'react-router-dom';
import { vehicleStyles, jurisdictions, provinces, vehicles, vehicleColours, cities, impoundLotOperators } from '../../../atoms/staticData';

jest.mock('react-router-dom', () => ({
    ...jest.requireActual('react-router-dom'),
    useNavigate: jest.fn(),
  }));
describe('CreateEvent component', () => {
    test('renders create event component correctly', async () => {
    let container; 

    await act(async () => {
      ({ container } = render( 
        <RecoilRoot
          initializeState={(snap) => {
            snap.set(vehicleStyles, [  {
                "code": "2DR",
                "name": "2-DOOR "
            },
            {
                "code": "3DR",
                "name": "3-DOOR "
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
                "mk": "AC-TEST",
                "search": "A C (GREAT BRITAIN)",
                "md": ""
            },
            {
                "mk": "TEST",
                "search": "A C (GREAT BRITAIN) - 3000 ME",
                "md": "300"
            }]);
            snap.set(vehicleColours, [
                {"code": 'test', 
                "display_name": 'test'}
            ]);
            snap.set(cities, [{
                "objectCd": "TEST",
                "objectDsc": "10 TEST HOUSE"
            },
            {
                "objectCd": "OHTM",
                "objectDsc": "10390 TEST ST"
            }]);
            snap.set(impoundLotOperators, [
            {
                "name": "TSET",
                "lot_address": "7 TEST ST",
                "city": "TEST",
                "phone": "250-003-73654"
            },
            {
                "name": "TSET",
                "lot_address": "7 TEST ST",
                "city": "TEST",
                "phone": "250-003-73654"
            }]);
          }}
        >
          <CreateEvent />
        </RecoilRoot>
      ));
    });

    expect(container).toMatchSnapshot();
});
});
