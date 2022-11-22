<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="email">email : </label>
      <input v-model="email"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2"><br>
      
      <label for="nickname"> nickname : </label>
      <input type="text" id="nickname" v-model="nickname"><br>
      
      <label for="profile_img"> profile_img : </label>
      <input type="file" id="profile_img" multiple @change='inputImage()' ref="serveyImage"><br>

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      email: null,
      password1: null,
      password2: null,
      nickname: null,
      profile_img: null,

    }
  },
  methods: {
    inputImage() {
      this.profile_img = this.$refs.serveyImage.files
    },
    signUp() {
      const email = this.email
      const password1 = this.password1
      const password2 = this.password2
      const nickname = this.nickname
      const profile_img = this.profile_img

      const payload = {
        email: email,
        password1: password1,
        password2: password2,
        nickname: nickname,
        profile_img: profile_img[0],
      }

      this.$store.dispatch('signUp', payload)
      this.$router.push({ name: 'MainView' })
    }
  }
}
</script>
