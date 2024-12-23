import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ServicesView from '../views/ServiceView.vue'
import IdeefixView from '../views/IdeefixView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: "/services",
      name: "services",
      // component: () => import('../views/ServiceView.vue'),
      component: ServicesView,
    },
    {
      path: "/ideefix",
      name: "ideefix",
      component: IdeefixView,
    }
    // // {
    // //   path: '/about',
    // //   name: 'about',
    // //   // route level code-splitting
    // //   // this generates a separate chunk (About.[hash].js) for this route
    // //   // which is lazy-loaded when the route is visited.
    // //   component: () => import('../views/AboutView.vue'),
    // // },
  ],
})

export default router
