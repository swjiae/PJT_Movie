<template>
  <div>
    <h1>MovieReviewList</h1>
    <MovieReviewListItem/>
  </div>
</template>

<script>
import MovieReviewListItem from '@/components/MovieReviewListItem'

export default {
    name: 'MovieReviewList',
    components: {
      MovieReviewListItem,
    }
}
</script>

<style>

</style>