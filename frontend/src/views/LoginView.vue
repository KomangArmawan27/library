<template>
    <div class="p-6 max-w-md mx-auto">
      <h1 class="text-2xl font-bold mb-4">Login</h1>
      <form @submit.prevent="login">
        <input
          v-model="username"
          type="text"
          placeholder="Username"
          class="border p-2 w-full mb-2"
        />
        <input
          v-model="password"
          type="password"
          placeholder="Password"
          class="border p-2 w-full mb-2"
        />
        <button type="submit" class="bg-blue-600 text-white px-4 py-2 w-full">
          Login
        </button>
      </form>
      <p v-if="errorMessage" class="mt-2 text-red-600">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import { loginUser } from "../services/authService";
  
  export default {
    data() {
      return {
        username: "",
        password: "",
        errorMessage: "",
      };
    },
    methods: {
      async login() {
        try {
          const response = await loginUser({
            username: this.username,
            password: this.password,
          });
          localStorage.setItem("token", response.data.access);
          localStorage.setItem("role", response.data.role);
          if (localStorage.getItem("role") === "librarian") {
            this.$router.push("/dashboard").then(() => {
              location.reload();
            });
          } else {
            this.$router.push("/books").then(() => {
              location.reload();
            });
          }
        } catch (error) {
          this.errorMessage = "Invalid credentials";
        }
      },
    },
  };
  </script>
  