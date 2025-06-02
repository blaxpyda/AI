import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📊 Loan Timeline App")

#User inputs
principal = st.number_input("Principal Amount", min_value=0, value=10000, step=1000)

rate1 = st.number_input("Annual Interest Rate 1(%)", min_value=0.0, value=5.0, step=0.1)
rate2 = st.number_input("Annual Interest Rate 2(%)", min_value=0.0, value=5.0, step=0.1)

years = st.number_input("Loan Term (Years)", min_value=1, value=5, step=1)

months = years * 12

def calc_monthly_payment(P, annual_rate, n_months):
    r = (annual_rate / 100) / 12
    return (P * r * (1+r) ** n_months) / ((1+r) ** n_months -1)

def get_loan_schedule(P, annual_rate, n_months):
    r = (annual_rate / 100) / 12
    payment = calc_monthly_payment(P, annual_rate, n_months)
    balance = P
    schedule = []
    for month in range(1, n_months + 1):
        interest = balance * r
        principal_paid = payment - interest
        balance -= principal_paid
        schedule.append([month, max(balance,0)])
    return pd.DataFrame(schedule, columns=['Month', 'Balance'])

#calculate payments
payment1 = calc_monthly_payment(principal, rate1, months)
payment2 = calc_monthly_payment(principal, rate2, months)

st.markdown(f"**Monthly payment at {rate1}%: ** {payment1:,.2f}")
st.markdown(f"**Monthly payment at {rate2}%: ** {payment2:,.2f}")

total1 = payment1 * months
total2 = payment2 * months

st.markdown(f"** Total paid at {rate1}%: ** {total1}")
st.markdown(f"** Total paid at {rate2}%: ** {total2}")

st.markdown(f"** Total Interest at {rate1}%: {total1:,.2f}")
st.markdown(f"** Total Interest at {rate2}%: {total2:,.2f}")

#Loan schedules
df1 = get_loan_schedule(principal, rate1, months)
df2 = get_loan_schedule(principal, rate2, months)


#Plot loan balances
fig, ax = plt.subplots()
ax.plot(df1["Month"], df1["Balance"], label=f"{rate1}%")
ax.plot(df2["Month"], df2["Balance"], label=f"{rate2}%")
ax.set_xlabel("Month")
ax.set_ylabel("Remaining balance")
ax.set_title("Loan Paydown Timeline")
ax.legend()
ax.grid(True)
st.pyplot(fig)

#Show schedule table
with st.expander("Show Loan Schedules"):
    st.write(f"Loan Schedule at {rate1}%")
    st.dataframe(df1)
    st.write(f"Loan Schedule at {rate2}%")
    st.dataframe(df2) 