import { useEffect, useState } from "react";
import axios from "axios";

function Products() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios
            .get("http://localhost:4000/product", {
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then((res) => setProducts(res.data))
            .catch(console.error);
    }, []);

    return (
        <div>
            <h2>Produkty</h2>
            <ul>
                {products.map((p) => (
                    <li key={p.ID}>
                        {p.name} - {p.price} zł
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Products;
