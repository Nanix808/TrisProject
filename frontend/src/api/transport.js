import { DefaultApiInstance } from '@/api/apiinstanse.js';

export const getTransport = () => {
  const url = '/transport/';
  return DefaultApiInstance.get(url);
};

export const getTransport_by_date = (date) => {
  const url = '/transport/get_by_date/';
  return DefaultApiInstance.get(url, {
    params: {
      date_in: date.date_in,
      car_id: date.car_id,
    },
  });
};

export const getCars = () => {
  const url = '/transport/cars/';
  return DefaultApiInstance.get(url);
};

export const addTransport = (payload) => {
  const url = '/transport/';
  return DefaultApiInstance.post(url, payload);
};

export const editTransport = (id, payload) => {
  const url = '/transport/' + id;
  return DefaultApiInstance.patch(url, payload);
};
export const deleteTransport = (id) => {
  const url = '/transport/' + id;
  return DefaultApiInstance.delete(url);
};

// export const createUser = (payload) => {
//   const url = '/users/';
//   return DefaultApiInstance.post(url, payload);
// };
