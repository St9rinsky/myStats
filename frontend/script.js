
const fileInput = document.getElementById("fileInput");
const uploadButton = document.getElementById("uploadButton");
const uploadStatus = document.getElementById("uploadStatus");
const datasetProfile = document.getElementById("datasetProfile");

uploadButton.addEventListener("click", async () => {

    const file = fileInput.files[0];

    if (!file) {
        uploadStatus.textContent = "Please select a CSV file.";
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    uploadStatus.textContent = "Processing dataset...";
    uploadButton.disabled = true;

    try {
        const response = await fetch("/api/datasets/preview", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Upload failed.");
        }

        uploadStatus.textContent = "Dataset processed successfully!";

        datasetProfile.innerHTML = `
            <h3>${result.filename}</h3>
            <p>Rows: ${result.total_rows}</p>
            <p>Columns: ${result.total_columns}</p>
            <h4>Column information</h4>
            <pre>${JSON.stringify(result.columns, null, 2)}</pre>
            <h4>Sample records</h4>
            <pre>${JSON.stringify(result.sample_data, null, 2)}</pre>
        `;

    } catch (error) {
        uploadStatus.textContent = error.message;
    } finally {
        uploadButton.disabled = false;
    }
});


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
