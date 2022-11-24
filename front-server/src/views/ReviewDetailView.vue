<template>
    <div>
      <h1>ReviewDetailView</h1>
      <button @click="deleteReview">DELETE</button><br>
      <button><router-link :to="{ name: 'MovieDetailView', parms:{ id: this.$route.params.id }}">뒤로가기</router-link></button>
      
      <b-card-img :src="url+getReview.movie.poster_path" alt="Image"
        class="rounded-0"
        style="height: 100px"
      ></b-card-img>

      {{ getReview }}


      <form @submit.prevent="changeLike">
          <input v-if="isLiked" type="submit" value="💖">
          <input v-if="!isLiked" type="submit" value="🤍">
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
        url : 'https://image.tmdb.org/t/p/original/',
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
        axios({
          method: 'delete',
          url: `${API_URL}/api/v1/reviews/${this.$route.params.review_id}/`,
          headers: {
            'Authorization': `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            console.log(res)
            this.$store.dispatch('getReviews')
            this.$router.push({ name: 'MovieDetailView', parms:{ id: this.$route.params.id }})
          })
          .catch((err) => {
            console.log(err)
          })
      },
      checkLiked() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/${this.$route.params.review_id}/review_likes/`,
          headers: {
            'Authorization': `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            this.isLiked = res.data.isLiked
            this.cntLike = res.data.cntLike
          })
          .catch((err) => {
            console.log(err)
          })
      },
      changeLike() {
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/${this.$route.params.review_id}/review_likes/`,
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