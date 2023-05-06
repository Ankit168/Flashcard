import axios from "axios";
import { getUrl, headerConfig } from './utils';

export const loginReq = (username, password) => axios.post(
    getUrl('login'),
    JSON.stringify({
        username,
        password
    }),
    headerConfig(false)
)

export const userDeckReq = () => axios.get(getUrl('deck'), headerConfig())

export const addNewCardServiceRequest = (front, back, deckId) => {
    return axios.post(
            getUrl('card'),
            JSON.stringify({ front, back, deck_id: deckId }),
            headerConfig()
        )
        // const res = await fetch(
        //     "http://127.0.0.1:5000/card", {
        //         method: "POST",
        //         headers: {
        //             "Content-Type": "application/json",
        //             "Authorization": `Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0ODExODAwNCwianRpIjoiZDJlNzlmYjMtNjQwNS00MTNhLTk2MDEtOWYxMmUxNzFjM2M0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjQ4MTE4MDA0LCJleHAiOjE2NDgxMTg5MDR9.5aBs7FrtaLmy0yKjSAvMc3Y2OFiyebewwXJGhU9VK-E`
        //         },
        //         body: JSON.stringify({ front, back, deck_id })
        //     }
        // );
        // const data = await res.json();
        // console.log(data);
}


export const editDeckServiceRequest = (name, id) => {
    return axios.put(
        getUrl(`deck/${id}`),
        JSON.stringify({ deck_name: name }),
        headerConfig()
    )
}

export const deleteDeck = (id) => {
    console.log("in here")
    return axios.delete(
        getUrl(`deck/${id}`),
        headerConfig(),
    )
}

export const getCardsRequest = (id) => {
    return axios.get(
        getUrl(`deck/${id}/cards`),
        headerConfig(),
    )
}

export const addDeckRequest = name => {
    console.log(name);
    return axios.post(
        getUrl('deck'),
        JSON.stringify({ deck_name: name }),
        headerConfig(),
    )
}

export const updateScoreReq = (id, score) => {
    return axios.put(
        getUrl(`deck/${id}/updateScore`),
        JSON.stringify({ score }),
        headerConfig(),
    )
}