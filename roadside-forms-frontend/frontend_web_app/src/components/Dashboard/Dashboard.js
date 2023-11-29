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
  formNumbers,
} from "../../utils/helpers";
import { convertToPST, convertToPSTFormat } from "../../utils/dateTime";
import { StaticDataApi } from "../../api/staticDataApi";
import { Button } from "../common/Button/Button";
import { useNavigate, Link } from "react-router-dom";
import { db } from "../../db";
import { userAtom } from "../../atoms/users";
import "./dashboard.scss";
import { FormIDApi } from "../../api/formIDApi";
import { getAllFormIDs } from "../../utils/dbHelpers";
import { useSharedIsOnline } from "../../utils/connectivity";

export const Dashboard = () => {
  const { isConnected } = useSharedIsOnline();
  const navigate = useNavigate();
  const [formsData, setFormsData] = useState([]);
  const [staticDataLoaded, setStaticDataLoaded] = useState(false);
  const [userResource, setUserResource] = useRecoilState(userAtom);
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
  const [vehicleTypeResource, setVehicleTypeResource] = useRecoilState(
    staticResources["vehicle_types"]
  );
  const [vehicleColourResource, setVehicleColourResource] = useRecoilState(
    staticResources["vehicle_colours"]
  );
  const [vehicleResource, setVehicleResource] = useRecoilState(
    staticResources["vehicles"]
  );

  const sortTableRows = (rows) => {
    if (rows.length > 0) {
      return rows.sort((a, b) => {
        return new Date(b.created_dt) - new Date(a.created_dt);
      });
    } else {
      return rows;
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      if (isConnected) {
        try {
          const agencyData = await StaticDataApi.get("agencies");
          const cityData = await StaticDataApi.get("cities");
          const countryData = await StaticDataApi.get("countries");
          const jurisdictionData = await StaticDataApi.get("jurisdictions");
          const impoundData = await StaticDataApi.get("impound_lot_operators");
          const provinceData = await StaticDataApi.get("provinces");
          const vehicleStyleData = await StaticDataApi.get("vehicle_styles");
          const vehicleTypeData = await StaticDataApi.get("vehicle_types");
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
          setVehicleTypeResource(vehicleTypeData.data);
          setStaticDataLoaded(true);

          try {
            await db.vehicles.bulkPut(vehicleData.data);
            await db.vehicleStyles.bulkPut(vehicleStyleData.data);
            await db.vehicleColours.bulkPut(vehicleColourData.data);
            await db.provinces.bulkPut(provinceData.data);
            await db.impoundLotOperators.bulkPut(impoundData.data);
            await db.jurisdictions.bulkPut(jurisdictionData.data);
            await db.countries.bulkPut(countryData.data);
            await db.cities.bulkPut(cityData.data);
            await db.vehicleTypes.bulkPut(vehicleTypeData.data);
            await db.agencies.bulkPut(agencyData.data);
          } catch (error) {
            console.log(error);
          }
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      } else {
        setVehicleResource(await db.vehicles.toArray());
        setVehicleStyleResource(await db.vehicleStyles.toArray());
        setVehicleColourResource(await db.vehicleColours.toArray());
        setProvinceResource(await db.provinces.toArray());
        setImpoundResource(await db.impoundLotOperators.toArray());
        setJurisdictionResource(await db.jurisdictions.toArray());
        setCountryResource(await db.countries.toArray());
        setCityResource(await db.cities.toArray());
        setAgencyResource(await db.agencies.toArray());
        setVehicleTypeResource(await db.vehicleTypes.toArray());
        setStaticDataLoaded(true);
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
    setVehicleTypeResource,
    isConnected,
  ]);

  useEffect(() => {
    const fetchEventData = async () => {
      if (isConnected) {
        const eventData = await FormSubmissionApi.get();
        const flattenedEventData = eventDataFormatter(
          eventObjectFlatener(eventData),
          userResource,
          provinceResource,
          vehicleResource,
          vehicleStyleResource,
          jusrisdictionResource,
          cityResource,
          impoundResource
        );
        if (flattenedEventData.length) {
          await db.event.bulkPut(flattenedEventData);
          setFormsData(flattenedEventData);
        }
      } else {
        const data = await db.event.toArray();
        setFormsData(data);
      }
    };
    if (staticDataLoaded) {
      fetchEventData();
    }
  }, [
    userResource,
    provinceResource,
    vehicleResource,
    vehicleStyleResource,
    jusrisdictionResource,
    cityResource,
    impoundResource,
    staticDataLoaded,
    isConnected,
  ]);

  useEffect(() => {
    const seedLeasedValues = async (idArray) => {
      if (idArray) {
        if (idArray.length > 0) {
          for (let i = 0; i < idArray.length; i++) {
            // Check if idArray[i] exists in indexedDB
            // If it does, check for leased property on that id
            // If it has a value, set the value = that value
            // Otherwise, set leased = false
            const existingId = await db.formID.get(idArray[i].id);
            if (existingId) {
              if (existingId.leased) {
                idArray[i].leased = existingId.leased;
              } else {
                idArray[i].leased = 0;
              }
            } else {
              idArray[i].leased = 0;
            }
          }
          return idArray;
        }
      }
      return [];
    };

    const fetchNeededIDs = async () => {
      const neededFormID = await getAllFormIDs();
      const newIDs = await FormIDApi.post(neededFormID);
      const seededIDs = await seedLeasedValues(newIDs.forms);
      await db.formID.bulkPut(seededIDs);
    };

    const fetchCurrentIDs = async () => {
      const currentIDs = await FormIDApi.get();
      const seededIDs = await seedLeasedValues(currentIDs);
      await db.formID.bulkPut(seededIDs);
    };

    if (staticDataLoaded) {
      if (isConnected) {
        fetchCurrentIDs().then(() => fetchNeededIDs());
      }
    }
  }, [staticDataLoaded, isConnected]);

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
            {formsData &&
              sortTableRows(formsData).map((data, index) => {
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
                        ? convertToPSTFormat(data["created_dt"])
                        : "N/A"}
                    </Link>
                  </td>
                  <td>{formNumbers(data)}</td>
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
