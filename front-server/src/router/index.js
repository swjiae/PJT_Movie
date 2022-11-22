import Vue from 'vue'
import VueRouter from 'vue-router'
import PreMainView from '@/views/PreMainView'
import MainView from '@/views/MainView'
import ProfileView from '@/views/ProfileView'
import MovieDetailView from '@/views/MovieDetailView'
import MovieReviewCreate from '@/components/MovieReviewCreate'
import ReviewDetailView from '@/views/ReviewDetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/premain',
    name: 'PreMainView',
    component: PreMainView
  },
  {
    path: '/main',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/profile',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },
  {
    path: '/:id',
    name: 'MovieReviewCreate',
    component: MovieReviewCreate
  },
  {
    path: '/review/:id',
    name: 'ReviewDetailView',
    component: ReviewDetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
