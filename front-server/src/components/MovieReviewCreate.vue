<template>
  <div>
    <h3>감상평을 자유롭게 남겨보세요!</h3>
    <div class="container text-start border rounded p-3">
      <form @submit.prevent="createReview">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">제목</label>
          <input type="text" class="form-control" id="exampleInputEmail1" v-model.trim="title" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">평점</label>
          <input v-model.trim="score" type="number" class="form-control" id="exampleInputPassword1">
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">내용</label>
          <textarea  v-model="content" class="form-control" id="exampleInputPassword1"></textarea>
        </div>
        <button type="submit" class="btn btn-outline-info">감상평 작성</button>
      </form>
    </div>


    <!-- <form @submit.prevent="createReview">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="score">평점 : </label>
      <input type="number" id="score" v-model.trim="score"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form> -->
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieReviewCreate',
    data() {
      return {
        title: null,
        score: 0,
        content: null,
      }
    },
    methods: {
      createReview() {
        const title = this.title
        const score = this.score
        const content = this.content
        const nickname = this.$store.state.user.nickname
        if (!title) {
          alert('제목을 입력해주세요')
          return
        } else if (!score) {
          alert('평점을 입력해주세요')
          return
        } else if (!content) {
          alert('내용을 입력해주세요')
          return
        }
        console.log(this.$route.params.id)
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/movies/${this.$route.params.id}/reviews/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
          data: {
            title: title,
            score: score,
            content: content,
            nickname: nickname,
          },
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'MovieDetailView', parmas: { id:this.$route.params.id }})
          })
          .catch((err) => {
            console.log(err)
          })
      },
    }
  }
</script>

<style>

</style>