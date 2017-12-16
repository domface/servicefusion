import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/Index'
import create from '@/components/Create'
import contact from '@/components/ContactCard'



Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index,
      children: [
        {
          path: 'create',
          name: 'create',
          component: create
        }, {
          path: 'contact/:id',
          name: 'contact',
          component: contact,
          props: true,
          
        }


      ]
    }

  ]
})

