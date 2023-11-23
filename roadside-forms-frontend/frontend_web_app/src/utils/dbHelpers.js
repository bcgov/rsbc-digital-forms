import { db } from "../db";

export const getAllFormIDs = async () => {
  //get all current id's for user in indexddb
  //count each type remaining
  //add all types and counts to dict

  const idDict = { "12Hour": 0, "24Hour": 0, IRP: 0, VI: 0 };

  const keys = Object.keys(idDict);
  for (const key of keys) {
    await db.formID
      .where("form_type")
      .equals(key)
      .toArray()
      .then((value) => {
        idDict[key] =
          value.length >= 0 && value.length <= 5 ? 5 - value.length : 0;
      });
  }
  return idDict;
};
