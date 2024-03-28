import axios from "axios";
import router from "@/router";
import store from "@/store";

const baseURL = "http://127.0.0.1:8000";
// const baseURL = 'https://scaner.3s.by/api/v2/'

const defaultConfig = {
  baseURL: baseURL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 300000,
};
const DefaultApiInstance = axios.create(defaultConfig);

// Добавление интерцептора для запросов
DefaultApiInstance.interceptors.request.use(
  (config) => {
    // Здесь можно модифицировать конфигурацию запроса
    config.headers.authorization = `Bearer ${localStorage.getItem(
      "accessToken"
    )}`;

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
      "accessToken"
    )}`;
    // Здесь можно обработать успешный ответ
    return config;
  },
  (error) => {
    if (error.response.data.detail === "acccess token invalid") {
      axios
        .post(
          "http://127.0.0.1:8000/auth/refresh/",
          {},
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${localStorage.getItem("refreshToken")}`,
            },
          }
        )
        .then((res) => {
          localStorage.setItem("accessToken", res.data.access_token);
          error.config.headers.authorization = `Bearer ${res.data.access_token}`;
          return DefaultApiInstance(error.config);
        })
        .catch((error) => {
          if (
            error.response.data.detail ===
            "refresh token invalid (user not found)"
          ) {
            console.log("redirect to login");
            router.push({ name: "home" }).then(() => {
              store.commit("openLoginPopup");
            });
          }
        });
    }

    if (error.response.status === 401) {
      // router.push ({name: 'login'})
    }
    return Promise.reject(error);
  }
);

export { DefaultApiInstance };
