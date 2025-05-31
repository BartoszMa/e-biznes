import React, { useState } from "react";
import ChatInput from "./components/ChatInput";
import ChatResponse from "./components/ChatResponse";

export default function App() {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSend(message) {
    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          messages: [{ role: "user", content: message }],
        }),
      });

      if (!res.ok) {
        const err = await res.text();
        setResponse("Error: " + err);
        setLoading(false);
        return;
      }

      const data = await res.json();

      setResponse(data.message?.content || "Brak odpowiedzi.");
    } catch (e) {
      setResponse("Error: " + e.message);
    }

    setLoading(false);
  }


  return (
      <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "sans-serif" }}>
        <h1>Chat with Ollama</h1>
        <ChatInput onSend={handleSend} />
        <ChatResponse response={response} loading={loading} />
      </div>
  );
}
