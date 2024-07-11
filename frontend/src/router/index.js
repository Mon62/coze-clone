import { createRouter, createWebHistory } from 'vue-router'
import { loadLayoutMiddleware } from './middleware'
import HomeView from '../views/HomeView.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      meta: {layout: DefaultLayout}
    },
    {
      path: '/space/:userId/bot',
      name: 'personal',
      component: () => import('../views/PersonalView.vue'),
      meta: {layout: DefaultLayout}
    }
  ]
})

router.beforeEach(loadLayoutMiddleware);

export default router
