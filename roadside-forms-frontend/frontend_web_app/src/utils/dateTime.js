import moment from "moment";

export const getCurrentDateTime = () => {
  const now = new Date();
  const dayString = now.toLocaleDateString("en-CA", { weekday: "long" });
  const dateString = now.toLocaleDateString("en-CA");
  const pacificTime = now.toLocaleTimeString("en-CA", {
    timeZone: "America/Vancouver",
    hour12: false,
  });
  const timeString = pacificTime.substr(0, 5);
  return { dateString, dayString, timeString };
};

export const convertToPST = (datetime) => {
  var myDate = new Date(datetime);
  var pstDate = myDate.toLocaleString("en-US", {
    timeZone: "America/Los_Angeles",
  });
  return pstDate;
};

// 2023-10-23 16:04:44
export const convertToPSTFormat = (datetime) => {
  return moment(datetime).tz("America/Vancouver").format("YYYY-MM-DD HH:mm:ss");
};

export const pstDate = (datetime) => {
  var myDate = new Date(datetime);
  var pstDate = new Date(
    myDate.toLocaleString("en-US", {
      timeZone: "America/Los_Angeles",
    })
  );
  return pstDate;
};

export const dateSortReactTable = (a, b, order) => {
  // Use 1000-01-01 as the default date for null values (only for sorting)
  const oldDate = '1000-01-01T00:00:00Z';
  const valueA = moment(a || oldDate);
  const valueB = moment(b || oldDate);
  
  return order === 'asc' ? valueA.valueOf() - valueB.valueOf() : valueB.valueOf() - valueA.valueOf();
};