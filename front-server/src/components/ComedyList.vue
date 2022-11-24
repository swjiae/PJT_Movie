<template>
  <div>
    <!-- {{this.poster_URL}} -->
    <!-- {{comedy}} -->
    <div class="container">
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
        img-width="50px"
        img-height="1vh"

      >
          <b-carousel-slide
            v-for="(path,i) in this.poster_path"
            :key=i
            :img-src="path"
          ></b-carousel-slide>
      </b-carousel>

    </div>

    <!-- {{this.poster_URL}} -->


    <!-- <Carousel
    v-if="this.poster_path"
    :autoplay="true"
    :loop="true"
    :center="true"
    :nav="false"
    :margin="5"
    >
      <img
        v-for="(path,i) in this.poster_path"
        :key="i"
        :src="path"
        width="446"
        height="446"
        @click="showSingle(path)"
      />
    </Carousel> -->

    <!-- <p class="mt-4">
      Slide #: {{ slide }}<br>
      Sliding: {{ sliding }}
    </p> -->


  </div>
</template>

<script>
// import Carousel from 'vue-carousel'
export default {
    name: 'ComedyList',
    data() {
        return {
            comedy: [],
            url : 'https://image.tmdb.org/t/p/original',
            poster_path: [],
            slide: 0,
            sliding: null

        }
    },
    components: {
      // Carousel,
    },
    computed: {
            movies() {
                return this.$store.state.movies
            },
            // poster_URL() {
            //   this.comedy.forEach((el) => {
            //     const pp = el.poster_path
            //     const path = this.url+pp
            //     this.poster_path.push(path)
            //   });
            //   return this.poster_path
            // }
        },
    created() {
    this.ComedyGenre()
    this.poster_URL()
    },
    methods: {
      ComedyGenre() {
      return this.movies.filter((movie) => {
        for (let i=0; i<movie.genres.length; i++) {
          if(movie.genres[i].name == '코미디') {
            this.comedy.push(movie)
            return this.comedy
              }
            }
          })
        },
      poster_URL() {
            this.comedy.forEach((el) => {
              const pp = el.poster_path
              const path = this.url+pp
              this.poster_path.push(path)
            });
            return this.poster_path
          },
      onSlideStart(slide) {
        console.log(slide)
          this.sliding = true
      },
      onSlideEnd(slide) {
        console.log(slide)
        this.sliding = false
      },


        },
        
}
</script>

<style>
#carousel-1 {
  height:5vh;
}
</style>