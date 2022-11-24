<template>
  <div>
    <nav>
      <!-- <b-button @click="logOut" v-if="this.$store.state.token">Logout</b-button> -->
      <PreMainView v-if="!this.$store.state.token"/>
      <MainView v-if="this.$store.state.token"/>
    </nav>
  </div>
</template>

<script>
import PreMainView from '@/views/PreMainView'
import MainView from '@/views/MainView'


export default {
    name: 'HomeView',
    components: {
      PreMainView,
      MainView,
    },
    data() {
      return {
        loggedIn: false
      }
    },
    methods: {
    logOut() {
        this.$store.dispatch('logOut')
      },
    }
  }
</script>

<style>

</style>