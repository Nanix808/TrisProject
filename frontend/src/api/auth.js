import {DefaultApiInstance} from '@/api/apiinstanse.js'


export const login = (payload) => { 
        const url = '/auth/login/';
        return DefaultApiInstance.post(url, payload)
}

