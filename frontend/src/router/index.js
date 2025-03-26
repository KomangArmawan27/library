import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import DashboardView from "../views/DashboardView.vue";
import BookList from "../views/BookList.vue";
import BorrowedBooks from "../views/BorrowedBooks.vue";
import ManageBooks from "../views/ManageBooks.vue";

const routes = [
  { path: "/", name: "Home", component: HomeView },
  { path: "/login", name: "Login", component: LoginView },
  { path: "/register", name: "Register", component: RegisterView },
  { path: "/dashboard", name: "Dashboard", component: DashboardView, meta: { requiresAuth: true, requiresLibrarian: true } },
  { path: "/books", name: "Books", component: BookList, meta: { requiresAuth: true } },
  { path: "/borrowed-books", component: BorrowedBooks, meta: { requiresAuth: true } },
  { path: "/manage-books", component: ManageBooks, meta: { requiresAuth: true, requiresLibrarian: true } },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  router.beforeEach((to, from, next) => {
    const isAuthenticated = !!localStorage.getItem("token");
    const userRole = localStorage.getItem("role"); 
  
    if (to.meta.requiresAuth && !isAuthenticated) {
      next("/login");
    } else if (to.meta.requiresLibrarian && userRole !== "librarian") {
      next("/books  "); 
    } else {
      next();
    }
  });
  
  export default router;
