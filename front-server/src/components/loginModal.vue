<template>
    <div>
      <b-button @click="modalShow = !modalShow" variant="warning">login</b-button>
      <b-modal v-model="modalShow" hide-footer="true" >
        <div>
            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
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
                <b-form-input type="password" id="text-password" aria-describedby="password-help-block"></b-form-input>
                <b-form-text id="password-help-block">
                  Your password must be 8-20 characters long, contain letters and numbers, and must not
                  contain spaces, special characters, or emoji.
                </b-form-text>
              </b-form>

              <!-- <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }">
                <b-form-checkbox-group
                  v-model="form.checked"
                  id="checkboxes-4"
                  :aria-describedby="ariaDescribedby"
                >
                  <b-form-checkbox value="me">Check me out</b-form-checkbox>
                  <b-form-checkbox value="that">Check that out</b-form-checkbox>
                </b-form-checkbox-group>
              </b-form-group> -->

              <b-button type="submit" variant="primary">Submit</b-button>
              <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
            <!-- <b-card class="mt-3" header="Form Data Result">
              <pre class="m-0">{{ form }}</pre>
            </b-card> -->
          </div>
        </b-modal>
    </div>
  </template>
  
  <script>
    export default {
      name: 'loginModal',
      data() {
        return {
          modalShow: false,
          form: {
          email: '',
          password: '',
        },
        show: true
        }
      },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.password = ''
        //this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    },
    computed: {
      validation() {
        return this.userId.length > 4
      }
    }
    }
  </script>