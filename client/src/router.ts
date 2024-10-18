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
const Home = () => import("./views/Home.vue");
const Teams = () => import("./views/teams/TeamsList.vue");
const Team = () => import("./views/teams/Team.vue");
const Category = () => import("./views/teams/Category.vue");
const Player = () => import("./views/players/Player.vue");
const CrossList = () => import("./views/crosses/CrossList.vue");

const routes: RouteRecordRaw[] = [
  {
    path: "",
    component: Shell,
    redirect: "/login",
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
            component: CrossList,
            name: "matches"
          }
        ]
      },
      {
        path: "home",
        component: Home,
        name: "home"
      },
      {
        path: "teams",
        children: [
          {
            path: "",
            component: Teams,
            name: "teams"
          },
          {
            path: ":id",
            component: Team
          },
          {
            path: ":teamId/categories/:categoryId",
            component: Category
          },
          {
            path: ":teamId/categories/:categoryId/players/:playerId",
            component: Player
          }
        ]
      }
    ]
  },
  {path: "/:catchAll(.*)", redirect: "/"},
];

const history: RouterHistory = createWebHistory();

const router: Router = createRouter({history, routes});

export default router;