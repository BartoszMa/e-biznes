import React, { useState } from "react";

export default function ChatInput({ onSend }) {
    const [input, setInput] = useState("");

    const handleSend = () => {
        if (input.trim()) {
            onSend(input);
            setInput("");
        }
    };

    return (
        <div>
      <textarea
          rows={4}
          style={{ width: "100%" }}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter your message..."
      />
            <button
                onClick={handleSend}
                style={{ marginTop: 8, padding: "8px 16px" }}
                disabled={!input.trim()}
            >
                Send
            </button>
        </div>
    );
}
