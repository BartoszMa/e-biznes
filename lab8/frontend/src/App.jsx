import './App.css'
import LoginForm from "./components/LoginForm.jsx";
import { useState } from "react";
import ProtectedContent from "./components/ProtectedContent.jsx";

function App() {
    const [showLogin, setShowLogin] = useState(false);

    const toggleLogin = () => {
        setShowLogin(!showLogin);
    };

    return (
        <>
            <div className="card">
                <button onClick={toggleLogin}>
                    {showLogin ? "Close Login" : "Login"}
                </button>
                {showLogin && <LoginForm />}
            </div>
            <div className="card">
                <ProtectedContent />
            </div>
        </>
    );
}

export default App;
