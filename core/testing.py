#The purpose of this file is for very very rudimentary testing
from .data_store import load_inventory,save_inventory,load_sales,save_sales
from .services import add_snack,remove_snack, place_on_hold, remove_hold

def _wipe_inventory() :
    inv = load_inventory()
    print(f"Inventory before wipe : \n {inv}\n")
    inv = []
    save_inventory(inv)
    inv = load_inventory()
    print(f"Inventory after wipe : \n {inv}")

# _wipe_inventory()


# ----Add Snack Testing
# test_snack1 = {"id":101,"name":"example_snack1","price":101,"stock_qty":101,"on_hold":False}
# test_snack2 = {"id":102,"name":"example_snack2","price":102,"stock_qty":102,"on_hold":False}
# add_snack(test_snack1)
# add_snack(test_snack2)


#----Remove Snack Testing
# remove_snack(101)
# remove_snack(102)

#----Place On-hold Testing
# place_on_hold(101)
# place_on_hold(102)

#----Remove Hold Testing
# remove_hold(101)
# remove_hold(102)


inv = load_inventory()
print(inv)

# for ea in inv : 
#     print(ea["id"])