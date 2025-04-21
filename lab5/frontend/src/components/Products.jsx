import { useEffect, useState } from "react";

function Products() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch("http://localhost:4000/product")
            .then((res) => res.json())
            .then(setProducts)
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
