import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Management from '@/components/management/Management'
import VisitorList from '@/components/management/VisitorList'
import LandingPage from '@/components/landing_page/LandingPage'
import VisitorForm from '@/components/landing_page/VisitorForm'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/management',
      name: 'Management',
      component: Management
    },
    {
      path: '/management/:event_id/visitor_list',
      name: 'VisitorList',
      component: VisitorList
    },
    {
      path: '/',
      name: 'LandingPage',
      component: LandingPage
    },
    {
      path: '/landing_page/:event_id/register',
      name: 'VisitorForm',
      component: VisitorForm
    },
  ],
  mode: 'history'
})
