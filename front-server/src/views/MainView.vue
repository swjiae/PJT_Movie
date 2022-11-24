<template>
  <div>
    <nav>
      <hr>
      <router-link :to="{ name: 'ProfileView' }">Profile</router-link>
      <hr>
    </nav>
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
    }
}
</script>

<style>
</style>