import { DefaultApiInstance } from '@/api/apiinstanse.js';

export const getTransport = () => {
  const url = '/transport/';
  return DefaultApiInstance.get(url);
};

export const getTransport_by_date = (date) => {
  const url = '/transport/get_by_date/';
  return DefaultApiInstance.post(url, date);
};

export const getCars = () => {
  const url = '/transport/cars/';
  return DefaultApiInstance.get(url);
};

export const addTransport = (payload) => {
  console.log(payload);
  const url = '/transport/';
  return DefaultApiInstance.post(url, payload);
};

// export const createUser = (payload) => {
//   const url = '/users/';
//   return DefaultApiInstance.post(url, payload);
// };
