// For SearchTable
function searchTable() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("searchInput");
  filter = input.value.toUpperCase();
  table = document.querySelector("table");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td");
    for (var j = 0; j < td.length; j++) {
      if (td[j]) {
        txtValue = td[j].textContent || td[j].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
          break; // Show the row if any of its cells match the search query
        } else {
          tr[i].style.display = "none"; // Hide the row if none of its cells match the search query
        }
      }
    }
  }
}

// Newly Added JS
// For passport
document.getElementById("passport").addEventListener("input", function (event) {
  const fileInput = event.target;

  if (fileInput.files && fileInput.files[0]) {
    const passportDisplay = document.getElementById("passport-display");

    // Create image element
    const uploadedPassport = document.createElement("img");
    uploadedPassport.src = URL.createObjectURL(fileInput.files[0]);
    uploadedPassport.classList.add("img-fluid");

    passportDisplay.innerHTML = "";
    passportDisplay.appendChild(uploadedPassport);
  }
});
// Passport End here

// For signature
document
  .getElementById("signature")
  .addEventListener("input", function (event) {
    const fileInput = event.target;

    if (fileInput.files && fileInput.files[0]) {
      const signatureDisplay = document.getElementById("signature-display");

      // Create image element
      const uploadedSignature = document.createElement("img");
      uploadedSignature.src = URL.createObjectURL(fileInput.files[0]);
      uploadedSignature.classList.add("img-fluid");

      signatureDisplay.innerHTML = "";
      signatureDisplay.appendChild(uploadedSignature);
    }
  });
// Newly Added JS End Here
