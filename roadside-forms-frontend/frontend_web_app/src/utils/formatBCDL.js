export const formatBCDL = (event, values) => {
  if (
    values["TwelveHour"] ||
    (values["drivers_licence_jurisdiction"] &&
      values["drivers_licence_jurisdiction"].label === "BRITISH COLUMBIA")
  ) {
    if (event.target.value.length === 7) {
      return "0" + event.target.value.toUpperCase();
    }
  }
  return event.target.value.toUpperCase();
};
