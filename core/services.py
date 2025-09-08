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
    success = False
    inv = load_inventory()
    # if _find_index_by_id(inv,snack["id"]) != None :
    #     print("This snack already exists, try again")
    #     return
    if snack["stock_qty"] < 0 :
        # print("Snack quantity must not be below 0\nPlease try again")
        return success
    # print(inv,"\n\n")
    inv.append(snack)
    save_inventory(inv)
    sucess = True
    return success
    # print(inv,"\n\n")
    

#--Remove Snack

def remove_snack(snack_id) :
    success = False
    message = ""
    inv = load_inventory()
    index = _find_index_by_id(inv,snack_id)
    if index == None :
        message = "Error : Action not Succesful : The snack you are trying to delete does not exist."
        return success , message
    else :
        removal_message = ""
        success = True
        message = "\nAction Succesful : Snack ID :",snack_id,"|","Snack Name :",inv[index]["name"] ,"has been successfully removed from the inventory"
        for ea in message :
            removal_message += str(ea)
            removal_message += " "
        message = removal_message
        inv.remove(inv[index])
        save_inventory(inv)
        return success, message

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
    success, message = False , ""
    inv = load_inventory()
    index = _find_index_by_id(inv,snack_id)
    if index == None :
        message = "Error : Action not Succesful : The snack you are trying to remove hold from does not exist."
        return success , message
    elif inv[index]["on_hold"] == False :
        message = "Error : Action not Succesful : The snack you are trying to remove hold from is already not on-hold."
        return success , message
    else : 
        inv[index]["on_hold"] = False
        save_inventory(inv)
        success = True
        message = ("Action Succesful : Hold has been removed from Snack ID :",snack_id,"|","Snack Name :",inv[index]["name"])
        success_message = ""
        for ea in message : 
            success_message += str(ea)
            success_message += " "
        return success , success_message

#----Sales Updates and View-------------------

def _subtract_stock(snack_id,qty_to_remove) :
    success = False
    message = ""
    inv = load_inventory()
    index = _find_index_by_id(inv,snack_id)
    if index == None :
        message = "Error : Action Not Succesful :The snack you are trying to update quantity for does not exist\nPlease try again."
        return success , message
    elif inv[index]["stock_qty"] <= 0 :
        message = "Error : Action Not Succesful : The snack you are trying to update quantity for is "
        return success , message
    elif ((inv[index]["stock_qty"]) - qty_to_remove <= 0 ) :
        message = "Error: Action Not Succesful : You cannot subtract more quantity than currently in inventory."
        return success , message 
    else :
        inv[index]["stock_qty"] -= qty_to_remove
        save_inventory(inv)
        success = True 
        message = ("Action Succesful : Stock Subtracted from Snack ID :",snack_id,"|","Snack Name :",inv[index]["name"],"\nPrevious Stock Quantity : ",inv[index]["stock_qty"]+qty_to_remove,"\nCurrent Stock Quantity :",inv[index]["stock_qty"])
        success_message = ""
        for ea in message :
            success_message += str(ea)
            success_message += " "
        return success , success_message
        

#--Record a Sale

def record_sale(snack_id,qty_sold) :
    success = False 
    message = " "
    inv = load_inventory() 
    index = _find_index_by_id(inv,snack_id)
    subtract_stock_success , subtract_message = _subtract_stock(snack_id,qty_sold) # assigns a Boolean and the message from the internal function _subtract_stock()
    if subtract_stock_success == False :
        message = "Error : Action not Succesful : Item Unable to be Sold\n"
        return success , message , subtract_message
    else : 
        success = True 
        message = "Action Succesful : Item Sold\n"
        message += subtract_message
        return success , message 
    