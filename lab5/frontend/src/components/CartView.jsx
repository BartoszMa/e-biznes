import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

function CartView() {
    const { id } = useParams();
    const [cart, setCart] = useState(null);

    useEffect(() => {
        axios
            .get(`http://localhost:4000/cart/${id}`, {
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then((res) => setCart(res.data))
            .catch(console.error);
    }, [id]);

    if (!cart) return <p>Ładowanie koszyka...</p>;

    return (
        <div>
            <h2>Koszyk #{cart.ID}</h2>
            {cart.cart_items?.length > 0 ? (
                cart.cart_items.map((item) => (
                    <li key={item.ID}>
                        {item.product?.name} - {item.product?.price} zł
                    </li>
                ))
            ) : (
                <p>Koszyk jest pusty</p>
            )}
        </div>
    );
}

export default CartView;
