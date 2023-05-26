import React from 'react';
import { VehicleImpoundment } from './component/vehicleImpoundment';
import { Prohibition } from './component/prohibition';
import { ReasonableGrounds } from './component/reasonableGrounds';
import PropTypes from 'prop-types';

export const TwentyFourHourForm = (props) => {
    const {cities, impoundLotOperators} = props;
 console.log(impoundLotOperators);
  return (
    <div>
    <VehicleImpoundment impoundLotOperators={impoundLotOperators}></VehicleImpoundment>
    <Prohibition cities={cities}></Prohibition>
    <ReasonableGrounds></ReasonableGrounds>
    </div>
  );
}

TwentyFourHourForm.propTypes = {
    cities: PropTypes.array.isRequired,
    impoundLotOperators: PropTypes.array.isRequired
};
