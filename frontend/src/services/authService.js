import api from "./api";

export const registerUser = async (userData) => {
  return api.post("/api/register", userData);
};

export const loginUser = async (credentials) => {
  return api.post("/api/login", credentials);
};

export const logoutUser = () => {
  localStorage.removeItem("token");
};
