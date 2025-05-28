import streamlit as st


st.title("Basic Loan Calculator")

principal = st.number_input("Principal Amount ($)")

months_number = st.number_input("Number of Months", min_value=1, max_value=48, value=1)

monthly_interest_rate = st.number_input("Monthly Interest Rate (%)", min_value=0.0, max_value=100.0, value=1.0)

if st.button("Calculate"):
    monthly_interest_rate /= 100  # Convert percentage to decimal
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months_number)
    total_payment = monthly_payment * months_number
    total_interest = total_payment - principal

    st.write(f"Monthly Payment: ${monthly_payment:.2f}")
    st.write(f"Total Payment: ${total_payment:.2f}")
    st.write(f"Total Interest Paid: ${total_interest:.2f}")

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