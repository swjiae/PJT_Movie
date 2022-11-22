<template>
    <div>
      <h1>ReviewDetailView</h1>
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
    data() {
      return {
        movie: null,
        credits: [],
      }
    },
  }
  </script>
  
  <style>
  
  </style>