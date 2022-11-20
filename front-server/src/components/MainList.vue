<template>
    <div>
        <h5>MainListItem</h5>
        <MainListItem
        v-for="movie in main_movielist"
        :key="movie.id"
        :movie="movie"
        />
        
    </div>
</template>

<script>
import MainListItem from '@/components/MainListItem'
export default {
    name: 'MainList',
    components: {
        MainListItem
    },
    computed: {
        main_movielist() {
            return this.$store.state.mainlist
        }
    }

}
</script>

<style>
.style {
    display: inline;
    font: sans-serif;
}

</style>