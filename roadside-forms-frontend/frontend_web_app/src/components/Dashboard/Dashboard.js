import React, { useEffect, useState } from "react";
import EditIcon from "@mui/icons-material/Edit";
import ErrorOutlineIcon from "@mui/icons-material/ErrorOutline";
import CheckCircleOutlineIcon from "@mui/icons-material/CheckCircleOutline";
import AddIcon from "@mui/icons-material/Add";
import Table from "react-bootstrap/Table";
import { useRecoilState } from "recoil";
import { FormSubmissionApi } from "../../api/formSubmissionApi";
import {
  staticResources,
  formTypes,
  eventObjectFlatener,
  eventDataFormatter,
} from "../../utils/helpers";
import { eventDataUpsert } from "../../utils/dbHelpers";
import { convertToPST } from "../../utils/dateTime";
import { StaticDataApi } from "../../api/staticDataApi";
import { Button } from "../common/Button/Button";
import { useNavigate, Link } from "react-router-dom";
import { db } from "../../db";
import "./dashboard.scss";

export const Dashboard = () => {
  const navigate = useNavigate();
  const [formsData, setFormsData] = useState([]);
  const [staticDataLoaded, setStaticDataLoaded] = useState(false);

  const [agencyResource, setAgencyResource] = useRecoilState(
    staticResources["agencies"]
  );
  const [cityResource, setCityResource] = useRecoilState(
    staticResources["cities"]
  );
  const [countryResource, setCountryResource] = useRecoilState(
    staticResources["countries"]
  );
  const [jusrisdictionResource, setJurisdictionResource] = useRecoilState(
    staticResources["jurisdictions"]
  );
  const [impoundResource, setImpoundResource] = useRecoilState(
    staticResources["impound_lot_operators"]
  );
  const [provinceResource, setProvinceResource] = useRecoilState(
    staticResources["provinces"]
  );
  const [vehicleStyleResource, setVehicleStyleResource] = useRecoilState(
    staticResources["vehicle_styles"]
  );
  const [vehicleColourResource, setVehicleColourResource] = useRecoilState(
    staticResources["vehicle_colours"]
  );
  const [vehicleResource, setVehicleResource] = useRecoilState(
    staticResources["vehicles"]
  );

  useEffect(() => {
    const fetchData = async () => {
      try {
        const agencyData = await StaticDataApi.get("agencies");
        const cityData = await StaticDataApi.get("cities");
        const countryData = await StaticDataApi.get("countries");
        const jurisdictionData = await StaticDataApi.get("jurisdictions");
        const impoundData = await StaticDataApi.get("impound_lot_operators");
        const provinceData = await StaticDataApi.get("provinces");
        const vehicleStyleData = await StaticDataApi.get("vehicle_styles");
        const vehicleColourData = await StaticDataApi.get("vehicle_colours");
        const vehicleData = await StaticDataApi.get("vehicles");

        setVehicleResource(vehicleData.data);
        setVehicleStyleResource(vehicleStyleData.data);
        setVehicleColourResource(vehicleColourData.data);
        setProvinceResource(provinceData.data);
        setImpoundResource(impoundData.data);
        setJurisdictionResource(jurisdictionData.data);
        setCountryResource(countryData.data);
        setCityResource(cityData.data);
        setAgencyResource(agencyData.data);
        setStaticDataLoaded(true);

        try {
          db.vehicles.bulkPut(vehicleData.data);
          db.vehicleStyles.bulkPut(vehicleStyleData.data);
          db.vehicleColours.bulkPut(vehicleColourData.data);
          db.provinces.bulkPut(provinceData.data);
          db.impoundLotOperators.bulkPut(impoundData.data);
          db.jurisdictions.bulkPut(jurisdictionData.data);
          db.countries.bulkPut(countryData.data);
          db.cities.bulkPut(cityData.data);
          db.agencies.bulkPut(agencyData.data);
        } catch (error) {
          console.log(error);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
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
    setFormsData,
    setStaticDataLoaded,
  ]);

  useEffect(() => {
    const fetchEventData = async () => {
      const eventData = await FormSubmissionApi.get();
      const flattenedEventData = eventDataFormatter(
        eventObjectFlatener(eventData),
        provinceResource,
        vehicleResource,
        vehicleStyleResource,
        jusrisdictionResource,
        cityResource,
        impoundResource
      );
      if (flattenedEventData.length) {
        db.event.bulkPut(flattenedEventData);
        console.log(flattenedEventData);
        setFormsData(flattenedEventData);
      }
    };
    if (staticDataLoaded) {
      fetchEventData();
    }
  }, [
    provinceResource,
    vehicleResource,
    vehicleStyleResource,
    jusrisdictionResource,
    cityResource,
    impoundResource,
    staticDataLoaded,
  ]);

  const handleClick = () => {
    navigate("/createEvent");
  };
  return (
    <>
      <div className="border-design text-font">
        <div className="dashboard-header">
          <h3>
            <EditIcon />
            Events in Progress
          </h3>
          <Button
            primary
            size="large"
            onClick={handleClick}
            label="New Event"
            icon={<AddIcon />}
          />
        </div>
        <hr className="hr" />
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
          <tbody>
            {formsData.map((data, index) => {
              return !data["submitted"] ? (
                <tr key={data["vehicle_vin_no"]}>
                  <td>
                    {data["created_dt"]
                      ? convertToPST(data["created_dt"])
                      : "N/A"}
                  </td>
                  <td>{formTypes(data)}</td>
                  <td>
                    {data["intersection_or_address_of_offence"]
                      ? data["intersection_or_address_of_offence"]
                      : "N/A"}
                  </td>
                  <td>
                    {data["driver_last_name"]
                      ? data["driver_last_name"]
                      : "N/A"}
                  </td>
                  <td>
                    {data["vehicle_plate_no"]
                      ? data["vehicle_plate_no"]
                      : "N/A"}
                  </td>
                  <td>Print</td>
                </tr>
              ) : null;
            })}
          </tbody>
        </Table>
      </div>
      <div className="border-design text-font">
        <div className="dashboard-header">
          <h3>
            <ErrorOutlineIcon />
            Waiting for Transmission to Server
          </h3>
          <span>Automatically re-trying in x seconds</span>
        </div>
        <hr className="hr" />
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
      <div className="border-design text-font">
        <div className="dashboard-header">
          <h3>
            <CheckCircleOutlineIcon />
            Completed
          </h3>
          <span>Last updated on date</span>
        </div>
        <hr className="hr" />
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
          <tbody>
            {formsData.map((data, index) => {
              return data["submitted"] ? (
                <tr key={data["vehicle_vin_no"]}>
                  <td>
                    <Link
                      to="/view-previous"
                      state={{ eventId: data["event_id"] }}
                    >
                      {data["created_dt"]
                        ? convertToPST(data["created_dt"])
                        : "N/A"}
                    </Link>
                  </td>
                  <td>{data["VI_number"]}</td>
                  <td>{formTypes(data)}</td>
                  <td>
                    {data["intersection_or_address_of_offence"]
                      ? data["intersection_or_address_of_offence"]
                      : "N/A"}
                  </td>
                  <td>
                    {data["driver_last_name"]
                      ? data["driver_last_name"]
                      : "N/A"}
                  </td>
                  <td>
                    {data["vehicle_plate_no"]
                      ? data["vehicle_plate_no"]
                      : "N/A"}
                  </td>
                </tr>
              ) : null;
            })}
          </tbody>
        </Table>
      </div>
    </>
  );
};
