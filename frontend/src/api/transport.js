import { DefaultApiInstance } from '@/api/apiinstanse.js';

export const getTransport = () => {
  const url = '/transport/';
  return DefaultApiInstance.get(url);
};

// export const createUser = (payload) => {
//   const url = '/users/';
//   return DefaultApiInstance.post(url, payload);
// };
