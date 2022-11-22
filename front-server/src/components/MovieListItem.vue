<template>
  <div>
    <p>{{ movie.poster_path }}</p>
    <h5>{{ movie.title }}</h5>
    <router-link :to="{ name: 'MovieDetailView', params: { id: movieId } }">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>

  export default {
    name: 'MovieListItem',
    props: {
      movie: Object,
    },
    computed: {
      movieId() {
        return this.movie.movie_id
      }
    }
  }
</script>

<style>

</style>