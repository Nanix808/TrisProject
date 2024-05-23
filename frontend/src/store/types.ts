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

export interface Transport {
  notice: string;
  destination: string;
  type_task: string;
  status: string;
  contact: string;
  car_id: string;
  user_id: string;
  date_from: Date;
  date_to: Date;
  id: number;
}


export interface TransportState {
  transports: Transport[];
}
