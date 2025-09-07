#-----importing path & pickle------------------------
from pathlib import Path 
import pickle

#Suggestions to self for later improvement --
# 1) could add 2 new sections to the snack database , "brand, "snack_flavor"
# 2) could later add a new section to the database for "supplier" and maybe even "price_paid" so that I can distinguish price I paid, vs the price I could sell it for
# 3) I could also add update_pricing() and update_qty() as functions that would get pulled from back end into the front end as forms on streamlit

#-----refencing MMv2 Directory--------

ROOT = Path(__file__).resolve().parent.parent # goes 2 directories up --> core --> MMv2
DATA_DIR = ROOT/"data"
DATA_DIR.mkdir(exist_ok=True) # this will make the data directory if it does not already exist

#-------referencing the pickle data files-------------

INV_PATH = DATA_DIR/"inventory.pkl"
SALES_PATH = DATA_DIR/"sales.pkl"


#------section for functions---------------------------
    #--read inventory-pickle-file

def load_inventory() :
    if INV_PATH.exists() and INV_PATH.stat().st_size > 0:
        with INV_PATH.open("rb") as f:
            return pickle.load(f)
    else: 
        with INV_PATH.open("wb") as f:
            pickle.dump([],f)
        with INV_PATH.open("rb") as f:
            return pickle.load(f)

    #--write to the inventory-pickle-file 

def save_inventory(input_items) :
    with INV_PATH.open("wb") as f :
        pickle.dump(input_items,f)
        
    #--read sales-pickle-file

def load_sales() :
    if SALES_PATH.exists() and SALES_PATH.is_file() and INV_PATH.stat().st_size > 0:
        with SALES_PATH.open("rb") as f:
            return pickle.load(f)
    else: 
        with SALES_PATH.open("wb") as f:
            pickle.dump([],f)
        with SALES_PATH.open("rb") as f:
            return pickle.load(f)

    #--write to sales-pickle-file

def save_sales(input_items) :
    with SALES_PATH.open("wb") as f :
        pickle.dump(input_items,f)




