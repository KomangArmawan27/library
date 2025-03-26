<template>
    <MainLayout>
        <div class="p-4">
            <h1 class="text-2xl font-bold mb-4">Manage Books</h1>

            <!-- Add Book Button -->
            <button 
                @click="openModal(null)" 
                class="bg-green-500 text-white px-4 py-2 rounded mb-4"
            >
                + Add Book
            </button>

            <!-- Book List -->
            <div v-if="loading">Loading books...</div>
            <div v-else-if="error" class="text-red-500">{{ error }}</div>
            <table v-else class="w-full border-collapse border border-gray-300">
                <thead>
                    <tr class="bg-gray-200">
                        <th class="border p-2">Title</th>
                        <th class="border p-2">Author</th>
                        <th class="border p-2">Published Date</th>
                        <th class="border p-2">Status</th>
                        <th class="border p-2">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="book in books" :key="book.id">
                        <td class="border p-2">{{ book.title }}</td>
                        <td class="border p-2">{{ book.author }}</td>
                        <td class="border p-2">{{ book.published_date }}</td>
                        <td class="border p-2">
                            <span v-if="book.is_borrowed" class="text-red-500">Borrowed</span>
                            <span v-else class="text-green-500">Available</span>
                        </td>
                        <td class="border p-2 flex justify-center gap-2">
                            <button @click="openModal(book)" class="bg-blue-500 text-white px-3 py-1 rounded">
                                Edit
                            </button>
                            <button @click="confirmDelete(book.id)" class="bg-red-500 text-white px-3 py-1 rounded">
                                Delete
                            </button>
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

            <!-- Add/Edit Book Modal -->
            <div v-if="showModal" class="fixed inset-0 bg-gray-900 bg-opacity-50 flex items-center justify-center">
                <div class="bg-white p-6 rounded w-96">
                    <h2 class="text-xl font-bold mb-4">{{ editingBook ? "Edit Book" : "Add Book" }}</h2>
                    <input v-model="form.title" type="text" placeholder="Title" class="border p-2 rounded w-full mb-2"/>
                    <input v-model="form.author" type="text" placeholder="Author" class="border p-2 rounded w-full mb-2"/>
                    <input v-model="form.published_date" type="date" class="border p-2 rounded w-full mb-2"/>
                    <div class="flex justify-end gap-2">
                        <button @click="showModal = false" class="bg-gray-500 text-white px-3 py-1 rounded">Cancel</button>
                        <button @click="saveBook" class="bg-green-500 text-white px-3 py-1 rounded">Save</button>
                    </div>
                </div>
            </div>
        </div>
    </MainLayout>
</template>

<script>
import MainLayout from "../layout/MainLayout.vue";
import { fetchBooks, createBook, updateBook, deleteBook } from "../services/bookService";
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
            showModal: false,
            editingBook: null,
            form: { title: "", author: "", published_date: "" },
        };
    },
    methods: {
        async loadBooks(page) {
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
        openModal(book) {
            this.editingBook = book;
            this.form = book ? { ...book } : { title: "", author: "", published_date: "" };
            this.showModal = true;
        },
        async saveBook() {
            try {
                if (this.editingBook) {
                    await updateBook(this.editingBook.id, this.form);
                } else {
                    await createBook(this.form);
                }
                this.showModal = false;
                this.loadBooks(1);
            } catch (err) {
                alert("Failed to save book.");
            }
        },
        confirmDelete(bookId) {
            if (confirm("Are you sure you want to delete this book?")) {
                this.removeBook(bookId);
            }
        },
        async removeBook(bookId) {
            try {
                await deleteBook(bookId);
                this.loadBooks(1);
            } catch (err) {
                alert("Failed to delete book.");
            }
        },
    },
    created() {
        this.loadBooks(1);
    },
};
</script>
