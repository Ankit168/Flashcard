import store from './store';
import router from './router';

export const BASE_URL = 'http://127.0.0.1:5000';
export const getUrl = url => `${BASE_URL}/${url}`

export const headerConfig = (requireToken = true) => {
    const userToken = store.getters.userToken;
    if (requireToken && !userToken) {
        alert('Please login!')
        router.push('/login');
        return;
    }
    console.log(userToken);
    const header = {};
    if (userToken) {
        header['Authorization'] = `Bearer ${userToken}`
    }
    header["Content-Type"] = "application/json";
    return { headers: {...header } };
}