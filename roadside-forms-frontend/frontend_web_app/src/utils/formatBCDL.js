export const formatBCDL = (dlNumber, values) => {
  if (
    values["TwelveHour"] ||
    (values["drivers_licence_jurisdiction"] &&
      values["drivers_licence_jurisdiction"].label === "BRITISH COLUMBIA")
  ) {
    if (dlNumber.length === 7) {
      return "0" + dlNumber.toUpperCase();
    }
  }
  return dlNumber.toUpperCase();
};
