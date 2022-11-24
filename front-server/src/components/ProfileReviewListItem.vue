<template>
  <div class="col">
  <div>
    <!-- <b-card no-body class="overflow-hidden" style="max-width: 50%; height:800px">
      <b-row no-gutters>
        <b-col md="7">
          <b-card-img :src="url+review.movie.poster_path" alt="Image"
          class="rounded-0"
          style="height: auto"
          ></b-card-img>
        </b-col>
        <b-col md="5">
          <b-card-body :title="review.movie.title" class="d-flex row">
            <b-card-text>
              {{ review.score }} <br>
              {{ review.title }}
            </b-card-text>
            <b-button
              variant="primary"
              router-link
              tag="img"
              :to="{ name: 'ReviewDetailView', params: { id: movieId, review_id: reviewId } }"
              >Detail</b-button>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card> -->
    <b-card
      :title="review.movie.title"
      :img-src="url+review.movie.poster_path"
      img-height=480px
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem; height:650px"
      class="mb-2"
    >
      <!-- <b-card-text> -->
        <!-- {{ movie.overview }} -->
      <!-- </b-card-text> -->

      <b-button
      variant="primary"
      router-link
      tag="img"
      :to="{ name: 'ReviewDetailView', params: { id: this.movieId, review_id: this.reviewId } }"
      >Detail</b-button>
    </b-card>
  </div>
</div>
</template>

<script>
export default {
    name: 'ProfileReviewListItem',
    props: {
      review: Object
    },
    data() {
      return {
        url : 'https://image.tmdb.org/t/p/original/',
      }
    },
    computed: {
      reviewId() {
        return this.review.id
      },
      movieId() {
        return this.review.movie.id
      }
    }
}
</script>

<style>
</style>