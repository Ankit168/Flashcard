<template>
  <div id="app">
    <div v-if="isUserLoggedIn" class="header">
      <div class="header-content">
        <router-link :to="{name:'Dashboard'}">Home</router-link>
        <button class="btn btn-outline-light" @click="logout">Logout</button>
      </div>
    </div>
    <div class="main-content">
      <router-view/>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapMutations} from 'vuex';
export default {
  name: 'App',
  computed: {
    ...mapGetters(['isUserLoggedIn'])
  },
  methods: {
    ...mapMutations(['logout'])
  }
}
</script>

<style>
  a {
    text-decoration: none !important;
    color: white !important;
  }
</style>

<style scoped>
  .header {
    background: black;
    padding: 10px;
  }

  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .header-content, .main-content {
    width: 80%;
    margin: auto;
  }
</style>