<template>
  <div>
    {{ comment.nickname}}:
    {{ comment.content }}
  </div>
</template>

<script>
export default {
    name: 'ReviewCommentListItem',
    props: {
      comment: Object
    }
}
</script>

<style>

</style>