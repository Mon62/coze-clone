import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'personal',
      component: () => import('../views/PersonalView.vue')
    },
    {
      path: '/space',
      name: 'Space',
      component: () => import('../views/SpaceView.vue')
    }
  ]
})

export default router
