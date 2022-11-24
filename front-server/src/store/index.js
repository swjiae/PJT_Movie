import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import createPersistedState from "vuex-persistedstate";
import router from "@/router";

Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: null,
    movies: [],
    reviews: [],
    comments: [],
    user: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false;
    },
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token;
      router.push({ name: "HomeView" });
    },
    DELETE_TOKEN(state) {
      state.token = null;
      router.push({ name: "HomeView" });
    },
    GET_MOVIES(state, movies) {
      state.movies = movies;
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews;
    },
    GET_COMMENTS(state, comments) {
      state.comments = comments;
    },
    GET_USER(state, user) {
      state.user = user;
    },
    DELETE_REVIEW(state, review_id) {
      state.reviews = state.reviews.filter((review) => {
        return !(review.id === review_id);
      });
    },
    REMOVE_REVIEWS(state) {
      state.reviews = [];
    },
  },
  actions: {
    signUp(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        headers: {
          "Content-Type": "multipart/form-data",
        },
        data: {
          email: payload.email,
          password1: payload.password1,
          password2: payload.password2,
          nickname: payload.nickname,
          profile_img: payload.profile_img,
        },
      }).then((res) => {
        context.commit("SAVE_TOKEN", res.data.key);
        context.dispatch("getUser");
      });
    },
    logIn(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          email: payload.email,
          password: payload.password,
        },
      }).then((res) => {
        context.commit("SAVE_TOKEN", res.data.key);
        context.dispatch("getUser");
      });
    },
    logOut(context) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      }).then(() => {
        context.commit("DELETE_TOKEN");
      });
    },
    getMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          context.commit("GET_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getReviews(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/reviews/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          context.commit("GET_REVIEWS", res.data);
        })
        .catch((err) => {
          context.commit("REMOVE_REVIEWS");
          console.log(err);
        });
    },
    getComments(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/comments/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          context.commit("GET_COMMENTS", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getUser(context) {
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          context.commit("GET_USER", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  modules: {},
});
