<template>
  <div>
    {{ review.user }} <br>
    {{ review.title }} <br>
    {{ review.score }} <br>
    
    <router-link :to="{ name: 'ReviewDetailView', params: { id: review.review_id } }">
      [DETAIL]
    </router-link>
  </div>
</template>

<script>
export default {
    name: 'MovieReviewListItem',
    props: {
      review: Object
    },
}
</script>

<style>

</style>