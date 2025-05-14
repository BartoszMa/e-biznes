import './App.css'
import LoginForm from "./components/LoginForm.jsx";
import { useState } from "react";
import ProtectedContent from "./components/ProtectedContent.jsx";
import RegisterForm from "./components/RegisterForm.jsx";
import LoginWithGoogle from "./components/LoginWithGoogle.jsx";

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
            <div className="card">
                <RegisterForm/>
            </div>
            <div className="card">
                <LoginWithGoogle/>
            </div>
        </>
    );
}

export default App;
