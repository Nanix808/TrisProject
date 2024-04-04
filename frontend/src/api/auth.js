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
  // DefaultApiInstance.defaults.headers.common['Authorization'] =
  //   'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYXZvc2ludml0YWxpQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoic2F2b3NpbnZpdGFsaUBnbWFpbC5jb20iLCJlbWFpbCI6bnVsbCwiZXhwIjoxNzEyMTUyMjQzLCJpYXQiOjE3MTIxNDUwNDN9.Tb5ILF2hNFKQvRiNwiDMsyoUpPzRqqQw2u8w9Fx4PdLJGKxXA1bSSGYdY4evnWQwp91Ym8aeX_8r84xoyLQ8QQC0iAyC5_27bDKuOxKwTLHIO-mL67LQcAIkVJA9Wv3krqYfaM-Iwj8kofMZD5jTVc88oddCYqhOl-dWfF3wHKgiL2GpTtRwx5YifoljidmrqpJ34ycnS5gy-O93BVv65Ef9w6j0w30I0nqsal_Fi-NFy4ZqJ9clKLWviCDRQhbXBEjNgmFTcquDM9B-UljNy3uq0ADIdvRVuNwbDNWJ-t_s7RX1SArv4fLUOrWg2txBhnIk92DNlffBxAkc0Q0_pA';
  return DefaultApiInstance.post(url, {}, config);
};
