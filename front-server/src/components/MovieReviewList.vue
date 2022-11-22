<template>
  <div>
    <h1>MovieReviewList</h1>
    <router-link :to="{ name: 'MovieReviewCreate', params: { id:movie?.movie_id } }">[CREATEREVIEW]</router-link>
     <MovieReviewListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
    />
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
          console.log(review.movie)
          return review.movie == this.movie.movie_id
        })
        return reviews
      }
    },
  }
</script>

<style>

</style>