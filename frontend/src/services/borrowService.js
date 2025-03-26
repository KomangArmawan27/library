import api from "./api";

// Fetch all borrowed books for the logged-in user
export const fetchBorrowedBooks = async () => {
  try {
    const response = await api.get("/api/borrowed-books/");
    return response.data;
  } catch (error) {
    console.error("Error fetching borrowed books:", error);
    throw error;
  }
};

// Return a borrowed book
export const returnBorrowedBook = async (bookId) => {
  try {
    await api.post(`/api/books/${bookId}/return_book/`);
  } catch (error) {
    console.error("Error returning book:", error);
    throw error;
  }
};
