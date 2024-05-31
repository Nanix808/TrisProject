import { DefaultApiInstance } from '@/api/apiinstanse.js';

export const getTransport = () => {
  const url = '/transport/';
  return DefaultApiInstance.get(url);
};

export const getTransport_by_date = (date) => {
  const url = '/transport/get_by_date/';
  return DefaultApiInstance.post(url, { date_in: '05/25/2025' });
};

export const getCars = () => {
  const url = '/transport/cars/';
  return DefaultApiInstance.get(url);
};

// export const createUser = (payload) => {
//   const url = '/users/';
//   return DefaultApiInstance.post(url, payload);
// };
