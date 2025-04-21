import { useState } from "react";

function Payments() {
    const [price, setPrice] = useState("");
    const [isPayed, setIsPayed] = useState(false);
    const [response, setResponse] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch("http://localhost:4000/payments", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ price: parseFloat(price), is_payed: isPayed })
        })
            .then((res) => res.json())
            .then(setResponse)
            .catch(console.error);
    };

    return (
        <div>
            <h2>Płatności</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Kwota:
                    <input
                        type="number"
                        step="0.01"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                    />
                </label>
                <label>
                    Opłacono:
                    <input
                        type="checkbox"
                        checked={isPayed}
                        onChange={(e) => setIsPayed(e.target.checked)}
                    />
                </label>
                <button type="submit">Wyślij płatność</button>
            </form>
            {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
        </div>
    );
}

export default Payments;
