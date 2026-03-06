import streamlit as st
import pandas as pd

st.title("AI Business Intelligence Copilot")

st.write("Upload your business dataset (CSV file)")

file = st.file_uploader("Upload Dataset", type=["csv"])

if file is not None:

    data = pd.read_csv(file)

    # Clean column names
    data.columns = data.columns.str.strip()

    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    st.subheader("Column Names")
    st.write(list(data.columns))

    if "Sales" in data.columns:

        total_sales = data["Sales"].sum()
        avg_sales = data["Sales"].mean()
        max_sales = data["Sales"].max()

        st.subheader("AI Insights")

        st.write("Total Sales:", total_sales)
        st.write("Average Sales:", avg_sales)
        st.write("Highest Sale:", max_sales)

    else:

        st.warning("No 'Sales' column found in dataset.")

        st.write("Please upload dataset with a Sales column.")