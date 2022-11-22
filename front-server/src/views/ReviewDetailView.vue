<template>
    <div>
      <h1>ReviewDetailView</h1>
      <button @click="deleteReview">DELETE</button><br>
      <router-link :to="{ name: 'ReviewDetailView' }">뒤로가기</router-link>
      {{ getReview }}
      <ReviewCommentCreate/>
      <ReviewCommentList
        :review="getReview"
      />
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
          return review.id == this.$route.params.id
        })
        return review
      }
    },
    methods: {
      deleteReview() {
        this.$store.commit('DELETE_REVIEW', this.getreview.id)
        this.$router.push({ name: 'ReviewDetailView' })
      },
    }
  }
  </script>
  
  <style>
  
  </style>