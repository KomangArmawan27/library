<template>
    <MainLayout>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-blue-500 text-white p-6 rounded-lg shadow-lg">
          <h2 class="text-xl font-semibold">Total Books</h2>
          <p class="text-3xl">{{ totalBooks }}</p>
        </div>
        <div class="bg-green-500 text-white p-6 rounded-lg shadow-lg">
          <h2 class="text-xl font-semibold">Borrowed Books</h2>
          <p class="text-3xl">{{ borrowedBooks }}</p>
        </div>
        <div class="bg-yellow-500 text-white p-6 rounded-lg shadow-lg">
          <h2 class="text-xl font-semibold">Total Members</h2>
          <p class="text-3xl">{{ totalMembers }}</p>
        </div>
      </div>
    </MainLayout>
  </template>
  
  <script>
  import MainLayout from "../layout/MainLayout.vue";
  import { fetchDashboardStats } from "../services/dashboardService";
  
  export default {
    components: { MainLayout },
    data() {
      return {
        totalBooks: 0,
        borrowedBooks: 0,
        totalMembers: 0,
      };
    },
    async created() {
      const stats = await fetchDashboardStats();
      this.totalBooks = stats.total_books;
      this.borrowedBooks = stats.borrowed_books;
      this.totalMembers = stats.total_members;
    }
  };
  </script>
  