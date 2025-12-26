// intercepting all the request we send by adding all the correct headers. to make our life easier
import axios from 'axios';
import {ACCESS_TOKEN} from "./constants";
// import anything from the specified environment we chose
const api= axios.create({
    baseURL: import.meta.env.VITE_API_URL
})
api.interceptors.request.use(
    (config)=>{
        const token= localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error)=>{
        return Promise.reject(error)
    }   
    
)

export default api