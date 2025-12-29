// STATIC DATA //

const paycheck_amount = document.getElementById("paycheck_amount").value;
console.log(paycheck_amount);
const bills = document.getElementById("total_bills")
console.log(bills.value);
let bills_amount;
if (!bills){
    bills_amount = 0;
    console.log("Element not found");
} else {
    bills_amount = bills.value;
    console.log("Found you", bills_amount);
}

// DYNAMICS

const free_amount = paycheck_amount - bills_amount;

const bills_percent = (bills_amount) / paycheck_amount;
const free_percent = 1 - bills_percent

console.log("Free percent:", free_percent);

const bills_degrees = bills_percent * 360;
const free_degrees = 360 - bills_degrees;

const wheel = document.getElementById("money-wheel");
wheel.style.setProperty("--bill-deg", bills_degrees + "deg")
wheel.style.setProperty("--free-deg", "360deg")

console.log(bills_degrees, free_degrees)

