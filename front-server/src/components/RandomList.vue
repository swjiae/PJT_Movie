<template>
  <div>
    {{this.random}}
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
        this.getrandomMovie()
        
        
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
        },
        getrandomMovie() {
            this.$store.state.movies.forEach((el) => {
                this.random.forEach((rel) => {
                    if (el.id === rel) {
                        this.randommovie.push(el)
                    }
                })
                // if (el.id in this.random) {
                //     this.randommovie.push(el)
                //     console.log('d')
                })

                }

                
            },
        test() {
        let arr1=[1,2,3,4,5]
        let arr2=[1,2]
            return console.log(arr1.filter(x=>arr2.includes(x)))
        },
        test2() {
            const abc = [2,3]
            if ('2' in abc) {
                console.log('yes')
        }else {
            console.log('d')
        }
      }
        }
      
      


        
        
</script>

<style>

</style>