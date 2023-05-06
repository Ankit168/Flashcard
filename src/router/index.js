import Vue from 'vue';
import Router from 'vue-router';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';
import Dashboard from '../components/Dashboard.vue';
import AddNewCard from '../components/AddNewCard.vue';
import EditDeck from '../components/EditDeck.vue';
import ReviewDeck from '../components/ReviewDeck.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/',
            redirect: '/login'
        },
        {
            path: '/login',
            name: 'Login',
            component: Login,
        },
        {
            path: '/register',
            name: 'Register',
            component: Register,
        },
        {
            path: '/dashboard',
            name: 'Dashboard',
            component: Dashboard,
        },
        {
            props: true,
            path: '/addNewCard/:id',
            name: 'AddNewCard',
            component: AddNewCard,
        },
        {
            props: true,
            path: '/editDeck/:id',
            name: 'EditDeck',
            component: EditDeck,
        },
        {
            props: true,
            path: '/review/deck/:id',
            name: 'ReviewDeck',
            component: ReviewDeck,
        }
    ],
});