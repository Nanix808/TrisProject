import { DefaultApiInstance } from "@/api/apiinstanse.js";

export const getUsers = () => {
  const url = "/users/";
  return DefaultApiInstance.get(url);
};

export const getRoles = () => {
  const url = "/authorization/";
  return DefaultApiInstance.get(url);
};

export const updateUser = (id, payload) => {
  const url = '/users/' + id;
  console.log(payload);
  return DefaultApiInstance.patch(url, payload);
};
