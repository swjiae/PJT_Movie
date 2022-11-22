<template>
  <div>
    <h1>MovieReview</h1>
    <router-link :to="{ name: 'MovieReviewCreate', params: { id:movie.movie_id } }">[CREATE]</router-link>
    <MovieReviewList/>
  </div>
</template>

<script>
import MovieReviewList from '@/components/MovieReviewList'

export default {
    name: 'MovieReview',
    components: {
      MovieReviewList
    },
    props: {
      movie: Object
    },
    computed: {
    }
}
</script>

<style>

</style>