import { DefaultApiInstance } from '@/api/apiinstanse.js';

export const login = (payload) => {
  const url = '/auth/login/';
  return DefaultApiInstance.post(url, payload);
};

export const refresh = () => {
  const url = '/auth/refresh/';
  const config = {
    headers: {
      Authorization: `Bearer ${localStorage.getItem('refreshToken')}`,
      'Content-Type': 'application/json',
    },
  };
  return DefaultApiInstance.post(url, {}, config);
};
