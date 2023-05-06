<template>
    <div>
        <div class="add-new">
            <h5 class="text-center">Add New Deck</h5>
            <form class="form-inline" @submit.prevent="addNewDeck">
                <div class="col-md-9">
                    <input type="text" class="form-control" placeholder="Deck name" v-model="name"/>
                </div>
                <div class="col-md-1">
                </div>
                <div class="col-md-2">
                <button type="submit" class="btn btn-primary"> Add </button>
                </div>
            </form>
        </div>
        <div class="row mt-5">
            <div class="col-md-4" v-for="deck in userDecks" :key="deck.id">
                <div class="vertical flip-container" ontouchstart="this.classList.toggle('hover');">
    
                    <div class="flipper">
                        <div class="front">
                            <div class="deck-name">{{ deck.name }}</div>
                        </div>
                        <div class="back">
    
                            <h6> Score: {{ deck['score'] }}</h6>
                            <h6> Last Reviewed at: <br> {{ deck['last_reviewed'] }}</h6>
    
                            <div class="button-group">
                                <router-link class="btn btn-outline-dark" :to="{name:'ReviewDeck', params: {id: deck.id}}">Review deck</router-link>
                                <router-link class="btn btn-outline-dark" :to="{name:'AddNewCard', params: {id: deck.id}}">Add Card</router-link>
                                <router-link class="btn btn-outline-dark" :to="{name:'EditDeck', params: {id: deck.id}}">Edit deck</router-link>
                                <button class="btn btn-outline-dark" @click="deleteSelectedDeck(deck.id)"> Delete Deck</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
    name: 'Dashboard',
    data() {
        return {
            userDecks: null,
            name: ''
        }
    },
    methods: {
        ...mapActions(['getUserDecks', 'deleteDeck', 'addDeck']),
        addNewDeck() {
            if (this.name) {
                this.addDeck(this.name).then(() => {
                    alert('Added');
                    this.name = '';
                    this.getUserDecks().then(decks => {
                    this.userDecks = decks;
                    })
                });
            } else {
                alert('Please enter the name');
            }
        },

        deleteSelectedDeck(id) {
            this.deleteDeck(id).then(() => {
                alert('Successfully deleted deck');
                this.getUserDecks().then(decks => {
                    this.userDecks = decks;
                })
            });
        }
    },
    mounted() {
        this.getUserDecks().then(decks => {
            this.userDecks = decks;
        })
    }
};
</script>

<style scoped>
.form-inline {
    display: flex;
}
.form-inline .form-group {
    flex: 1;
}

.flip-container {
    perspective: 1000px;
}

.flip-container,
.front,
.back {
    width: 240px;
    height: 320px;
}

/* flip speed goes here */

.flipper {
    transition: 0.6s;
    transform-style: preserve-3d;
    position: relative;
}

/* hide back of pane during swap */

.front,
.back {
    position: absolute;
    top: 0;
    left: 0;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    border: 5px solid black;
}

/* front pane, placed above back */

.front {
    text-align: center;
    z-index: 1;
    font-style: italic;
}

/* back, initially hidden pane */

.back {
    transform: rotateX(-180deg);
    animation: toFront 0.3s linear normal forwards;
    padding: 10px;
    text-align: center;
    background: darkred;
    color: white;
}

.vertical.flip-container {
    position: relative;
}

.vertical.flip-container:hover .back {
    animation-delay: 0.3s;
    animation: toBack 0.3s linear normal forwards;
}

@keyframes toBack {
    0% {
        z-index: 0;
    }
    100% {
        z-index: 1;
    }
}

@keyframes toFront {
    0% {
        z-index: 1;
    }
    100% {
        z-index: 0;
    }
}

.vertical.flip-container .flipper {
    transform-origin: 100% 160px;
    /* half of height */
}

.vertical.flip-container:hover .flipper {
    transform: rotateX(-180deg);
}

.button-group .btn {
    margin: 10px;
    padding: 10px;
    display: block;
    color: white;
    border: 1px solid white;
    width: 190px;
}

.col-md-4 {
    padding: 10px
}

.deck-name {
    border: solid;
    background-color: black;
    color: white;
    margin: 20px;
    width: 200px;
    height: 270px;
    text-align: center;
    vertical-align: middle;
    line-height: 200px;
    font-size: x-large;
    font-family: 'Times New Roman', Times, serif;
    font-style: italic;
    background: darkred;
    position: relative;
}

.deck-name,
.deck-name::before,
.deck-name::after {
    /* Styles to distinguish sheets from one another */
    box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.25);
    border: 1px solid black;
}

.deck-name::before,
.deck-name::after {
    content: "";
    position: absolute;
    height: 95%;
    width: 99%;
    background-color: grey;
}

.deck-name::before {
    right: 15px;
    top: 0;
    transform: rotate(-1deg);
    z-index: -1;
}

.deck-name::after {
    top: 5px;
    right: -5px;
    transform: rotate(1deg);
    z-index: -2;
}

.card {
    border: 1px solid black;
}

.add-new {
    width: 40%;
    padding: 20px;
    margin: 50px auto;
    border: 1px solid;
}
</style>
