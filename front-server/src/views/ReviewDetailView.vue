<template>
    <div>
      <h1>ReviewDetailView</h1>
      <div class="container">
        <div class="row">
          <div class='col-2'></div>
          <button class='col-2'><router-link :to="{ name: 'MovieDetailView', parms:{ id: this.$route.params.id }}">뒤로가기</router-link></button>
          <div class='col-4'></div>
          <button class='col-2' @click="deleteReview">DELETE</button>
        </div>
      </div>

      <div class="container">
        <div class="bg-warning border border-warning bg-opacity-10 mt-3">
          <b-card-img :src="url+getReview.movie.poster_path" alt="Image"
            class="rounded-2"
            style="height: 300px; width: 200px; "
          ></b-card-img>
          <h2 class="mt-4">{{ getReview.movie.title}}</h2>
        </div>
        <!-- {{ getReview }} -->
        <div class="rounded-3 border border-danger mt-3 bg-danger bg-opacity-10">
          <h3>제목: {{getReview.title}}</h3>
          <div> 평점: {{getReview.score }}</div>
          <div> 닉네임: {{ getReview.nickname }}</div>
          <div> 내용: {{ getReview.content }}</div>
          <!-- <div>좋아요 한 사람들: {{ getReview.like_users }}</div> -->

        </div>
          <span>좋아요 : {{linkCntLike}}개</span>
          <form @submit.prevent="changeLike">
              <input v-if="isLiked" type="submit" value="💖">
              <input v-if="!isLiked" type="submit" value="🤍">
          </form>
          <hr>
          <ReviewCommentList
            :review="getReview"
          />
          <hr>

          <ReviewCommentCreate/>

        <div>
        </div>
      </div>
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