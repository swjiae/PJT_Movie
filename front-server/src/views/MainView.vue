<template>
  <div>
    <div>
    <!-- <RandomList/> -->
    <MovieList
    class="row d-flex"
    />
    <!-- <ComedyList/> -->
    </div>
</div>

</template>

<script>
import MovieList from '@/components/MovieList'
// import RandomList from '@/components/RandomList'
// import ComedyList from '@/components/ComedyList'
export default {
    name: 'MainView',
    components: {
      MovieList,
      // RandomList,
      // ComedyList
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
      },

    }
}
</script>

<style>
</style>