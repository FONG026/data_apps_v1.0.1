import streamlit as st
import pandas as pd
from script.payments import CleanPayments

df_payments = pd.read_csv('data/olist_order_payments_dataset.csv')

# Clean the DataFrame
cleaned_df = CleanPayments.clean(df_payments)

# Display the DataFrame


kpi_results = CleanPayments.kpi(df_payments)

st.metric('Total Payment', kpi_results['Total Payment'])
st.metric('Average Payment', kpi_results['Average Payment'])