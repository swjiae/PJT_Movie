<template>
  <div>
    <h1>TWEEDLES</h1>
    <!-- Main Poster Randomly -->
    <MainList/>
    <!--  -->
  </div>
</template>

<script>
// @ is an alias to /src
import MainList from '../components/MainList'

export default {
  name: 'HomeView',
  components: {
    MainList
  },
  created() {
    this.getMainList()
  },
  methods: {
    getMainList() {
      this.$store.dispatch('getMainList')
    }
  }
}
</script>
