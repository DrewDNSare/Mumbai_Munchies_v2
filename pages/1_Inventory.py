import streamlit as st
st.title("Inventory Page")
import pickle as pk
import datetime as dt

# ----- imports from internal modules ------

from core.data_store import load_inventory 

from core.services import add_snack, remove_snack , place_on_hold , remove_hold , list_inventory_for_UI


#-------------------Table for all snacks-----------------------------------------------------

data = load_inventory()
data_for_table = list_inventory_for_UI(data)
st.table(data_for_table)

#-------------------Add a Snack--------------------------------------------------------------

st.header("Add a Snack")

with st.form(key="Add_Snack_Form") :
    new_id = 101
    ids = {ea["id"] for ea in data}
    while new_id in ids : 
        new_id += 1
    name = st.text_input("New Snack Name : ")
    price = st.number_input("Price in $ : ", min_value = 0.00, step = .01, format = "%.2f")
    stock_qty = st.number_input("Total Starting Stock Amount : ",min_value = 0 , step = 1)
    on_hold = False 
    add_data = {"id":new_id,"name":name,"price":price,"stock_qty":stock_qty,"on_hold":on_hold}
    add_submit_button = st.form_submit_button("Submit")

if add_submit_button :
    add_result = add_snack(add_data)
    if add_result == False :
        st.write("Error Occured : Quantity may not be below 0 : Add not Succesful")
    else: 
        st.write(f"{add_data['name']} Succesfully Added to the inventory")
        st.rerun()