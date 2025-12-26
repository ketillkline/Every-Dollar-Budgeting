document.addEventListener("DOMContentLoader", () => {
    const addButton = document.getElementById("bill_trigger");
    const table = document.getElementById("bills-table");
    const addRow = document.getElementById("add-row");

    addButton.addEventListener("click", () => {
        // create new table row
        const newRow = document.createElement("tr");

        //create cells with input fields
        newRow.innerHTML= `
        <td><input type="text" name=""
        `
    })

})