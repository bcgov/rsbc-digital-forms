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
  let myDate = new Date(datetime);
  let pstDate = myDate.toLocaleString("en-US", {
    timeZone: "America/Los_Angeles"
  });
  let newDate = new Date(pstDate);
  let day = newDate.getDate();
  let month = newDate.getMonth();
  let year = newDate.getFullYear();
  let hours = newDate.getHours();
  let minutes = newDate.getMinutes();
  let seconds = newDate.getSeconds();
  const formattedPSTDate = `${year}-${month + 1}-${day} ${hours}:${minutes}:${seconds}`;
  return formattedPSTDate;
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


