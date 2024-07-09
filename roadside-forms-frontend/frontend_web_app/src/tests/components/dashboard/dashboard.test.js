import React from 'react';
import { act, render } from '@testing-library/react';
import { RecoilRoot } from 'recoil';
import { Dashboard } from '../../../components/Dashboard/Dashboard';
import { StaticDataApi } from '../../../api/staticDataApi';
import { FormSubmissionApi } from '../../../api/formSubmissionApi';
import { vehicleStyles, jurisdictions, provinces, vehicles, vehicleColours, cities, impoundLotOperators } from '../../../atoms/staticData';
jest.mock('react-router-dom', () => ({
    ...jest.requireActual('react-router-dom'),
    useNavigate: jest.fn(),
  }));
describe('Dashboard', () => {
    beforeAll(() => {
        jest.useFakeTimers();
        jest.setSystemTime(new Date("2024-01-01T00:00"));
    });

    afterAll(() => {
        jest.useRealTimers();
    });

    test('renders dashboard component correctly', async () => {
    StaticDataApi.get = jest.fn().mockImplementation(async (table) => {
        switch (table) {
            case "vehicle_styles":
                return { data: [{
                    "code": "2DR",
                    "name": "2-DOOR SEDAN"
                },
                {
                    "code": "3DR",
                    "name": "3-DOOR HATCH"
                }]};
            case "jurisdictions":
                return { data: [{
                    "id": 1,
                    "objectCd": "AL",
                    "objectDsc": "ALABAMA"
                },
                {
                    "id": 2,
                    "objectCd": "AK",
                    "objectDsc": "ALASKA"
                }]};
            case "provinces":
                return { data: [{
                    "id": 1,
                    "objectCd": "AK",
                    "objectDsc": "ALASKA"
                },
                {
                    "id": 2,
                    "objectCd": "ALTA",
                    "objectDsc": "ALBERTA"
                }]};
            case "vehicles":
                return { data: [{
                    "id": 123,
                    "mk": "AC",
                    "search": "A C (GREAT BRITAIN)",
                    "md": ""
                },
                {
                    "id": 124,
                    "mk": "AC",
                    "search": "A C (GREAT BRITAIN) - 3000 ME",
                    "md": "300"
                }]};
            case "vehicle_colours":
                return { data: [
                    {"code": 'test', 
                    "display_name": 'test'}
                ]};
            case "cities":
                return { data: [{
                    "id": 1,
                    "objectCd": "OH3H",
                    "objectDsc": "100 TEST 1 HOUSE"
                },
                {
                    "id": 2,
                    "objectCd": "OHdM",
                    "objectDsc": "106 TEST HOUSE"
                }]};
            case "impound_lot_operators":
                return { data: [
                {
                    "id": 1,
                    "name": "Tset",
                    "lot_address": "Test ST",
                    "city": "TEST",
                    "phone": "250-000-5343"
                },
                {
                    "id": 2,
                    "name": "Tset",
                    "lot_address": "Test ST",
                    "city": "TEST",
                    "phone": "250-000-5343"
                }]};
            default:
                return {data: []};
        }
    });
    FormSubmissionApi.get = jest.fn().mockResolvedValue({});
    
    let container;
    await act(async () => {
        ({ container } = render( 
            <RecoilRoot>
            <Dashboard />
            </RecoilRoot>
        ));
    });

    expect(container).toMatchSnapshot();
});
});
