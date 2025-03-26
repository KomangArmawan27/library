<template>
    <MainLayout>
        <div class="p-4">
            <h1 class="text-2xl font-bold mb-4">Book List</h1>

            <!-- Search & Filter -->
            <div class="mb-4 flex gap-4">
                <input 
                    v-model="searchQuery" 
                    @input="fetchPage(1)" 
                    type="text" 
                    placeholder="Search by title or author..." 
                    class="border p-2 rounded w-full"
                />
                <select v-model="filterAvailable" @change="fetchPage(1)" class="border p-2 rounded">
                    <option value="">All</option>
                    <option value="true">Available</option>
                    <option value="false">Borrowed</option>
                </select>
            </div>

            <!-- Book List -->
            <div v-if="loading">Loading books...</div>
            <div v-else-if="error" class="text-red-500">{{ error }}</div>
            <table v-else class="w-full border-collapse border border-gray-300">
                <thead>
                    <tr class="bg-gray-200">
                        <th class="border p-2">Title</th>
                        <th class="border p-2">Author</th>
                        <th class="border p-2">Available</th>
                        <th class="border p-2">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="book in books" :key="book.id">
                        <td class="border p-2">{{ book.title }}</td>
                        <td class="border p-2">{{ book.author }}</td>
                        <td class="border p-2">
                            <span v-if="book.is_borrowed" class="text-red-500">Borrowed</span>
                            <span v-else class="text-green-500">Available</span>
                        </td>
                        <td class="border p-2 text-center">
                            <button 
                                v-if="!book.is_borrowed" 
                                @click="confirmBorrow(book)" 
                                class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
                            >
                                Borrow
                            </button>
                            <span v-else class="text-gray-500">N/A</span>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Pagination -->
            <Pagination 
                :currentPage="currentPage" 
                :nextPage="nextPage" 
                :prevPage="prevPage" 
                @change-page="fetchPage"
            />
        </div>
    </MainLayout>
</template>

<script>
import MainLayout from "../layout/MainLayout.vue";
import { fetchBooks, borrowBookById } from "../services/bookService";
import Pagination from "../components/Pagination.vue";

export default {
    components: { MainLayout, Pagination },
    data() {
        return {
            books: [],
            loading: true,
            error: "",
            currentPage: 1,
            nextPage: null,
            prevPage: null,
            searchQuery: "",
            filterAvailable: "",
        };
    },
    methods: {
        async fetchPage(page) {
            if (!page) return;
            this.loading = true;
            this.error = "";

            try {
                const response = await fetchBooks(page, this.searchQuery, this.filterAvailable);
                this.books = response.results;
                if (this.books.length < 1) {
                    this.error = "No books found.";
                } else {
                    this.error = ""; 
                }
                this.currentPage = page;
                this.nextPage = response.next ? this.currentPage + 1 : null;
                this.prevPage = response.previous ? this.currentPage - 1 : null;
            } catch (err) {
                console.error("Failed to fetch books:", err);
                this.error = "Failed to load books. Please try again.";
            } finally {
                this.loading = false;
            }
        },

        async confirmBorrow(book) {
            const confirmation = confirm(`Are you sure you want to borrow "${book.title}" by ${book.author}?`);
            if (confirmation) {
                this.borrowBook(book.id);
            }
        },

        async borrowBook(bookId) {
            try {
                await borrowBookById(bookId);
                alert("Book borrowed successfully!");
                this.fetchPage(this.currentPage); // Refresh book list
            } catch (error) {
                console.error("Error borrowing book:", error);
                alert(error.response?.data?.error || "Failed to borrow book.");
            }
        }
    },
    created() {
        this.fetchPage(1);
    },
};
</script>
