<template>
  <div>
    <h1>MainView</h1>
    <button @click="logOut">logOut</button>
    <MovieList
    v-for="movie in getMovies"
    :key=movie.id
    :movie=movie
    />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'


export default {
    name: 'MainView',
    components: {
      MovieList,
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