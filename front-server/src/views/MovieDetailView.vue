<template>
  <div class="row">
    <!-- {{ 뒤로가기 }} -->
    <div class="d-flex justify-content-center row">
    <router-link :to="{ name: 'MainView' }"><b-icon icon="arrow-left" animation="cylon" variant="dark" style="width:15px"></b-icon></router-link>
    </div>

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
                  <input v-if="isLiked" type="submit" value="좋아요 취소">
                  <input v-if="!isLiked" type="submit" value="좋아요">
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
      async getAllDetail() {
        const getdetail_res =  await axios.get(`${API_URL}/api/v1/movies/${this.$route.params.id}`)
        const detail = getdetail_res.data
        const genres = detail.genres
        // console.log('get_movie_detail')
        // console.log(detail)
        this.movie = detail
        this.genre_list = genres
        // console.log('genre')
        // console.log(this.genre_list)
        const getcredit_res = await axios.get(`${API_URL}/api/v1/credits/${this.$route.params.id}`)
        const credit = getcredit_res.data
        this.credits = credit
        // console.log('getcredit_res')
        // console.log(credit)
        this.test()
        const gettrailer_res = await axios.get(`${API_URL}/api/v1/trailer/${this.$route.params.id}`)
        // console.log('trailer')
        const trailer_data = gettrailer_res.data
        const trailer_key = trailer_data.key
        const trailer_url = this.youtube_url+trailer_key
        this.trailer_url = trailer_url
        // console.log('trailer_url')
        // console.log(this.trailer_url)
      }
      ,
        test() {
          this.genre_list.forEach((el) => {
            this.genres.push(el.name)
          })
        },
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