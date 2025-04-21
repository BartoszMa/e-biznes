import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Products from "./components/Products";
import Payments from "./components/Payments";
import CartView from "./components/CartView";
import Navbar from "./components/Navbar";

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Products />} />
                <Route path="/payments" element={<Payments />} />
                <Route path="/cart/:id" element={<CartView />} />
            </Routes>
        </Router>
    );
}

export default App;
