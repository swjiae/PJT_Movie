<template>
  <div id="app">
    <h1 style="font-family: 'Rubik Bubbles', cursive;" id="tweedles">TWEEDLES</h1>
    <nav>
      <router-link :to="{ name: 'PreMainView' }">PreMain</router-link> | 
      <router-link :to="{ name: 'MainView' }">Main</router-link> | 
      <router-link :to="{ name: 'ProfileView' }">Profile</router-link>
    </nav>
    <router-view/>
  </div>
</template>

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
</style>