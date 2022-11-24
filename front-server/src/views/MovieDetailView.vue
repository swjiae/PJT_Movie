<template>
  <div class="row">
    <!-- {{ 뒤로가기 }} -->
    <button><router-link :to="{ name: 'MainView' }">BAEK</router-link></button>
    <div class="d-flex justify-content-center">
      <b-card no-body class="overflow-hidden" style="max-width: 50%; height:800px">
        <b-row no-gutters>
          <b-col md="7">
            <b-card-img :src="poster_PATH" alt="Image"
            class="rounded-0"
            style="height: auto"
            @mouseover="activate"
            @mouseout="diactivate"
            v-b-modal.modal_trailer
            ></b-card-img>
          </b-col>
          <b-col md="5">
            <b-card-body :title="Title" class="d-flex row">

              <hr>
              <!-- 좋아요 -->
              <form @submit.prevent="changeLike">
                  <input v-if="isLiked" type="submit" value="💖">
                  <input v-if="!isLiked" type="submit" value="🤍">
              </form>
              <span>좋아요 : {{linkCntLike}}개</span>
              <!-- 텍스트 일렬정렬하기 -->
              <div>
                <b-card-text>

                <!-- <li>{{movie.id}}</li> -->
                <li>평점 : {{vote_AVG}}</li>
                <li>개봉일 : {{released_Date}}</li>
                <li>장르 : {{genres}}</li>
                <li>줄거리 : {{Overview}}</li>

              </b-card-text>
              </div>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </div>

    <!-- 동영상팝업창으로 넣기 -->
    <div
    v-show="isShow"
    id="trailer">
    <b-embed
          type="iframe"
          aspect="16by9"
          :src="trailer_url"
          allowfullscreen
          width="80%" height="800px"
        ></b-embed>
    </div>
      <hr>
      <MovieReviewList :movie="this.movie"/>
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
        url : 'https://image.tmdb.org/t/p/original',
        youtube_url : 'https://www.youtube.com/embed/',
        movie: null,
        credits: [],
        genre_list: [],
        genres: [],
        trailer_url: null,
        isShow: false,
        isLiked: false,
        cntLike: null,
      }},
    created() {
      this.getAllDetail()
      this.checkLiked()
    },
    computed: {
      //template에서 movie.data를 불러오는데 delay가 발생 -> computed/ if-else문을 이용해 오류를 해결
      linkCntLike() {
        return this.cntLike
      },
      poster_PATH() {
        if (this.movie) {
          return this.url+ this.movie.poster_path
        } else {
          return console.log('plz wait for poster_path')
        }
      },
      Title() {
        if (this.movie) {
          return this.movie.title
        } else {
          return console.log('plz wait for title')
        }
      },
      vote_AVG() {
        if (this.movie) {
          return this.movie.vote_avg
        } else {
          return console.log('plz wait for vote_avg')
        }
      },
      Overview() {
        if (this.movie) {
          return this.movie.overview
        } else {
          return console.log('plz wait for overview')
        }
      },
      released_Date() {
        if (this.movie) {
          console.log(Array(this.movie.released_date))
          return this.movie.released_date
        } else {
          return console.log('plz wait for released_date')
        }
      },

    },
    methods: {
      // detail data가 있어야 이 페이지의 모든 요소를 띄울 수 있다.
      // 비동기의 특성상 먼저 실행되어 선행되야하는 값이 없는 경우에 오류가 뜨기 때문에
      // async ~ await 함수를 이용해 실행순서를 정해둔다
      async getAllDetail() {
        const getdetail_res =  await axios.get(`${API_URL}/api/v1/movies/${this.$route.params.id}`)
        const detail = getdetail_res.data
        const genres = detail.genres
        this.movie = detail
        this.genre_list = genres
        const getcredit_res = await axios.get(`${API_URL}/api/v1/credits/${this.$route.params.id}`)
        const credit = getcredit_res.data
        this.credits = credit
        this.test()
        const gettrailer_res = await axios.get(`${API_URL}/api/v1/trailer/${this.$route.params.id}`)
        const trailer_data = gettrailer_res.data
        const trailer_key = trailer_data.key
        const trailer_url = this.youtube_url+trailer_key
        this.trailer_url = trailer_url
      }
      ,
      activate() {
        this.isShow = true
      },
      diactivate() {
        this.isShow = false
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
#trailer {
  position:absolute;
  z-index: 2;
}
</style>