export interface UserPayload {
  email: string;
  password: string;
}

export interface User {
  email: string;
}

export interface ILoginResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
}
