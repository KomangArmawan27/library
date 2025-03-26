<!-- src/components/Navbar.vue -->
<template>
  <nav class="p-4 bg-gray-800 text-white flex justify-between items-center shadow-md">
    <div class="flex gap-6">
      <router-link to="/" class="hover:text-gray-300 transition">Home</router-link>
      <router-link to="/books" class="hover:text-gray-300 transition" v-if="isAuthenticated">Books</router-link>
      <router-link to="/dashboard" class="hover:text-gray-300 transition" v-if="isAuthenticated && role === 'librarian'" >Dashboard</router-link>
    </div>

    <div class="flex gap-4">
      <router-link to="/login" class="hover:text-gray-300 transition" v-if="!isAuthenticated">Login</router-link>
      <router-link to="/register" class="hover:text-gray-300 transition" v-if="!isAuthenticated">Register</router-link>
      <button 
        @click="logout" 
        v-if="isAuthenticated" 
        class="bg-red-500 px-4 py-2 rounded-md text-white hover:bg-red-600 transition"
      >
        Logout
      </button>
    </div>
  </nav>
</template>

<script>
import { ref, watchEffect } from "vue";
import { logoutUser } from "../services/authService"; // Import logout service

export default {
  setup() {
    const isAuthenticated = ref(!!localStorage.getItem("token"));
    const role = localStorage.getItem("role");

    const logout = () => {
      logoutUser();
      isAuthenticated.value = false;
      window.location.href = "/dashboard"; // Redirect after logout
    };

    watchEffect(() => {
      isAuthenticated.value = !!localStorage.getItem("token");
    });

    return { isAuthenticated, role, logout };
  },
};
</script>
