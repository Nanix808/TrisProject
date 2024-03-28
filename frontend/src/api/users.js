import { DefaultApiInstance } from '@/api/apiinstanse.js';

export const getUsers = () => {
  const url = '/auth/users/me/';
  return DefaultApiInstance.get(url);
};

export const createUser = (payload) => {
  const url = '/users/';
  return DefaultApiInstance.post(url, payload);
};


