<template>
  <div class="row">
    <div class="d-flex justify-content-center">
      <b-card no-body class="overflow-hidden" style="max-width: 50%; height:800px">
        <b-row no-gutters>
          <b-col md="7">
            <b-card-img :src="url+movie.poster_path" alt="Image"
            class="rounded-0"
            style="height: auto"
            @mouseover="activate"
            @mouseout="diactivate"
            v-b-modal.modal_trailer
            ></b-card-img>
          </b-col>
          <b-col md="5">
            <b-card-body :title="movie.title" class="d-flex row">
              <hr>
              <!-- 텍스트 일렬정렬하기 -->
              <div>
                <b-card-text>
                <li>{{movie.id}}</li>
                <li>평점 : {{movie.vote_avg}}</li>
                <li>개봉일 : {{movie.released_date}}</li>
                <li>장르 : {{genres}}</li>
                <li>줄거리 : {{movie.overview}}</li>
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
        url : 'https://image.tmdb.org/t/p/original/',
        youtube_url : 'https://www.youtube.com/embed/',
        movie: null,
        credits: [],
        genre_list: [],
        genres: [],
        trailer: null,
        trailer_key:null,
        trailer_url: null,
        isShow: false,
      }},
    created() {
      this.getAllDetail()
    },

    methods: {
      async getAllDetail() {
        const getdetail_res =  await axios.get(`${API_URL}/api/v1/movies/${this.$route.params.id}`)
        const detail = getdetail_res.data
        const genres = detail.genres
        this.movie = detail
        this.genre_list = genres
        // console.log('get_movie_detail')
        // console.log(detail)
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
        this.trailer = gettrailer_res.data
        this.trailer_key = this.trailer.key
        const trailer_url = this.youtube_url+this.trailer_key
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
    },
}
</script>

<style>
#trailer {
  position:absolute;
  z-index: 2;
}

</style>