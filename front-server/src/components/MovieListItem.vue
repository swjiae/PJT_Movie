<template>
<div class="col">
  <div>
    <b-card
      :title="movie.title"
      :img-src="posterPath"
      img-height=480px
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; height:650px"
      class="mb-2"
    >
      <!-- <b-card-text> -->
        <!-- {{ movie.overview }} -->
      <!-- </b-card-text> -->

      <b-button
      variant="primary"
      router-link
      tag="img"
      :to="{ name: 'MovieDetailView', params: { id: movieID } }"
      >Detail</b-button>
    </b-card>
  </div>

</div>
    
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
      },
      movieID() {
        return this.movie.id
      }
      }
    }
</script>

<style>
</style>