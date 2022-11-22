<template>
    <div>
      <h1>ReviewDetailView</h1>
      {{ getReview }}
      <ReviewCommentCreate/>
      <ReviewCommentList/>
    </div>
  </template>
  
  <script>
  import ReviewCommentCreate from '@/components/ReviewCommentCreate'
  import ReviewCommentList from '@/components/ReviewCommentList'
  

  export default {
    name: 'ReviewDetailView',
    components: {
      ReviewCommentCreate,
      ReviewCommentList,
    },
    computed: {
      getReview() {
        const review = this.$store.state.reviews.find((review) => {
          review.id == this.$route.params.id
        })
        console.log(review)
        return review
      }
    }
  }
  </script>
  
  <style>
  
  </style>