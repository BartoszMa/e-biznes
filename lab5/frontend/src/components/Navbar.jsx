import { Link } from "react-router-dom";

function Navbar() {
    return (
        <nav>
            <Link to="/">Produkty</Link> |{" "}
            <Link to="/payments">Płatności</Link> |{" "}
            <Link to="/cart/1">Koszyk</Link>
        </nav>
    );
}

export default Navbar;
