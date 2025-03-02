import axios from "axios";

export const askCDP = async (query) => {
  const response = await axios.post("http://localhost:8000/ask", { query });
  return response.data.response;
};
