<template>
  <div>
    <!-- {{this.comedy}}
    {{this.$store.state.movies}} -->
  </div>
</template>

<script>
export default {
    name: 'ComedyList',
    data() {
        return {
            comedy: [],

        }
    },
    computed: {
            movies() {
                return this.$store.state.movies
            }
        },
    created() {
    this.ComedyGenre()
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
    }

        },
        
}
</script>

<style>

</style>