<template>
  <div>
    {{ review.nickname }} <br>
    {{ review.title }} <br>
    {{ review.score }} <br>
    
    <router-link :to="{ name: 'ReviewDetailView', params: { id: movieId, review_id: reviewId } }">
      [DETAIL]
    </router-link>
  </div>
</template>

<script>
export default {
    name: 'MovieReviewListItem',
    props: {
      movieId: String,
      review: Object,
    },
    computed: {
      reviewId() {
        return this.review.id
      }
    }
  }
</script>

<style>

</style>