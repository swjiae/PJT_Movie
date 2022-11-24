<template>
  <div class="margin:10px;">
    <h1>Review</h1>
    <router-link :to="{ name: 'MovieReviewCreate', params: { id:movieId } }">[CREATEREVIEW]</router-link>
     <MovieReviewListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
      :movieId="movieId"
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
          return review.movie == this.movie?.movie_id
        })
        return reviews
      },
      movieId() {
        return this.movie?.movie_id
      }
    },
  }
</script>

<style>

</style>