<template>
  <div>
    {{ review.nickname }} <br>
    {{ review.title }} <br>
    {{ review.score }} <br>
    
    <router-link :to="{ name: 'ReviewDetailView', params: { id: reviewId } }">
      [DETAIL]
    </router-link>
  </div>
</template>

<script>
export default {
    name: 'MovieReviewListItem',
    props: {
      review: Object
    },
    data() {
      return {
        user: this.$store.state.user
      }
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