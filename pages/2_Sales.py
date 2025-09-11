import streamlit as st
import pickle as pk
import datetime as dt
import time

from core.data_store import load_sales , load_inventory
from core.services import record_sale , list_of_current_ids

st.title("Sales Page")

sls = load_sales()
inv = load_inventory()
st.table(sls)

st.header("Record a Sale")

with st.form(key="sales_form") :
    options = list_of_current_ids()
    selected_for_sale = st.selectbox("Please select a snack ID : ", options) # returns a list
    qty_sold = st.number_input("Please input quantity sold : ", min_value = 1 , step = 1)
    submit_sale = st.form_submit_button("Submit")

if submit_sale :
    result, result_message = record_sale(selected_for_sale,qty_sold)
    st.toast(result_message,icon="ℹ️")
    st.warning("Refreshing...")
    time.sleep(4)
    st.rerun()

st.table(inv)