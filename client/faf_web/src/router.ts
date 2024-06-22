import {
  createRouter,
  createWebHistory,
  Router,
  RouteRecordRaw,
  RouterHistory,
  // RouterView,
} from "vue-router";

const Shell = () => import("./views/Shell.vue");
const Home = () => import("./views/Home.vue");
const Teams = () => import("./views/Teams.vue");

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
  {
    path: "/home",
    component: Home
  },
  {
    path: "/teams",
    component:  Teams
  },
  { path: "/:catchAll(.*)", redirect: "/" },
];

const history: RouterHistory = createWebHistory();

const router: Router = createRouter({ history, routes });

export default router;