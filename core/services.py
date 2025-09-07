# --------import from .data_store ---------------------

from .data_store import load_inventory , save_inventory , load_sales , save_sales

#---------other imports--------------------------------

import datetime as dt

#---------internal helper functions--------------------

def _find_index_by_id(inventory_list,snack_id) :
    for index, each_item in enumerate(inventory_list) :
        if each_item["id"] == snack_id :
            return index
    return None

#---------exportable functions-------------------------

#----Inventory Updates-------------------------
#--list for Inventory Table

def list_inventory_for_UI(inventory_list) :
    return [{**each_item,"available":each_item["stock_qty"] > 0 and not each_item["on_hold"]} for each_item in inventory_list]

#--Add Snack

def add_snack(snack):  # dict: {id, name, price, initially_on-hold?} -- maybe I could use a form in Streamlit to collect?
    Success = True
    inv = load_inventory()
    # if _find_index_by_id(inv,snack["id"]) != None :
    #     print("This snack already exists, try again")
    #     return
    if snack["stock_qty"] < 0 :
        # print("Snack quantity must not be below 0\nPlease try again")
        Success = False
        return Success
    # print(inv,"\n\n")
    inv.append(snack)
    save_inventory(inv)
    return Success
    # print(inv,"\n\n")
    

#--Remove Snack

def remove_snack(snack_id) :
    inv = load_inventory()
    index = _find_index_by_id(inv,snack_id)
    if index == None :
        print("The snack you are trying to delete does not exist.\nPlease try again.")
        return
    inv.remove(inv[index])
    save_inventory(inv)

#--Place On-hold

def place_on_hold(snack_id) :
    inv = load_inventory()
    index = _find_index_by_id(inv,snack_id)
    if index == None :
        print("The snack you are trying to place on-hold does not exist.\nPlease try again.")
        return
    elif inv[index]["on_hold"] == True :
        print("The snack you are trying to place on-hold is already on-hold.\nPlease try again.")
        return
    inv[index]["on_hold"] = True 
    save_inventory(inv)

#--Remove Hold

def remove_hold(snack_id) :
    inv = load_inventory()
    index = _find_index_by_id(inv,snack_id)
    if index == None :
        print("The snack you are trying to remove hold does not exist.\nPlease try again.")
        return
    elif inv[index]["on_hold"] == False :
        print("The snack you are trying to remove hold is already not on-hold.\nPlease try again.")
        return
    inv[index]["on_hold"] = False
    save_inventory(inv)

#----Sales Updates and View-------------------

def _subtract_stock(snack_id,qty_to_remove) :
    inv = load_inventory()
    index = _find_index_by_id(inv,snack_id)
    if index == None :
        print("The snack you are trying to update quantity for does not exist\nPlease try again.")
        return
    elif inv[index]["stock_qty"] <= 0 :
        print("The snack you are trying to update quantity for is ")
        

#--Record a Sale


