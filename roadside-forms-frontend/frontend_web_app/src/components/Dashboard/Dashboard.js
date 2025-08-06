import React, { useEffect, useState } from "react";
import EditIcon from "@mui/icons-material/Edit";
import ErrorOutlineIcon from "@mui/icons-material/ErrorOutline";
import CheckCircleOutlineIcon from "@mui/icons-material/CheckCircleOutline";
import AddIcon from "@mui/icons-material/Add";
import Table from "react-bootstrap/Table";
import { useRecoilState } from "recoil";
import { useNavigate, Link } from "react-router-dom";
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
import { db } from "../../db";
import { userAtom } from "../../atoms/users";
import { useAuth } from "react-oidc-context";
import "./dashboard.scss";
import { FormIDApi } from "../../api/formIDApi";
import { getAllFormIDs } from "../../utils/dbHelpers";
import { useSharedIsOnline } from "../../utils/connectivity";
import { ArrowDownwardRounded, ArrowUpwardRounded } from "@mui/icons-material";

export const Dashboard = () => {
  const auth = useAuth();
  const { isConnected } = useSharedIsOnline();
  const navigate = useNavigate();
  const [formsData, setFormsData] = useState([]);
  const [incompleteFormsData, setIncompleteFormsData] = useState([]);
  const [completedTableRows, setCompletedTableRows] = useState([]);
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
  const [nscPujResource, setNscPujResource] = useRecoilState(
    staticResources["nscPuj"]
  );
  const [jurisdictionCountryResource, setJurisdictionCountryResource] =
    useRecoilState(staticResources["jurisdictionCountry"]);
  const [lastUpdatedDate, setLastUpdatedDate] = useState(null);
  const [sortMode, setSortMode] = useState("DATE_DESC");
  const [formIDsLoaded, setFormIDsLoaded] = useState(false);

  useEffect(() => {
    async function sortRows() {
      if (formsData && formsData.length > 0) {
        const rows = await sortTableRows(formsData);
        await setCompletedTableRows(rows);
      }
    }
    sortRows();
  }, [formsData, sortMode]);

  const sortTableRows = (rows) => {
    switch (sortMode) {
      case "DATE_ASC":
        return rows.sort((a, b) => {
          return new Date(a.created_dt) - new Date(b.created_dt);
        });
      case "DATE_DESC":
        return rows.sort((a, b) => {
          return new Date(b.created_dt) - new Date(a.created_dt);
        });
      case "SURNAME_ASC":
        return rows.sort((a, b) => {
          return a.driver_last_name.localeCompare(b.driver_last_name);
        });
      case "SURNAME_DESC":
        return rows.sort((a, b) => {
          return b.driver_last_name.localeCompare(a.driver_last_name);
        });
      default:
        return rows;
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      if (isConnected) {
        try {
          const agencyData = await StaticDataApi.get("agencies", auth);
          const cityData = await StaticDataApi.get("cities", auth);
          const countryData = await StaticDataApi.get("countries", auth);
          const jurisdictionData = await StaticDataApi.get("jurisdictions", auth);
          const impoundData = await StaticDataApi.get("impound_lot_operators", auth);
          const provinceData = await StaticDataApi.get("provinces", auth);
          const vehicleStyleData = await StaticDataApi.get("vehicle_styles", auth);
          const vehicleTypeData = await StaticDataApi.get("vehicle_types", auth);
          const vehicleColourData = await StaticDataApi.get("vehicle_colours", auth);
          const vehicleData = await StaticDataApi.get("vehicles", auth);
          const nscPujData = await StaticDataApi.get("nsc_puj", auth);
          const jurisdictionCountryData = await StaticDataApi.get(
            "jurisdiction_country", auth
          );

          // Sort vehicle data alphabetically
          const dataObj = vehicleData.data;
          dataObj.sort((a, b) => a.search.localeCompare(b.search));

          setVehicleResource(dataObj);
          setVehicleStyleResource(vehicleStyleData.data);
          setVehicleColourResource(vehicleColourData.data);
          setProvinceResource(provinceData.data);
          setImpoundResource(impoundData.data);
          setJurisdictionResource(jurisdictionData.data);
          setCountryResource(countryData.data);
          setCityResource(cityData.data);
          setAgencyResource(agencyData.data);
          setVehicleTypeResource(vehicleTypeData.data);
          setNscPujResource(nscPujData.data);
          setJurisdictionCountryResource(jurisdictionCountryData.data);

          try {
            await db.vehicles.clear();
            await db.vehicleStyles.clear();
            await db.vehicleColours.clear();
            await db.provinces.clear();
            await db.impoundLotOperators.clear();
            await db.jurisdictions.clear();
            await db.countries.clear();
            await db.cities.clear();
            await db.vehicleTypes.clear();
            await db.agencies.clear();
            await db.nscPuj.clear();
            await db.jurisdictionCountry.clear();

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
            await db.nscPuj.bulkPut(nscPujData.data);
            await db.jurisdictionCountry.bulkPut(jurisdictionCountryData.data);
          } catch (error) {
            console.log(error);
          }
        } catch (error) {
          console.error("Error fetching data:", error);
        }
        setStaticDataLoaded(true);
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
        setNscPujResource(await db.nscPuj.toArray());
        setJurisdictionCountryResource(await db.jurisdictionCountry.toArray());
        setStaticDataLoaded(true);
      }
    };

    fetchData();
    setLastUpdatedDate(new Date().toLocaleString());
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
    setJurisdictionCountryResource,
    setNscPujResource,
    isConnected,
    auth,
  ]);

  useEffect(() => {
    const fetchEventData = async () => {
      if (isConnected) {
        const eventData = await FormSubmissionApi.get(auth);
        const flattenedEventData = eventDataFormatter(
          eventObjectFlatener(eventData),
          userResource,
          provinceResource,
          vehicleResource,
          vehicleStyleResource,
          jusrisdictionResource,
          cityResource,
          impoundResource,
          jurisdictionCountryResource,
          nscPujResource
        );
        if (flattenedEventData.length) {
          await db.event.bulkPut(flattenedEventData);
          setFormsData(flattenedEventData);
        }
      } else {
        const data = await db.event.toArray();
        setFormsData(data);
      }
      const incompleteForms = await db.incompleteEvent.toArray();
      setIncompleteFormsData(incompleteForms);
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
    jurisdictionCountryResource,
    nscPujResource,
    isConnected,
    auth,
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
      if (neededFormID["12Hour"] > 0 || neededFormID["24Hour"] > 0 || neededFormID["VI"] > 0) {
        const newIDs = await FormIDApi.post(neededFormID, auth);
        if (newIDs) { 
          const seededIDs = await seedLeasedValues(newIDs.forms);
          await db.formID.bulkPut(seededIDs);
        }
      }
      setFormIDsLoaded(true);
    };

    const fetchCurrentIDs = async () => {
      const currentIDs = await FormIDApi.get(auth);
      const seededIDs = await seedLeasedValues(currentIDs);
      await db.formID.bulkPut(seededIDs);
    };

    if (staticDataLoaded) {
      if (isConnected) {
        fetchNeededIDs();
        // fetchCurrentIDs().then(() => );
      }
    }
  }, [staticDataLoaded, isConnected, auth]);

  const handleClick = () => {
    navigate("/createEvent");
  };

  //TODO: add in pull for incomplete events.

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
            disabled={!formIDsLoaded}
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
              {/* <th>Date & Time</th> */}
              <th>Surname</th>
              <th>Form Type</th>
              <th>Form #</th>
              <th>Plate #</th>
              <th>Location</th>
            </tr>
          </thead>
          <tbody>
            {incompleteFormsData.map((data, index) => {
              return (
                <tr key={data["vehicle_vin_no"]+"_"+data["inc_event_id"]}>
                  {/* <td>
                    {data["created_dt"]
                      ? convertToPSTFormat(data["created_dt"])
                      : "N/A"}
                  </td> */}
                  <td>
                    <Link
                      to="/createEvent"
                      state={{
                        incEventId: data["inc_event_id"],
                      }}
                    >
                      {data["driver_last_name"]
                        ? data["driver_last_name"]
                        : "N/A"}
                    </Link>
                  </td>
                  <td>{formTypes(data)}</td>

                  <td>
                    <Link
                      to="/createEvent"
                      state={{
                        incEventId: data["inc_event_id"],
                      }}
                    >
                      {formNumbers(data)}
                    </Link>
                  </td>
                  <td>
                    {data["vehicle_plate_no"]
                      ? data["vehicle_plate_no"]
                      : "N/A"}
                  </td>
                  <td>
                    {data["intersection_or_address_of_offence"]
                      ? data["intersection_or_address_of_offence"]
                      : "N/A"}
                  </td>
                </tr>
              );
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
        </div>
        <hr className="hr" />
        <Table>
          <thead>
            <tr>
              <th>Date & Time</th>
              <th>Surname</th>
              <th>Form Type</th>
              <th>Form #</th>
              <th>Plate #</th>
              <th>Location</th>
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
          <span>Last updated at {lastUpdatedDate}</span>
        </div>
        <hr className="hr" />
        <Table>
          <thead>
            <tr>
              <th>
                Date & Time
                <ArrowUpwardRounded
                  onClick={() => setSortMode("DATE_ASC")}
                  style={{
                    cursor: "pointer",
                    color: sortMode === "DATE_ASC" ? "black" : "gray",
                  }}
                />
                <ArrowDownwardRounded
                  onClick={() => setSortMode("DATE_DESC")}
                  style={{
                    cursor: "pointer",
                    color: sortMode === "DATE_DESC" ? "black" : "gray",
                  }}
                />
              </th>
              <th>
                Surname
                <ArrowUpwardRounded
                  onClick={() => setSortMode("SURNAME_ASC")}
                  style={{
                    cursor: "pointer",
                    color: sortMode === "SURNAME_ASC" ? "black" : "gray",
                  }}
                />
                <ArrowDownwardRounded
                  onClick={() => setSortMode("SURNAME_DESC")}
                  style={{
                    cursor: "pointer",
                    color: sortMode === "SURNAME_DESC" ? "black" : "gray",
                  }}
                />
              </th>
              <th>Form Type</th>
              <th>Form #</th>
              <th>Plate #</th>
              <th>Location</th>
            </tr>
          </thead>
          <tbody>
            {completedTableRows.map((data, index) => {
              return data["submitted"] ? (
                <tr key={data["vehicle_vin_no"]+"_"+data["event_id"]}>
                  <td>
                    {data["created_dt"]
                      ? convertToPSTFormat(data["created_dt"])
                      : "N/A"}
                  </td>
                  <td>
                    <Link
                      to="/view-previous"
                      state={{ eventId: data["event_id"] }}
                    >
                      {data["driver_last_name"]
                        ? data["driver_last_name"]
                        : "N/A"}
                    </Link>
                  </td>
                  <td>{formTypes(data)}</td>

                  <td>
                    <Link
                      to="/view-previous"
                      state={{ eventId: data["event_id"] }}
                    >
                      {formNumbers(data)}
                    </Link>
                  </td>
                  <td>
                    {data["vehicle_plate_no"]
                      ? data["vehicle_plate_no"]
                      : "N/A"}
                  </td>
                  <td>
                    {data["intersection_or_address_of_offence"]
                      ? data["intersection_or_address_of_offence"]
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
