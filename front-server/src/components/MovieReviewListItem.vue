<template>
  <div>
    <h1>MovieReviewListItem</h1>
    <ReviewCommentList/>
  </div>
</template>

<script>
import ReviewCommentList from '@/components/ReviewCommentList'

export default {
    name: 'MovieReviewListItem',
    components: {
      ReviewCommentList
    }
}
</script>

<style>

</style>