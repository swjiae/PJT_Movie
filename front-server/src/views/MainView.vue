<template>
  <div>
    <h1>MainView</h1>
    <button @click="logOut">logOut</button>
    <div>
    <MovieList
    class="row d-flex"
    />
    </div>
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