import Vue from "vue";
import Vuex from "vuex";

import userStore from './userStore';
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const store = new Vuex.Store({
    ...userStore,
    plugins: [createPersistedState()],
})

export default store;