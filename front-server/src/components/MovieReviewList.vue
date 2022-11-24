<template>
  <div>
    <h1>MovieReview</h1>
    <router-link :to="{ name: 'MovieReviewCreate', params: { id:movie?.id } }">[CREATE]</router-link>
    <MovieReviewListItem
      v-for="review in reviews"
      :key="review?.id"
      :review="review"
      :movie="movie"
    />
    <hr>
  </div>
</template>

<script>
  import MovieReviewListItem from '@/components/MovieReviewListItem'

  export default {
    name: 'MovieReviewList',
    components: {
      MovieReviewListItem,
    },
    props: {
      movie: Object
    },
    created() {
      this.$store.dispatch('getReviews')
    },
    computed: {
      reviews() {
        const reviews = this.$store.state.reviews.filter((review) => {
          return review.movie?.id == this.movie?.id
        })
        return reviews
      },
      // movieId() {
      //   return this.movie?.movie_id
      // }
    },
  }
</script>

<style>

</style>