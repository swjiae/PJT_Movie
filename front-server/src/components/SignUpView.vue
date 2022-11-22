<template>
  <div>
    <!-- <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="email">email : </label>
      <input type="email" id="email" v-model="email"><br>
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2"><br>
      
      <label for="nickname"> nickname : </label>
      <input type="text" id="nickname" v-model="nickname"><br>
      
      <label for="profile_img"> profile_img : </label>
      <input type="file" id="profile_img" multiple @change='inputImage()' ref="serveyImage"><br>
      <input type="submit" value="SignUp">
    </form> -->

     <b-button @click="modalShow = !modalShow" variant="warning">Signup</b-button>
    <b-modal v-model="modalShow" hide-footer >
      <div>
          <b-form @submit.prevent="signUp" @reset="onReset" v-if="show">
            <b-form-group
              id="input-group-1"
              label="Email address:"
              label-for="input-1"
              description="Please input your email-address"
            >
              <b-form-input
                id="input-1"
                v-model="form.email"
                type="email"
                placeholder="Enter email"
                required
              ></b-form-input>
            </b-form-group>

            <b-form @submit.stop.prevent>
              <label for="password1">Password</label>
              <b-form-input
              id="password1"
              v-model="form.password1"
              type="password"
              aria-describedby="password-help-block"
              ></b-form-input>
              <b-form-text id="password-help-block">
                good
              </b-form-text>
            </b-form>

            <b-form @submit.stop.prevent>
              <label for="password2"> password confirmation : </label>
              <b-form-input
              id="password2"
              v-model="form.password2"
              type="password"
              aria-describedby="password-help-block"
              ></b-form-input>
              <b-form-text id="password-help-block">
                good
              </b-form-text>
            </b-form>

            <b-form @submit.stop.prevent>
              <label for="nickname"> nickname : </label>
              <b-form-input
              id="nickname"
              v-model="form.nickname"
              type="text"
              description="Please input your nickname"
              ></b-form-input>
            </b-form>

            <b-form-file
              v-model="form.profile_img"
              :state="Boolean(form.profile_img)"
              placeholder="Choose a file or drop it here..."
              drop-placeholder="Drop file here..."
              ></b-form-file>
              <div class="mt-3">Selected file: {{ form.profile_img ? form.profile_img.name : '' }}</div>


            <b-button type="submit" variant="primary">Signup</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-form>
        </div>
      </b-modal>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      modalShow: false,
      form: {
        email: null,
        password1: null,
        password2: null,
        nickname: null,
        profile_img: null,
      },
      show: true
    }
  },
  methods: {
    inputImage() {
      this.form.profile_img = this.$refs.serveyImage.files
    },
    onReset(event) {
      event.preventDefault()
      this.form.email = ''
      this.form.password1 = ''
      this.form.password2 = ''
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    signUp() {
      const email = this.form.email
      const password1 = this.form.password1
      const password2 = this.form.password2
      const nickname = this.form.nickname
      const profile_img = this.form.profile_img
      const payload = {
        email: email,
        password1: password1,
        password2: password2,
        nickname: nickname,
        profile_img: profile_img[0],
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>