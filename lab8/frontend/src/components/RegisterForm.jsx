import { useState } from "react";

function RegisterForm() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch("http://localhost:8000/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();

        if (response.ok) {
            setMessage("Zarejestrowano pomyślnie!");
        } else {
            setMessage(`Błąd: ${data.detail}`);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Rejestracja</h2>
            <input placeholder="Username" onChange={e => setUsername(e.target.value)} />
            <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
            <button type="submit">Zarejestruj</button>
            {message && <p>{message}</p>}
        </form>
    );
}

export default RegisterForm;
