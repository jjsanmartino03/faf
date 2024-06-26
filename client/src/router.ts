import {
    createRouter,
    createWebHistory,
    Router,
    RouteRecordRaw,
    RouterHistory,
    RouterView,
  } from "vue-router";  

  const Shell = () => import("./views/Shell.vue");

  const Login = () => import("./views/Login/Login.vue");
  const MatchList = () => import("./views/Match/Match-list.vue");
  
  const routes: RouteRecordRaw[] = [
    {
      path: "",
      component: Shell,
      redirect: "login",
      children: [
        {
          path: "login",
          component: RouterView,
          children: [
            { 
              path: "",
              component: Login,
              name: "login"
            }
          ]
        },
        {
          path: "matches",
          component: RouterView,
          children: [
            {
              path: "",
              component: MatchList,
              name: "matches"
            }
          ]
        }
      ]
    },
    { path: "/:catchAll(.*)", redirect: "/" },
  ];
  
  const history: RouterHistory = createWebHistory();
  
  const router: Router = createRouter({ history, routes });
  
  export default router;