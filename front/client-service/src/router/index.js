import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Register from '@/components/Register'
import UserBoard from '@/components/UserBoard'
Vue.use(VueRouter)

const routes = [ 
    {
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
        meta: { 
            guest: true
        }
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
        meta: { 
            guest: true
        }
    },
    {
        path: '/dashboard',
        name: 'userboard',
        component: UserBoard,
        meta: { 
            requiresAuth: true
        } 
    }
    // }
   
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
