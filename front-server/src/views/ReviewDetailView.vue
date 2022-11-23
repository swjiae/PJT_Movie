<template>
    <div>
      <h1>ReviewDetailView</h1>
      <button @click="deleteReview">DELETE</button><br>
      <button><router-link :to="{ name: 'MovieDetailView', parms:{ id: this.$route.params.id }}">뒤로가기</router-link></button>
      {{ getReview }}


      <form @submit.prevent="changeLike">
          <input v-if="isLiked" type="submit" value="좋아요 취소">
          <input v-if="!isLiked" type="submit" value="좋아요">
      </form>
      <span>좋아요 : {{linkCntLike}}개</span>


      <ReviewCommentCreate/>
      <ReviewCommentList
        :review="getReview"
      />
    </div>
  </template>
  
  <script>
  import ReviewCommentCreate from '@/components/ReviewCommentCreate'
  import ReviewCommentList from '@/components/ReviewCommentList'
  
  import axios from 'axios'
  const API_URL = 'http://127.0.0.1:8000'

  export default {
    name: 'ReviewDetailView',
    components: {
      ReviewCommentCreate,
      ReviewCommentList,
    },
    data() {
      return {
        isLiked: false,
        cntLike: null,
      }
    },
    created() {
      this.checkLiked()
    },
    computed: {
      getReview() {
        const review = this.$store.state.reviews.find((review) => {
          return review.id == this.$route.params.review_id
        })
        return review
      },
      linkCntLike() {
        return this.cntLike
      }
    },
    methods: {
      deleteReview() {
        this.$store.commit('DELETE_REVIEW', this.getreview.id)
        this.$router.push({ name: 'ReviewDetailView' })
      },
      checkLiked() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/${this.$route.params.review_id}/likes/`,
          headers: {
            'Authorization': `Token ${this.$store.state.token}`,
          },
        })
        .then((res) => {
          console.log(`res.data.isLiked ${res.data}`)
          this.isLiked = res.data.isLiked
          this.cntLike = res.data.cntLike
        })
        .catch((err) => {
          console.log(err)
        })
      },
      changeLike() {
        console.log(this.$route.params.review_id, '-------------')
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/${this.$route.params.review_id}/likes/`,
          headers: {
            'Authorization': `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.isLiked=res.data.isLiked
            this.cntLike=res.data.cntLike
            console.log(this.isLiked)
          })
          .catch((err) => {
            console.log(err)
          })
      },
    }
  }
  </script>
  
  <style>
  
  </style>