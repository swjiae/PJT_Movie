<template>
  <div id="app">
    <header>
      <a href="http://localhost:8080"><h1 style="font-family: 'Rubik Bubbles', cursive;" id="tweedles">TWEEDLES</h1></a>
      <b-button @click="logOut" v-if="this.$store.state.token">Logout</b-button> |
      <b-button v-if="this.$store.state.token"><router-link v-if="this.$store.state.token" :to="{ name: 'MainView' }" style="color:white">Main</router-link></b-button> |
      <b-button v-if="this.$store.state.token"><router-link v-if="this.$store.state.token" :to="{ name: 'ProfileView' }" style="color:white">Profile</router-link></b-button>
    </header>
    <body>
      <router-link :to="{ name: 'HomeView' }"></router-link>
      <router-view/>
    </body>
    <footer class="footer width-full container-xl p-responsive">
      <div class="position-relative d-flex flex-items-center pb-2 f6 color-fg-muted border-top color-border-muted flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap mt-6 pt-6">
        <div class="list-style-none d-flex flex-wrap col-0 col-lg-2 flex-justify-start flex-lg-justify-between mb-2 mb-lg-0">
          <div class="mt-2 mt-lg-0 d-flex flex-items-center">
            <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/swjiae/PJT_Tweedles">
              <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
                <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
              </svg>
              </a>        
              <span>
                   © 2022 Tweedles, SSAFY.
              </span>
          </div>
        </div>
        <nav aria-label="footer" class="col-12 col-lg-8">
          <ul class="list-style-none d-flex flex-wrap col-12 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">
              <p class="mr-3 mr-lg-0 service_tag"><a href="">Customer Service : 02) 4229-0388</a></p> |
              <p class="mr-3 mr-lg-0 service_tag"><a href="https://www.google.com/search?q=Google+is+the+best+teacher!&oq=Google+is+the+best+supporter!&aqs=chrome..69i57j0i30j69i64.8793j0j15&sourceid=chrome&ie=UTF-8">Technical Support</a></p> |
              <p class="mr-3 mr-lg-0 service_tag"><a href="https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp">Address : Samsung Gwangju global center</a></p> |
              <p class="mr-3 mr-lg-0 service_tag"><a href="https://edu.ssafy.com/edu/community/search/searchStudentList.do">Thanks to : Gwangju campus class-3 dongmudle </a></p> |
              <p class="mr-3 mr-lg-0 service_tag"><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com"></a></p>
              
          </ul>
        </nav>
      </div>

      <div class="d-flex flex-justify-center pb-6">
        <span class="f6 color-fg-muted"></span>
      </div>
    </footer>
  </div>
    
</template>

<script>
  export default {
    name: 'AppView',
    methods: {
      logOut() {
        this.$store.dispatch('logOut')
      },
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
  /* background-color: black;
  height: 1000vh; */
  /* width: 100% */
  /* width: 1000vw; */
}
nav {
  padding: 10px;
  margin-bottom: 20px;
}
nav a {
  font-weight: bold;
  color: #2c3e50;
}
nav a.router-link-exact-active {
  color: #42b983;
}
#tweedles {
  margin-top: 15px;
  color: crimson;
}
.service_tag{
  margin-left: 30px;
  margin-right: 30px;
}
</style>