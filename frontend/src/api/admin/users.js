import { DefaultApiInstance } from '@/api/apiinstanse.js';

export const getUsers = () => {
  const url = '/users/';
  return DefaultApiInstance.get(url);
};

export const getRoles = () => {
  const url = '/authorization/';
  return DefaultApiInstance.get(url);
};

export const getEndpoints = () => {
  const url = '/authorization/list_endpoints/';
  return DefaultApiInstance.get(url);
};

export const updateUser = (id, payload) => {
  const url = '/users/' + id;
  return DefaultApiInstance.patch(url, payload);
};

export const deleteUser = (id) => {
  const url = '/users/' + id;
  console.log(url);
  return DefaultApiInstance.delete(url);
};

export const adminaddRole = (payload) => {
  const url = '/authorization/';
  console.log(url, payload);
  return DefaultApiInstance.post(url, payload);
};
export const adminupdateRole = (id, payload) => {
  const url = '/authorization/' + id;

  return DefaultApiInstance.putch(url, payload);
};
