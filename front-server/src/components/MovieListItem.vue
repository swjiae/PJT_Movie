<template>
  <!-- <div >
    <p>{{ movie.poster_path }}</p>
    <h5>{{ movie.title }}</h5>
    <router-link :to="{ name: 'MovieDetailView', params: { id: movie.movie_id } }">
      [DETAIL]
    </router-link> -->

    <div class="card" style="width: 18rem;">
      <img :src="posterPath" class="card-img-top" height="400px" >
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.overview }}</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
      </div>
    </div>

    <!-- </div> -->


</template>

<script>

export default {
    name: 'MovieListItem',
    props: {
      movie: Object,
  },
    data() {
      return {
        url : 'https://image.tmdb.org/t/p/original/'
      }
    },
    // created() {
    //   this.posterPath()
    // },

    computed: {
      posterPath() {
        return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
      }
    }
}
</script>

<style>

</style>