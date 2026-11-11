
async function checkBackend() {
    const status = document.getElementById("status");

    try {
        const response = await fetch("/api/health");
        const data = await response.json();

        status.textContent = `Backend: ${data.status}`;
    } catch (error) {
        status.textContent = "Backend: unavailable";
    }
}

checkBackend();
