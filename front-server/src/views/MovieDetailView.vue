<template>
  <div class="container justify-content-center">
    <button class="rounded mt-5"><router-link :to="{ name: 'MainView' }">뒤로가기</router-link></button>
    <hr>
    <div class="row">
      <div class="d-flex col">
        <img :src="url+movie?.poster_path" alt="Image"
          class="rounded-0"
          style="height: 36rem"
          @mouseover="activate"
          @mouseout="diactivate"
          v-b-modal.modal_trailer
        />

        <div class="card bg-warning bg-opacity-10" style="width: 24rem;">
          <div class="card-body">
            <h5 class="card-title">{{movie?.title}}</h5>
            <hr>
            <form @submit.prevent="changeLike">
              <input v-if="isLiked" type="submit" value="💖">
              <input v-if="!isLiked" type="submit" value="🤍">
            </form>
            <span>좋아요 : {{linkCntLike}}개</span>
            <hr>
            <h6 class="card-subtitle mb-2 text-muted">평점 : {{movie?.vote_avg}}</h6>
            <h6 class="card-subtitle mb-2 text-muted">개봉일 : {{movie?.released_date}}</h6>
            <h6 class="card-subtitle mb-2 text-muted">장르 : {{genre}}</h6>
            <hr>
            <p class="card-text">{{movie?.overview}}</p>
          </div>
        </div>

        <div class="card bg-danger p-2 bg-opacity-10 mx-1" style="width: 24rem;">
          <MovieReviewList :movie="movie"/>
        </div>

      </div>
    </div>
    <!-- <div
      v-show="isShow"
      id="trailer">
      <b-embed
        type="iframe"
        aspect="16by9"
        :src="trailer_url"
        allowfullscreen
        width="80%" height="800px"
      ></b-embed> -->
    <!-- </div> -->
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
      genre() {
        let result = []
        this.genre_list.forEach((el) => {
          result.push(el.name)
        })
        return result
      }
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
        // const gettrailer_res = await axios.get(`${API_URL}/api/v1/trailer/${this.$route.params.id}`)
        // const trailer_data = gettrailer_res.data
        // const trailer_key = trailer_data.key
        // const trailer_url = this.youtube_url+trailer_key
        // this.trailer_url = trailer_url
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