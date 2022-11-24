<template>
  <div>
    <h1>MainView</h1>
    <b-button @click="logOut">logOut</b-button>
    <ComedyList/>
    <RandomList/>
    <div>
    <MovieList
    class="row d-flex"
    />
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
import ComedyList from '@/components/ComedyList'
import RandomList from '@/components/RandomList'

export default {
    name: 'MainView',
    components: {
      MovieList,
      ComedyList,
      RandomList
    },
    created() {
      this.getMovies()
    },
    methods: {
      getMovies() {
        this.$store.dispatch('getMovies')
      },
      logOut() {
        this.$store.dispatch('logOut')
      }
    }
}
</script>

<style>
</style>