import { useState } from "react";
import { askCDP } from "./api";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleAsk = async () => {
    const answer = await askCDP(query);
    setResponse(answer);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">CDP Chatbot</h1>
      <textarea
        className="w-96 p-2 border rounded"
        rows="3"
        placeholder="Ask about Segment, mParticle, Lytics, Zeotap..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button className="mt-2 p-2 bg-blue-500 text-white rounded" onClick={handleAsk}>
        Ask
      </button>
      {response && (
        <div className="mt-4 p-4 bg-white border rounded w-96">
          <strong>Response:</strong> <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
