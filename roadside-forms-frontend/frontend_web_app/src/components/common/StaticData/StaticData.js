import React from "react";
import PropTypes from "prop-types";
import { staticResources } from "../../../utils/helpers";
import { useSetRecoilState } from "recoil";
import { StaticDataApi } from "../../../api/staticDataApi";

export const StaticData = () => {
  const setAgencyResource = useSetRecoilState(staticResources["agencies"]);
  const setCityResource = useSetRecoilState(staticResources["cities"]);
  const setCountryResource = useSetRecoilState(staticResources["countries"]);
  const setJurisdictionResource = useSetRecoilState(
    staticResources["jurisdictions"],
  );
  const setImpoundResource = useSetRecoilState(
    staticResources["impound_lot_operators"],
  );
  const setProvinceResource = useSetRecoilState(staticResources["provinces"]);
  const setVehicleStyleResource = useSetRecoilState(
    staticResources["vehicle_styles"],
  );
  const setVehicleResource = useSetRecoilState(staticResources["vehicles"]);

  const handleStaticDataPull = () => {
    const agencyData = StaticDataApi.get("agencies").data;
    const cityData = StaticDataApi.get("cities").data;
    const contryData = StaticDataApi.get("countries").data;
    const jurisdictionData = StaticDataApi.get("jurisdictions").data;
    const impoundData = StaticDataApi.get("impound_lot_operators").data;
    const provinceData = StaticDataApi.get("provinces").data;
    const vehicleStyleData = StaticDataApi.get("vehicle_styles").data;
    const vehicleData = StaticDataApi.get("vehicles").data;

    setVehicleResource(vehicleData);
    setVehicleStyleResource(vehicleStyleData);
    setProvinceResource(provinceData);
    setImpoundResource(impoundData);
    setJurisdictionResource(jurisdictionData);
    setCountryResource(contryData);
    setCityResource(cityData);
    setAgencyResource(agencyData);
  };
  handleStaticDataPull();
  return null;
};

StaticData.propTypes = {
  user: PropTypes.shape({}),
};

StaticData.defaultProps = {
  user: null,
};
