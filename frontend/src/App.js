import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setAnswer("");
    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });
    const data = await res.json();
    setAnswer(data.answer);
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h2>University Assistant</h2>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a question..."
          style={{ width: "80%", padding: "0.5rem" }}
        />
        <button type="submit" disabled={loading} style={{ padding: "0.5rem" }}>
          {loading ? "Thinking..." : "Ask"}
        </button>
      </form>
      {answer && (
        <div style={{ marginTop: "1rem", background: "#f0f0f0", padding: "1rem" }}>
          <strong>Answer:</strong>
          <div>{answer}</div>
        </div>
      )}
    </div>
  );
}

export default App;