import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

const routerOption = [
  { path: '/', component : 'Home'},
  { path: '/about', component: 'About'}
]

const routes = routerOption.map( route => {
    return {
      ...route,
      component: () => import( `@/components/${route.component}.vue`)
    }
})

Vue.use(Router)

/*
export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})*/

export default new Router({
  routes,
  mode: 'history'
})
