<template>
    <div class="p-6 max-w-md mx-auto">
      <h1 class="text-2xl font-bold mb-4">Register</h1>
      <form @submit.prevent="register">
          <input
            v-model="email"
            type="email"
            placeholder="Email"
            class="border p-2 w-full mb-2"
          />
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
          Register
        </button>
      </form>
      <p v-if="message" class="mt-2 text-green-600">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import { registerUser } from "../services/authService";
  
  export default {
    data() {
      return {
        email: "",
        username: "",
        password: "",
        message: "",
      };
    },
    methods: {
      async register() {
        try {
          await registerUser({ email: this.email, username: this.username, password: this.password });
          this.message = "Registration successful! You can now log in.";
        } catch (error) {
          console.error("Registration failed:", error.response.data);
        }
      },
    },
  };
  </script>
  