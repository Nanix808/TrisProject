import axios from 'axios';
import router from '@/router';
import store from '@/store';

const baseURL = import.meta.env.VITE_BASE_URL;

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
        store.commit('resetUser');
        store.commit('openLoginPopup');
      });
    }

    if (error.response.status === 401) {
      // router.push ({name: 'login'})
    }
    return Promise.reject(error);
  }
);

export { DefaultApiInstance };
