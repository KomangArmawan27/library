import api from "./api";

export async function fetchBooks(page = 1, search = "", isAvailable = "") {
    try {
        const params = new URLSearchParams();
        params.append("page", page);
        if (search) params.append("search", search); // Search title or author
        if (isAvailable !== "") params.append("is_available", isAvailable); 

        const response = await api.get(`/api/books/?${params.toString()}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching books:", error.response?.data || error.message);
        throw error;
    }
}

export const borrowBookById = async (bookId) => {
    return api.post(`/api/books/${bookId}/borrow/`);
};

// Create a new book (Librarian only)
export const createBook = async (bookData) => {
    try {
        const response = await api.post("/api/books/", bookData);
        return response.data;
    } catch (error) {
        console.error("Error creating book:", error.response?.data || error.message);
        throw error;
    }
};

// Update an existing book (Librarian only)
export const updateBook = async (bookId, bookData) => {
    try {
        const response = await api.put(`/api/books/${bookId}/`, bookData);
        return response.data;
    } catch (error) {
        console.error("Error updating book:", error.response?.data || error.message);
        throw error;
    }
};

// Delete a book (Librarian only)
export const deleteBook = async (bookId) => {
    try {
        await api.delete(`/api/books/${bookId}/`);
    } catch (error) {
        console.error("Error deleting book:", error.response?.data || error.message);
        throw error;
    }
};