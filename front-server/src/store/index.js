import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  state: {
    token: null,
    movies: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'MainView' })
    },
    DELETE_TOKEN(state) {
      state.token = null
      router.push({ name: 'PreMainView' })
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
  },
  actions: {
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        data: {
          email: payload.email,
          password1: payload.password1,
          password2: payload.password2,
          nickname: payload.nickname,
          profile_img: payload.profile_img,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          email: payload.email,
          password: payload.password,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logOut(context) {
      console.log(context.state.token)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        headers: {
          'Authorization': `Token ${context.state.token}`,
        },
      })
        .then(() => {
          context.commit('DELETE_TOKEN')
        })
    },
    getMovies(context) {
      console.log(context.state.token)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})