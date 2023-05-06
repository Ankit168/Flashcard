<template>
    <div class="container mt-5 mb-5" id="review-container">
        <div class="row justify-content-center">
            <div v-if="noCards" class="text-center">
                <h2>No cards have been added yet to deck </h2>
                <button type="button" class="btn btn-outline-secondary">
                    <router-link :to="{name:'AddNewCard', params: {id: deckId}}">Add Card</router-link>
                </button>
            </div>
            <h2 class="text-center" v-else> Review Cards </h2>
            <div v-for="(card, index) in cards" :key="card.id" class="cards-container">
                <div class="card col-md-4" v-if="activeCardId === card.id">
                    <div class="vertical flip-container" ontouchstart="this.classList.toggle('hover');">
                        <div class="flipper">
                            <div class="front">
                                <div class="" id="front">{{card.front}}</div>
                            </div>
                            <div class="back">
                                <div id="back">{{card.back}}</div>
                            </div>
                        </div>
                    </div>
    
                    <div class="submit-action">
                        <form>
                            <div>
                                <label class="radio-inline">
                                    <input type="radio" name="score" id="easy" value=2 v-model="selectedScore">
                                    EASY
                                </label>
        
                                <label class="radio-inline">
                                    <input type="radio" name="score" id="medium" value=3 v-model="selectedScore">
                                    MEDIUM
                                </label>
        
                                <label class="radio-inline">
                                    <input type="radio" name="score" id="hard" value=5 v-model="selectedScore">
                                    HARD
                                </label>
                            </div>
                            <div class="submit-btns">
                                <button class="btn btn-light" id="submit-score" @click.prevent="initUpdateScore()"> Update Score </button>
                                <button class="btn btn-light" @click.prevent="next(index+1)">Next</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
    name: 'ReviewDeck',
    data() {
        return {
            cards: [],
            activeCardId: null,
            noCards: false,
            deckId: null,
            selectedScore: 2,
            score: 0
        }
    },
    methods: {
        ...mapActions(['getCards', 'updateScore']),
        initUpdateScore() {
            this.updateScore({id:this.deckId, score:this.score}).then(() => {
                alert('Score updated');
            })
        },
        next(index) {
            if (this.cards[index]) {
                this.activeCardId = this.cards[index].id;    
                this.score = this.score + parseInt(this.selectedScore)
                this.selectedScore = 2
            } else {
                this.score = this.score + parseInt(this.selectedScore) // to add thhe score of last card
                alert('No more cards for this deck!');
            }
        }
    },
    mounted() {
        this.deckId = this.$router.currentRoute.params.id;
        this.getCards(this.$router.currentRoute.params.id).then(cards => {
            this.noCards = false;
            if (cards.data && cards.data.length) {
                this.cards = cards.data;
                this.activeCardId = this.cards[0].id;
            } else {
                this.noCards = true;
            }
        });
    },
};
</script>

<style scoped>
a {
    color: black !important;
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
    border: 10px solid black;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2em;
    text-transform: capitalize;
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

.cards-container {
    display: flex;
    justify-content: center;
}

.card {
    background-image: url('http://localhost:8080/background.jpeg');
    background-size: cover;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 50px 0 0 0;
}

.submit-action {
    width: 100%;
    padding: 20px 0 30px 0;
    background: #00000070;
    color: white;
    margin-top: 10px;
}

.submit-action > form > div {
    display: flex;
    justify-content: space-around;
}

.submit-action > form > .submit-btns {
    justify-content: space-between;
    margin: 10px;
}

</style>
