<template>
  <div>
    <h1>ProfileReviewList</h1>
    <ProfileReviewListItem
      v-for="review in reviews"
      :key="review.id"
      :review="review"
    />
  </div>
</template>

<script>
import ProfileReviewListItem from '@/components/ProfileReviewListItem'

export default {
    name: 'ProfileReviewList',
    components: {
      ProfileReviewListItem,
    },
    created() {
      this.$store.dispatch('getReviews')
    },
    computed: {
      reviews() {
        const reviews = this.$store.state.reviews.filter((review) => {
          console.log(this.$store.state.user.pk)
          return review.user == this.$store.state.user.pk
        })
        return reviews
      },
      
    },
  }
</script>

<style>

</style>