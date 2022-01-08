//1.导入路由对象
// import Vue from 'vue'



import { createRouter, createMemoryHistory, createWebHistory } from 'vue-router'

const Ping = ()=>import('../components/Ping.vue')
const Book = ()=>import('../components/book.vue')
const history = isServer ? createMemoryHistory() : createWebHistory()
const isServer = typeof window === 'undefined'

const routes = [
    {
        path: '/',
        name: "books",
        component: Book
    },
    {
        path: '/Ping',
        name: "Ping",
        component: Ping
    }
]
const router = createRouter({
    history,
    routes
})
//钩子函数，路由改变前修改title
// router.beforeEach((to,from,next)=>{
//     window.document.title = to.meta.title;
//     next()
// })
export default router