<template>
    <div>
      <form @submit.prevent="createComment">
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
        <input type="submit" id="submit">
      </form>
    </div>
  </template>
  
<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewCommentCreate',
  data() {
    return {
      content: null,
    }
  },
  methods: {
    createComment() {
      const content = this.content
      const nickname = this.$store.state.user.nickname
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/reviews/${this.$route.params.id}/comments/`,
        data: {
          content: content,
          nickname: nickname,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.content = null
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>