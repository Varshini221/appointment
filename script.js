const dialog = document.getElementById("formDialog");
const API = "http://localhost:5001";
 
// Function to open the pop-up form as a modal
function openForm() {
  dialog.showModal(); 
}

// Function to close the pop-up form
function closeForm() {
  dialog.close();
}

async function submitForm() {
    const serviceName = document.getElementById("name").value.trim();
    const date = document.getElementById("event-date").value;
    const category = document.getElementById("category").value;

    if (!serviceName || !date || !category) {
        alert("please fill in all fields")
        return;
    }
    const services = await fetch(`${API}/services`).then(r=> r.json()); 
}