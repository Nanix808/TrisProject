import { DefaultApiInstance } from '@/api/apiinstanse.js';

export const addCar = (payload) => {
  const url = '/transport/cars/';
  return DefaultApiInstance.post(url, { name: payload.name });
};

export const updateCar = (id, payload) => {
  const url = '/transport/cars/' + id;
  return DefaultApiInstance.patch(url, payload);
};

export const deleteCar = (id) => {
  const url = '/transport/cars/' + id;
  return DefaultApiInstance.delete(url);
};
