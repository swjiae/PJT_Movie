<template>
  <div>
    <ReviewCommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script>
import ReviewCommentListItem from '@/components/ReviewCommentListItem'

export default {
    name: 'ReviewCommentList',
    components: {
      ReviewCommentListItem,
    },
    props: {
      review: Object
    },
    created() {
      this.$store.dispatch('getComments')
    },
    computed: {
      comments() {
        const comments = this.$store.state.comments.filter((comment) => {
          return comment.review == this.review.id
        })
        return comments
      },
    }
}
</script>

<style>

</style>