import {
    createRouter,
    createWebHistory,
    Router,
    RouteRecordRaw,
    RouterHistory,
    // RouterView,
  } from "vue-router";  

  const Shell = () => import("./views/Shell.vue");
  
  const routes: RouteRecordRaw[] = [
    {
      path: "",
      component: Shell,
      // beforeEnter: authGuard,
      // redirect: "login",
      children: [
        //Rutas hijas del shell
      ]
    },
    { path: "/:catchAll(.*)", redirect: "/" },
  ];
  
  const history: RouterHistory = createWebHistory();
  
  const router: Router = createRouter({ history, routes });
  
  export default router;