import React from 'react';
import { VehicleImpoundment } from './vehicleImpoundment';
import { Prohibition } from './prohibition';
import { ReasonableGrounds } from './reasonableGrounds';
import PropTypes from 'prop-types';

export const TwentyFourHourForm = (props) => {
    const {cities, impoundLotOperators} = props;
 console.log(impoundLotOperators);
  return (
    <div>
    <VehicleImpoundment impoundLotOperators={impoundLotOperators}/>
    <Prohibition cities={cities}/>
    <ReasonableGrounds/>
    </div>
  );
}

TwentyFourHourForm.propTypes = {
    cities: PropTypes.array.isRequired,
    impoundLotOperators: PropTypes.array.isRequired
};
