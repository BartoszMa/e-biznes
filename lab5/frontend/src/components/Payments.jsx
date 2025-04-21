import { useState } from "react";
import axios from "axios";

function Payments() {
    const [price, setPrice] = useState("");
    const [isPayed, setIsPayed] = useState(false);
    const [response, setResponse] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();

        axios
            .post("http://localhost:4000/payments", {
                price: parseFloat(price),
                is_payed: isPayed
            }, {
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then((res) => setResponse(res.data))
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
