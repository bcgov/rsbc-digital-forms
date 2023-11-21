export const formatBCDL = (event, values) => {
  console.log("In format....");
  if (
    values["TwelveHour"] ||
    (values["drivers_licence_jurisdiction"] &&
      values["drivers_licence_jurisdiction"].label === "BRITISH COLUMBIA")
  ) {
    if (event.target.value.length === 7) {
      console.log("Returning value.");
      console.log("The DL we got was ", event.target.value);
      console.log(
        "The DL we are returning is ",
        "0" + event.target.value.toUpperCase()
      );
      return "0" + event.target.value.toUpperCase();
    }
  }
  console.log("Did not meet requirement.");
  console.log("The DL we got was ", event.target.value);
  return event.target.value.toUpperCase();
};
