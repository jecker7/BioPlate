import Vue from 'vue';
import Router from 'vue-router';
import BioPlate from '@/components/BioPlate';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'BioPlate',
      component: BioPlate,
    },
  ],
});
