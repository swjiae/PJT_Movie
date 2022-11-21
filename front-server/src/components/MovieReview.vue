<template>
  <div>
    <h1>MovieReview</h1>
    <MovieReviewCreate/>
    <MovieReviewList/>
  </div>
</template>

<script>
import MovieReviewCreate from '@/components/MovieReviewCreate'
import MovieReviewList from '@/components/MovieReviewList'

export default {
    name: 'MovieReview',
    components: {
      MovieReviewCreate,
      MovieReviewList
    }
}
</script>

<style>

</style>