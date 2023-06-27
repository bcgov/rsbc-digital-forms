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
                "objectCd": "OHMH",
                "objectDsc": "100 MILE HOUSE"
            },
            {
                "objectCd": "OHTM",
                "objectDsc": "103 MILE HOUSE"
            }]);
            snap.set(impoundLotOperators, [
            {
                "name": "24 HOUR TOWING",
                "lot_address": "728 PAYNE ST",
                "city": "CRESTON",
                "phone": "250-428-2323"
            },
            {
                "name": "5 STAR TOWING",
                "lot_address": "733 2ND AVE",
                "city": "PRINCE GEORGE",
                "phone": "250-614-9393"
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
