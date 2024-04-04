import axios from 'axios';
import router from '@/router';
import store from '@/store';

const baseURL = 'http://127.0.0.1:8000';
// const baseURL = 'https://scaner.3s.by/api/v2/'

const defaultConfig = {
  baseURL: baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 300000,
};
const DefaultApiInstance = axios.create(defaultConfig);

const Endpoints = {
  AUTH: {
    LOGIN: '/auth/login/',
    REFRESH: '/auth/refresh/',
    LOGOUT: '/auth/logout/',
    PROFILE: '/auth/profile/',
  },
};

const urlsSkipAuth = [
  Endpoints.AUTH.LOGIN,
  Endpoints.AUTH.REFRESH,
  Endpoints.AUTH.LOGOUT,
];

// Добавление интерцептора для запросов
DefaultApiInstance.interceptors.request.use(
  async (config) => {
    if (config.url && urlsSkipAuth.includes(config.url)) {
      return config;
    }
    // Здесь можно модифицировать конфигурацию запроса
    // config.headers.authorization = `Bearer ${localStorage.getItem(
    //   'accessToken'
    // )}`;
    const accessToken = await store.dispatch('getAccessToken');

    if (accessToken) {
      const autharization = `Bearer ${accessToken}`;
      // config.headers.authorization = autharization;

      config.headers = {
        ...config.headers,
        authorization: autharization,
      };
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
// Добавление интерцептора для запросов
// DefaultApiInstance.interceptors.request.use(
//   (config) => {
//     // if (config.url && urlsSkipAuth.includes(config.url)) {
//     //   return config;
//     // }
//     // Здесь можно модифицировать конфигурацию запроса
//     console.log('1111111111111111111111111');
//     // const accessToken = store.dispatch('getAccessToken');
//     console.log(accessToken, '22222222222222222222222');
//     // if (accessToken) {
//     //   const autharization = `Bearer ${accessToken}`;

//     //   config.headers = {
//     //     ...config.headers,
//     //     authorization: autharization,
//     //   };
//     //   // config.headers.authorization = `Bearer ${localStorage.getItem(
//     //   //   'accessToken'
//     //   // )}`;
//     // }
//     return config;
//   },
//   (error) => {
//     return Promise.reject(error);
//   }
// );

// Добавление интерцептора для ответов
DefaultApiInstance.interceptors.response.use(
  (config) => {
    config.headers.authorization = `Bearer ${localStorage.getItem(
      'accessToken'
    )}`;
    // Здесь можно обработать успешный ответ
    return config;
  },
  (error) => {
    if (
      error.response.data.detail === 'refresh token invalid (user not found)'
    ) {
      router.push({ name: 'home' }).then(() => {
        store.commit('openLoginPopup');
      });

      // axios
      //   .post(
      //     'http://127.0.0.1:8000/auth/refresh/',
      //     {},
      //     {
      //       headers: {
      //         'Content-Type': 'application/json',
      //         Authorization: `Bearer ${localStorage.getItem('refreshToken')}`,
      //       },
      //     }
      //   )
      //   .then((res) => {
      //     localStorage.setItem('accessToken', res.data.access_token);
      //     error.config.headers.authorization = `Bearer ${res.data.access_token}`;
      //     return '';
      //   })
      //   .catch((error) => {
      //     if (
      //       error.response.data.detail ===
      //       'refresh token invalid (user not found)'
      //     ) {
      //       console.log('redirect to login');
      //       router.push({ name: 'home' }).then(() => {
      //         store.commit('openLoginPopup');
      //       });
      //     }
      //   });
    }

    if (error.response.status === 401) {
      // router.push ({name: 'login'})
    }
    return Promise.reject(error);
  }
);

export { DefaultApiInstance };
