// import axios from 'axios';
import router from '../../router';
import { loginReq, userDeckReq, addNewCardServiceRequest, editDeckServiceRequest, deleteDeck, getCardsRequest, addDeckRequest, updateScoreReq } from '../../services';

const initialState = {
    isLoggedIn: false,
    userData: null,
}

const actions = {
    initLogin({ commit }, { username, password }) {
        loginReq(username, password).then(({ data }) => {
            commit('loginUserSuccess', {
                token: data.access_token,
                user: data.user
            })
        })
    },
    getUserDecks({ commit }) {
        return userDeckReq().then(res => {
            return res.data;
            // commit('initializeUserDecks', res.data)
        }).catch(() => {
            commit('logout');
        })
    },
    getDeckInfo({ dispatch }, deckId) {
        const decks = dispatch('getUserDecks');
        return decks.then((decks) => decks.find(({ id }) => Number(id) === Number(deckId)));
    },
    addNewCardRequest(_, { front, back, deck }) {
        return addNewCardServiceRequest(front, back, deck);
    },
    editDeckRequest(_, { name, id }) {
        return editDeckServiceRequest(name, id);
    },
    deleteDeck(_, id) {
        return deleteDeck(id)
    },
    getCards(_, id) {
        console.log(id)
        return getCardsRequest(id);
    },
    updateScore(_, { id, score }) {
        return updateScoreReq(id, score);
    },
    addDeck(_, name) {
        return addDeckRequest(name);
    }
}

const mutations = {
    loginUserSuccess(state, user) {
        state.isLoggedIn = true;
        state.userData = {...user }
    },
    initializeUserDecks(state, decks) {
        state.userData = {
            ...state.userData,
            decks
        }
    },
    logout(state) {
        state.isLoggedIn = false;
        state.userData = null;
        router.push('/login');
    }
}

const getters = {
    isUserLoggedIn: state => state.isLoggedIn,
    userData: state => state.userData,
    userToken: state => state.isLoggedIn ? state.userData.token : null,
    userDecks: (state, getters) => getters.userData.decks,
}

const user = {
    state: () => initialState,
    mutations,
    actions,
    getters
}

export default user;