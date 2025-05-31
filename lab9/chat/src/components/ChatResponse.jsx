import React from "react";

export default function ChatResponse({ response, loading }) {
    return (
        <div
            style={{
                marginTop: 16,
                whiteSpace: "pre-wrap",
                background: "#f1f1f1",
                color: "#000",
                padding: 16,
                borderRadius: 6,
                minHeight: 100,
            }}
        >
            {loading ? "Loading..." : response}
        </div>
    );
}
