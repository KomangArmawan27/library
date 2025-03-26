<template>
    <aside class="w-64 bg-gray-800 text-white p-4 h-full">
      <nav>
        <RouterLink v-if="isLibrarian" to="/dashboard" class="rounded-md block py-2 px-4 hover:bg-gray-700">Dashboard</RouterLink>
        <RouterLink to="/books" class="rounded-md block py-2 px-4 hover:bg-gray-700">Books</RouterLink>
        <RouterLink to="/borrowed-books" class="rounded-md block py-2 px-4 hover:bg-gray-700">My Borrowed Books</RouterLink>
        <RouterLink v-if="isLibrarian" to="/manage-books" class="rounded-md block py-2 px-4 hover:bg-gray-700">Manage Books</RouterLink>
        <button @click="logout" class="rounded-md mt-4 block w-full text-left py-2 px-4 hover:bg-red-700">Logout</button>
      </nav>
    </aside>
  </template>
  
  <script>
  export default {
    computed: {
      isLibrarian() {
        return localStorage.getItem("role") === "librarian";
      }
    },
    methods: {
      logout() {
        localStorage.removeItem("token");
        this.$router.push("/login");
      }
    }
  };
  </script>
  