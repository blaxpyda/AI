import streamlit as st
import pandas as pd


st.title("📊 Data Profiler App")

#Step 1 Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)

    #step 2 Data summary
    st.subheader("📋 Dataset Info")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")
    st.write("Data Types:")
    st.write(df.dtypes)

    st.write("Missing Values:")
    st.write(df.isnull().sum())

    st.write("Unique Values:")
    st.write(df.nunique())

    # Step 3 Column filter
    st.subheader("🔍 Filter Columns")
    selected_columns = st.selectbox("Select column to filer by", df.columns)
    unique_values = df[selected_columns].dropna().unique()
    selected_value = st.selectbox("Select value to filter by", unique_values)
    filtered_df = df[df[selected_columns] == selected_value]
    st.dataframe(filtered_df)

    #Step 4 Grouping
    st.subheader("📊 Grouping Data")
    group_col = st.selectbox("Select column to group by", df.columns)
    agg_col = st.selectbox("Aggregate column", df.select_dtypes(include=['number']).columns)
    agg_func = st.selectbox("Aggregation function", ["mean", "sum", "count", "min", "max"])
    grouped = df.groupby(group_col)[agg_col].agg(agg_func)
    st.dataframe(grouped.reset_index(drop=True))


    # #Step 5 Pivot Table
    # st.subheader("📈 Pivot Table")
    # pivot_index = st.selectbox("Select index for pivot table", df.columns, key="pi").astype(str)
    # pivot_columns = st.selectbox("Select columns for pivot table", df.columns, key="pc")
    # pivot_values = st.selectbox("Select values for pivot table", df.select_dtypes(include=['number']).columns, key="pv")
    # pivot_df = df.pivot_table(index=pivot_index, columns=pivot_columns, values=pivot_values, aggfunc='mean')
    # st.dataframe(pivot_df)

    #Step 6 Download Processed Data
    st.subheader("📥 Download Processed Data")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )
