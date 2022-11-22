<template>
<div>
    <!-- <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="email">email : </label>
      <input type="email" id="email" v-model="email"><br>
      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>
      <input type="submit" value="logIn">
    </form> -->
  <b-button @click="modalShow = !modalShow" variant="primary">login</b-button>
    <b-modal v-model="modalShow" hide-footer >
      <div>
          <b-form @submit.prevent="logIn" @reset="onReset" v-if="show">
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
              <label for="text-password">Password</label>
              <b-form-input
              id="text-password"
              v-model="form.password"
              type="password"
              aria-describedby="password-help-block"
              ></b-form-input>
              <b-form-text id="password-help-block">
                Your password must be 8-20 characters long, contain letters and numbers, and must not
                contain spaces, special characters, or emoji.
              </b-form-text>
            </b-form>

            <b-button type="submit" variant="primary">Submit</b-button>
            <b-button type="reset" variant="danger">Reset</b-button>
          </b-form>
        </div>
      </b-modal>
</div>

</template>

<script>
  export default {
    name: 'LogInView',
    components: {
  },
    data() {
      return {
        modalShow: false,
        form: {
          email: null,
        password: null,
        },
        show: true
      }
    },
  methods: {
    // onSubmit(event) {
    //   event.preventDefault()
    //   alert(JSON.stringify(this.form))
    // },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.password = ''
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    logIn() {
      const email = this.form.email
      const password = this.form.password
      const payload = {
        email: email,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  },
  computed: {
    validation() {
      return this.userId.length > 4
    }
  },
  
  }
</script>

<style>
</style>