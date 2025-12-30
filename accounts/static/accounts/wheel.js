// STATIC DATA //

const paycheck_amount = document.getElementById("paycheck_amount").value;
const bills = document.getElementById("total_bills")
let bills_amount;
if (!bills){
    bills_amount = 0;
} else {
    bills_amount = bills.value;
}

// DYNAMICS

const free_amount = paycheck_amount - bills_amount;

const bills_percent = (bills_amount) / paycheck_amount;
const free_percent = 1 - bills_percent


const bills_degrees = bills_percent * 360;
const free_degrees = 360 - bills_degrees;

const wheel = document.getElementById("money-wheel");
wheel.style.setProperty("--bill-deg", bills_degrees + "deg")
wheel.style.setProperty("--free-deg", "360deg")


