import streamlit as st
st.title("Inventory Page")
import pickle as pk
import datetime as dt
import time

# ----- imports from internal modules ------

from core.data_store import load_inventory 

from core.services import add_snack, remove_snack ,  place_on_hold , remove_hold , list_inventory_for_UI , assign_new_id , list_of_current_ids


#-------------------Table for all snacks-----------------------------------------------------

data = load_inventory()
data_for_table = list_inventory_for_UI(data)
st.table(data_for_table)

#-------------------Add a Snack--------------------------------------------------------------

st.header("Add a Snack")

with st.form(key="Add_Snack_Form") :
    new_id = assign_new_id()
    name = st.text_input("New Snack Name : ")
    price = st.number_input("Price in $ : ", min_value = 0.00, step = .01, format = "%.2f")
    stock_qty = st.number_input("Total Starting Stock Amount : ",min_value = 0 , step = 1)
    on_hold = False 
    add_data = {"id":new_id,"name":name,"price":price,"stock_qty":stock_qty,"on_hold":on_hold}
    add_submit_button = st.form_submit_button("Submit")

if add_submit_button :
    add_result , add_message = add_snack(add_data)
    st.toast(add_message,icon="ℹ️")
    st.warning("Refreshing...")
    time.sleep(4)
    st.rerun()
    
#-----------------Remove Snack-----------------------------------------------

st.header("Remove a Snack")
with st.form(key="remove_snack_form") :
    options = list_of_current_ids()
    selected_for_removal = st.multiselect("Please Choose the ID of the Snack you wish to remove : ",options)
    # I'm thinking that the multiselect makes the datatype string by default
    remove_submit_button = st.form_submit_button("Submit")

if remove_submit_button :
    for each in selected_for_removal :
        remove_result , result_message = remove_snack(each)
        st.toast(result_message,icon="ℹ️")
        st.warning("Refeshing...")
        time.sleep(4)
    st.rerun()



#-----------------Place on Hold----------------------------------------------


#-----------------Remove Hold------------------------------------------------


#-----------------Update Qty-------------------------------------------------

# Product Loss
# Shipment Receieved