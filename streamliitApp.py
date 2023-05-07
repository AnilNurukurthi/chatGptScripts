import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Create the dropdown list
options = ["Option 1", "Option 2", "Option 3"]

# Create the date range chooser
start_date = st.date_input("Start date", datetime.now() - timedelta(days=7))
end_date = st.date_input("End date", datetime.now())

# Load the data
df = pd.read_csv("data.csv")

# Create the charts
selected_option = st.selectbox("Select an option", options)
filtered_df = df[(df["Option"] == selected_option) & (df["Date"] >= start_date) & (df["Date"] <= end_date)]
line_chart = px.line(filtered_df, x="Date", y="Value")
bar_chart = px.bar(filtered_df, x="Date", y="Value")

# Display the charts side by side
st.plotly_chart(line_chart, use_container_width=True)
st.plotly_chart(bar_chart, use_container_width=True)
