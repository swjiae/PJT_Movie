<template>
  <div class="row d-flex justify-content-center">

    <!-- <div>
      <div class="card mb-3" style="max-width: 540px;">
        <div class="g-0">
          <div class="col-md-4 col-lg-2 col-sm-2">
            <img :src="url+movie.poster_path" class="img-fluid rounded-start">
          </div>
          <div class="row col-md-8">
            <div class=" card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
              <p class="card-text">{{ movie.overview }}</p>
              <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
          </div>
        </div>
      </div> -->

    {{ movie }}
    {{ credits }}
    <!-- {{ movie.poster_path }} -->
    <!-- <img :src="url+movie.poster_path"> -->

    <MovieReview/>
  </div>
</template>

<script>
import MovieReview from '@/components/MovieReview'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
    name: 'MovieDetailView',
    components: {
      MovieReview,
    },
    data() {
      return {
        movie: null,
        credits: [],
        url : 'https://image.tmdb.org/t/p/original/',
        
      }
    },
    created() {
      this.getMovieDetail()
      this.getMovieCredits()
    },
    methods: {
      getMovieDetail() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
        })
          .then((res) => {
            this.movie = res.data
          })
          .catch((err) => {
            console.log(err)
          })
      },
      getMovieCredits() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/credits/${this.$route.params.id}`
        })
          .then((res) => {
            this.credits = res.data
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    }
}
</script>

<style>

</style>