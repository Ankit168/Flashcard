<template>
    <div class="container mt-5 mb-5">
        <div class="row justify-content-center">
            <h2 class="text-center"> Update</h2>
            <h2 class="text-center" v-if="deck"> {{ deck.name }}</h2>
            <div class="card col-md-4 p-2">
                <form @submit.prevent="editDeck">
                    <div class="form-group">
                        <label for="front">New Name: </label>
                        <input type="text" class="form-control" placeholder="New Deck Name" name="front" v-model="newName">
                    </div>
                    <br>
                    <div class="d-flex justify-content-between">
                        <router-link class="btn btn-primary" :to="{name:'Dashboard'}">Go back to Decks </router-link>
                        <button type="submit" class="btn btn-primary active">Submit</button>
                    </div>
    
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex';
// import { addNewCardRequest } from '../services';
export default {
    name: 'EditDeck',
    data() {
        return {
            deck: null,
            newName: '',
        }
    },

    methods: {
        ...mapActions(['getDeckInfo', 'editDeckRequest']),
        editDeck() {
            this.editDeckRequest({
                name:this.newName,
                id: this.$router.currentRoute.params.id
            }).then(() => {
                this.deck.name = this.newName;
                this.newName = '';
                alert('Successfully Updated')
            })
        }
    },
    mounted() {
        this.getDeckInfo(this.$router.currentRoute.params.id).then(deck => {
            this.deck = deck;
        });
    },
};
</script>