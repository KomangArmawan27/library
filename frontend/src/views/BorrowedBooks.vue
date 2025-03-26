<template>
    <MainLayout>
        <div class="max-w-5xl mx-auto p-6">
        <h1 class="text-2xl font-semibold mb-6">📚 Borrowed Books</h1>
    
        <div v-if="loading" class="text-gray-500">Loading borrowed books...</div>
        <div v-else-if="message" class="text-gray-500">{{ message }}</div>
    
        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div v-for="book in books" :key="book.id" class="bg-white p-4 rounded-lg shadow-lg">
            <h2 class="text-xl font-bold">{{ book.title }}</h2>
            <p class="text-gray-700">Author: <span class="font-medium">{{ book.author }}</span></p>
            <p class="text-gray-500">Borrowed On: {{ formatDate(book.created_at) }}</p>
    
            <button
                @click="returnBook(book.id)"
                class="mt-4 w-full bg-red-500 text-white py-2 rounded-lg hover:bg-red-600"
            >
                Return Book
            </button>
            </div>
        </div>
        </div>
    </MainLayout>
  </template>
  
  <script>
  import { ref, onMounted } from "vue";
  import { fetchBorrowedBooks, returnBorrowedBook } from "../services/borrowService";
  import MainLayout from "../layout/MainLayout.vue";

  
  export default {
    components: { MainLayout },
    setup() {
      const books = ref([]);
      const message = ref("");
      const loading = ref(true);
  
      const loadBorrowedBooks = async () => {
        loading.value = true;
        try {
          const data = await fetchBorrowedBooks();
          if (data.message) {
            message.value = data.message;
          } else { 
            books.value = data.results;
          }
        } catch (error) {
          console.error("Error fetching borrowed books:", error);
        } finally {
          loading.value = false;
        }
      };
  
      const returnBook = async (bookId) => {
        try {
          await returnBorrowedBook(bookId);
          books.value = books.value.filter(book => book.id !== bookId);
          alert("Book returned successfully!");
          window.location.reload(); 
        } catch (error) {
          console.error("Error returning book:", error);
          alert(error.response?.data?.error || "Failed to return book.");
        }
      };
  
      const formatDate = (date) => {
        return date ? new Date(date).toLocaleDateString() : "N/A";
      };
  
      onMounted(loadBorrowedBooks);
  
      return { books, message, loading, returnBook, formatDate };
    },
  };
  </script>
  