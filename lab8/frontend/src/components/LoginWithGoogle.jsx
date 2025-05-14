function LoginWithGoogle() {
    const handleGoogleLogin = () => {
        window.location.href = "http://localhost:8000/auth/google";
    };

    return (
        <button onClick={handleGoogleLogin}>
            Zaloguj przez Google
        </button>
    );
}

export default LoginWithGoogle;
