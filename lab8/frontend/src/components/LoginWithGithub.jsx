function LoginWithGithub() {
    const handleGithubLogin = () => {
        window.location.href = "http://localhost:8000/auth/github";
    };

    return (
        <button onClick={handleGithubLogin}>
            Zaloguj przez Github
        </button>
    );
}

export default LoginWithGithub;
