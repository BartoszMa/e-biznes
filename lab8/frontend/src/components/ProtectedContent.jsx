import { useEffect, useState } from "react";

function ProtectedContent() {
    const [message, setMessage] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem("token");

        if (!token) {
            setError("No token found. Please log in.");
            return;
        }

        fetch("http://localhost:8000/protected", {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })
            .then(res => {
                if (!res.ok) {
                    throw new Error("Unauthorized or invalid token");
                }
                return res.json();
            })
            .then(data => {
                setMessage(data.message);
            })
            .catch(err => {
                setError(err.message);
            });
    }, []);

    return (
        <div>
            <h2>Protected Content</h2>
            {message && <p>{message}</p>}
            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
}

export default ProtectedContent;
