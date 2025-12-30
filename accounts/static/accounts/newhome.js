class BillManager {
    constructor(){
        this.table = document.getElementById("bills-table");

        this.addButton = document.getElementById("bill_trigger");
        this.updateUI(this.addButton, "show");

        this.tbody = document.querySelector(".bills-body");
        this.setupEvents();
    }
    setupEvents() {
        this.addButton.addEventListener("click", () => {
            this.addBillRow();
        })
        this.table.addEventListener("click", (e) => {
            if (e.target.classList.contains("edit_bill_trigger")){
                console.log(e.target.dataset.name)
            }
        });
    }

    updateUI(element, action) {
        if (action == "show") {
            element.hidden = false;
        } else if (action == "hide"){
            element.hidden = true;
        }


    }


    addBillRow(){
        this.updateUI(this.addButton, "hide");
        const row = document.createElement("tr")
        row.innerHTML = `
        <td><input type="text" name="bill_name" placeholder="Name"></td>
        <td><input type="number" name="bill_amount" placeholder="Amount"></td>
        <td><input type="number" name="bill_pay_day" placeholder="Pay Day"></td>
        <td>
            <button type="submit" name="action" value="add_bill">Save</button>
            <button type="button" class="cancel-bill">Cancel</button>
        </td>
        `
        this.tbody.appendChild(row);

        const cancelButton = row.querySelector(".cancel-bill");

        cancelButton.addEventListener("click", () => {
            row.remove();
            this.updateUI(this.addButton, "show");
        })
    }
    editBillRow() {
        console.log("editing Bill");
        this.editingBill = true;
        this.updateUI();
        const row = document.getElementById("bill-row");
        console.log(row.dataset.name);



    }
}

document.addEventListener("DOMContentLoaded", () => {
    new BillManager();
})