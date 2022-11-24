<template>
  <div>
    {{this.randommovie}}
  </div>
</template>

<script>
export default {
    name: 'RandomList',
    data() {
        return {
            random: null,
            randommovie: []

        }
    },
    computed: {
            movies() {
                return this.$store.state.movies
            },
            
            
        },
    mounted() {
        this.randomPick()
        // this.getrandomMovie()
        // this.getAllData()
        this.test()
        
        
    },
    methods: {
        async getAllData() {
            let f_randompick = this.randomPick()
            let f_getrandommovie = this.getrandomMovie()
            console.log('a')
            await f_randompick
            console.log('b')
            console.log(this.random)

            await f_getrandommovie
            console.log('c')
            console.log(this.randommovie)


            


        },
        randomPick() {
            var random_list=[]
            for (let i=1; i<=7; i+=1) {
                var random_number = Math.floor(Math.random()* this.$store.state.movies.length)
                random_list.push(random_number)
            }
            this.random = random_list
            console.log('h')
        },
        getrandomMovie() {
            this.$store.state.movies.forEach((el) => {
                console.log(el)
                console.log('d')
                if (el.id in this.randommovie) {
                    console.log(el)
                    this.randommovie.push(el)

                }
                
            })
        },
        test() {
            if (5 in [5,10]) {
                    console.log('잇다')
                }
        }


        }}
        
</script>

<style>

</style>