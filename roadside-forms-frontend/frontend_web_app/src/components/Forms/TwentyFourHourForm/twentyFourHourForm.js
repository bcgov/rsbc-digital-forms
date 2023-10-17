import React from 'react';
import { VehicleImpoundment } from './vehicleImpoundment';
import { Prohibition } from './prohibition';
import { ReasonableGrounds } from './reasonableGrounds';
import { TestAdministered } from './testAdministered';
import PropTypes from 'prop-types';

export const TwentyFourHourForm = (props) => {
  const {cities, impoundLotOperators} = props;
  return (
    <div>
    <VehicleImpoundment impoundLotOperators={impoundLotOperators}/>
    <Prohibition cities={cities}/>
    <ReasonableGrounds/>
    <TestAdministered/>
    </div>
  );
}

TwentyFourHourForm.propTypes = {
    cities: PropTypes.array.isRequired,
    impoundLotOperators: PropTypes.array.isRequired
};
