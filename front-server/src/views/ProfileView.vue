<template>
  <div>
    <h1>ProfileView</h1>
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
    }
}
</script>

<style>
</style>