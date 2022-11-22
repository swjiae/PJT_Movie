<template>
  <div>
    <h1>MovieDetailView</h1>
    {{ movie }}
    <div v-if="credits.length">{{ credits }}</div>
    <MovieReviewList :movie="movie"/>
  </div>
</template>

<script>
import MovieReviewList from '@/components/MovieReviewList'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieDetailView',
    components: {
      MovieReviewList,
    },
    data() {
      return {
        movie: null,
        credits: [],
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