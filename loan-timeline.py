import streamlit as st

st.title("Loan Timeline Calculator")
st.write("This tool helps you visualize the timeline of your loan payments.")

principal = st.number_input("Principal Amount ($)", min_value=0.0, value=1000.0)

months_number = st.number_input("Number of Months", min_value=1, max_value=48, value=12)
monthly_interest_rate = st.number_input("Monthly Interest Rate (%)", min_value=0.0, max_value=100.0, value=1.0)

if st.button("Calculate"):
    monthly_interest_rate /= 100  # Convert percentage to decimal
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months_number)
    total_payment = monthly_payment * months_number
    total_interest = total_payment - principal

    st.write(f"Monthly Payment: ${monthly_payment:.2f}")
    st.write(f"Total Payment: ${total_payment:.2f}")
    st.write(f"Total Interest Paid: ${total_interest:.2f}")

    # Create a timeline of payments
    st.write("### Payment Timeline")
    for month in range(1, months_number + 1):
        st.write(f"Month {month}: ${monthly_payment:.2f} payment")
    st.write("### How to Use:")
    st.write("1. Enter the principal amount of the loan.")
    st.write("2. Specify the number of months for the loan term (1 to 48 months).")
    st.write("3. Input the monthly interest rate as a percentage (e.g., 1 for 1%).")
    st.write("4. Click the 'Calculate' button to see the results.")
    st.write("### Example:")
    st.write("For a principal of $1000, 12 months, and a monthly interest rate of 1%, the monthly payment will be approximately $87.92.")
    st.write("### Note:")
    st.write("This is a basic calculator and does not include additional fees or taxes that may apply to your loan.")
    st.write("### Disclaimer:")

    st.write("This calculator is for informational purposes only and does not constitute financial advice. Please consult a financial advisor for personalized advice.")
    st.write("The calculations are based on the inputs provided and may not reflect actual loan terms or conditions.")
    st.write("The results may vary based on the lender's terms and conditions.")
    st.write("By using this calculator, you acknowledge that you understand the limitations and assumptions of the calculations provided.")
    st.write("Always read the terms and conditions of your loan agreement carefully before proceeding.")
    st.write("This calculator does not account for any additional fees, taxes, or insurance that may apply to your loan.")
    st.write("Ensure you understand the total cost of your loan, including interest and any additional charges.")
    st.write("This calculator is intended to provide a basic understanding of loan payments and should not be used as a substitute for professional financial advice.")

    