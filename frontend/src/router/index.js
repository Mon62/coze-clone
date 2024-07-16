import { createRouter, createWebHistory } from 'vue-router'
import { loadLayoutMiddleware } from './middleware'
import HomeView from '../views/HomeView/HomeView.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import NoneSidebarLayout from '../layouts/NoneSidebarLayout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/home' },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      meta: { layout: DefaultLayout }
    },
    {
      path: '/space/:spaceId',
      name: 'personal',
      component: () => import('../views/PersonalView/PersonalView.vue'),
      meta: { layout: DefaultLayout },
      children: [
        {
          path: 'bot',
          name: 'personal-bot',
          component: () => import('@/views/PersonalView/PersonalBotView.vue')
        },
        {
          path: 'knowledge',
          name: 'personal-knowledge',
          component: () => import('@/views/PersonalView/PersonalKnowledgeView.vue')
        }
      ]
    },
    {
      path: '/space',
      name: 'Space',
      component: () => import('../views/SpaceView.vue')
    },
    {
      path: '/space/upload',
      name: 'Upload',
      component: () => import('../views/UploadView.vue')
    }
  ]
})

router.beforeEach(loadLayoutMiddleware)

export default router
