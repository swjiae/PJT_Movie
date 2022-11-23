<template>
  <div class="row">
    <!-- {{ movie }} -->
    <div class="d-flex justify-content-center">
      <b-card no-body class="overflow-hidden" style="max-width: 50%; height:800px">
        <b-row no-gutters>
          <b-col md="7">
            <b-card-img :src="url+movie.poster_path" alt="Image"
            class="rounded-0"
            style="height: auto"
            @mouseover="play_preview"
            ></b-card-img>
            <!-- <b-card-img :src="url+movie.poster_path" alt="Image"
            class="rounded-0"
            style="height: auto"
            ></b-card-img> -->
          </b-col>
          <b-col md="5">
            <b-card-body :title="movie.title">


              <form @submit.prevent="changeLike">
                  <input v-if="isLiked" type="submit" value="좋아요 취소">
                  <input v-if="!isLiked" type="submit" value="좋아요">
              </form>
              <span>좋아요 : {{linkCntLike}}개</span>


              <b-card-text>
                <li>평점 : {{movie.vote_avg}}</li>
                <li>개봉일 : {{movie.released_date}}</li>
                <li>
                줄거리 : {{movie.overview}}
                </li>
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </div>
    <hr>
    <MovieReviewList :movie="movie"/>

  </div>


</template>

<script>
import MovieReviewList from '@/components/MovieReviewList'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
    name: 'MovieDetailView',
    components: {
      MovieReviewList,
    },
    data() {
      return {
        movie: null,
        credits: [],
        url : 'https://image.tmdb.org/t/p/original/',
        isLiked: false,
        cntLike: null,
      }},
    created() {
      this.getMovieDetail()
      this.getMovieCredits()
      this.checkLiked()
    },
    computed: {
      linkCntLike() {
        return this.cntLike
      }
    },
    methods: {
      play_preview() {
      },
      getMovieDetail() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/movies/${this.$route.params.id}`
        })
        .then((res) => {
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      },
      getMovieCredits() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/credits/${this.$route.params.id}`
        })
        .then((res) => {
            this.credits = res.data
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      },
      checkLiked() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/${this.$route.params.id}/likes/`,
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
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/${this.$route.params.id}/likes/`,
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
    },
  }
</script>

<style>
</style>