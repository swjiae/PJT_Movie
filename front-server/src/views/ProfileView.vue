<template>
  <div>
    <div>
      EMAIL : {{ getUser.email }} <br>
      NICKNAME : {{ getUser.nickname }} <br>
      profile : {{ getUser.profile_img }}
    </div>
    <ProfileUpdate/>
    <ProfileReviewList/>
  </div>
</template>

<script>
import ProfileUpdate from '@/components/ProfileUpdate'
import ProfileReviewList from '@/components/ProfileReviewList'
export default {
    name: 'ProfileView',
    components: {
      ProfileUpdate,
      ProfileReviewList,
    },
    computed: {
      getUser() {
        return this.$store.state.user
      }
    }
}
</script>

<style>
</style>