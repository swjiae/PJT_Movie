import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    mainlist: null,
  },
  getters: {
  },
  mutations: {
    GET_MAINLIST(state, mainlist) {
      state.mainlist = mainlist
      console.log(state.mainlist)
    }
  },
  actions: {
    getMainList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/mainmovies/`
      })
      .then((res) => {
        // console.log(context, res)
        // console.log(res)
        context.commit('GET_MAINLIST', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  modules: {
  }
})
