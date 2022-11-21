<template>
  <div>
    <p>{{ movie.poster_path }}</p>
    <h5>{{ movie.title }}</h5>
    <router-link :to="{ name: 'MovieDetailView', params: { id: movie.movie_id } }">
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
  }
}
</script>

<style>

</style>