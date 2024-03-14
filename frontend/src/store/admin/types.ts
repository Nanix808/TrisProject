export interface User {
  username: string;
  role_id: number;
  is_active: boolean;
  id: number;
}

export interface Role {
  name: string;
  description: string;
  permissions: boolean;
}

export interface UsersState {
  users: User[];
  roles: Role[];
}

// export interface Roles {
//   name: string;
//   description: string;
//   permissions: boolean;
// }

// export interface RolesState {
//   roles: Roles[];
// }
