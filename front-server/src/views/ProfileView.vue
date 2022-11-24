<template>
  <div>
    <nav>
      <hr>
      <router-link :to="{ name: 'MainView' }">Main</router-link>
      <hr>
    </nav>
    <div class="position-relative d-inline-block col-2 col-md-12 mr-3 mr-md-0 flex-shrink-0" style="z-index:4;">
      <img style="height:auto;" alt="" width="260" height="260" class="avatar avatar-user width-full border color-bg-default" :src="uploadImg">
      <div class="vcard-names-container float-left js-profile-editable-names col-12 py-3 js-sticky js-user-profile-sticky-fields" data-original-top="0px" style="position: sticky;">
        <h1 class="vcard-names ">
          <span class="p-name vcard-fullname d-block overflow-hidden" itemprop="name">
            <h1>{{ getUser.nickname }}</h1>
          </span>
          <span class="p-nickname vcard-username d-block" itemprop="additionalName">
            <h5>{{ getUser.email }}</h5>
          </span>
        </h1>
      </div>
    </div>
    <div>
      <ProfileReviewListVue
        class="row d-flex"
      />
    </div>

  </div>
</template>

<script>
// import ProfileUpdate from '@/components/ProfileUpdate'
import ProfileReviewListVue from '@/components/ProfileReviewList.vue'

export default {
    name: 'ProfileView',
    components: {
      // ProfileUpdate,
      ProfileReviewListVue,
    },
    computed: {
      getUser() {
        return this.$store.state.user
      },
      uploadImg() {
        if (!this.$store.state.user.profile_img) {
          return 'http://127.0.0.1:8000/media/profile_img/baekhyunjjang.jfif'
        }
        return this.$store.state.user.profile_img
      }
    }
}
</script>

<style>
</style>