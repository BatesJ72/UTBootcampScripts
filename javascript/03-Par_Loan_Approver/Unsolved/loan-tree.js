// @NOTE: change these to test the code with different values
let income = 95000;
let debtIncomeRatio = .4;
let yearsInJob = .5;
let criminalRecord = true;

// @TODO: Write the Conditional Statements needed to approve or deny a loan

if (income < 30000 & debtIncomeRatio < .5) {
    console.log("No Loan")
} else if (income < 75000 & income >= 30000 & yearsInJob < 1) {
    console.log("No Loan")
} else if (income >= 75000 & criminalRecord === true) {
    console.log("No Loan")
} else {
    console.log("Congrats! You got a loan!")
}
