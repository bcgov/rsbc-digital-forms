import { atom } from "recoil";

export const usersAtom = atom({
  key: "users",
  default: null,
});

export const userAtom = atom({
  key: "user",
  default: [],
});
